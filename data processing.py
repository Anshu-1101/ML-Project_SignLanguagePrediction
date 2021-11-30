from zipfile import ZipFile

with ZipFile('train.zip', 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall('data0')
   print('File is unzipped for data') 
    
#resizing the images into one same size
    
f = r'data0/Best'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((640,480))
    img.save(f_img)
    
    
    #converting the images into blur and thresholding them
minValue = 70
def func(path):    
    frame = cv2.imread(path)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)

    th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
    ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    return res
