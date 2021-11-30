 
if not os.path.exists("processed_data"):
    os.makedirs("processed_data")
if not os.path.exists("processed_data/train"):
    os.makedirs("datasets1/train")
if not os.path.exists("processed_data/test"):
    os.makedirs("processed_data/test")
path="data0"
path1 = "processed_data"
a=['label']

for i in range(64*64):
    a.append("pixel"+str(i))
    
label=0
var = 0
c1 = 0
c2 = 0

for (dirpath,dirnames,filenames) in os.walk(path):
    for dirname in dirnames:
        print(dirname)
        for(direcpath,direcnames,files) in os.walk(path+"/"+dirname):
       	    if not os.path.exists(path1+"/train/"+dirname):
                os.makedirs(path1+"/train/"+dirname)
            if not os.path.exists(path1+"/test/"+dirname):
                os.makedirs(path1+"/test/"+dirname)
            # num=0.75*len(files)
            num = 5678
            i=0
            for file in files:
                var+=1
                actual_path=path+"/"+dirname+"/"+file
                actual_path1=path1+"/"+"train/"+dirname+"/"+file
                actual_path2=path1+"/"+"test/"+dirname+"/"+file
                img = cv2.imread(actual_path, 0)
                bw_image = func(actual_path)
                if i<num:
                    c1 += 1
                    cv2.imwrite(actual_path1 , bw_image)
                else:
                    c2 += 1
                    cv2.imwrite(actual_path2 , bw_image)
                    
                i=i+1
                
        label=label+1
print(var)
print(c1)
print(c2)
