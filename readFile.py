import os
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    nameDir = []
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    nameDir.append(int(name.split(".")[0]))

                    break
    nameDir.sort()
    for i in nameDir:
        file.write(str(i) + ".jpg" + "\n")
def Test():
  dir="/home/lyw/datasets/Camera"
  outfile="nameinfo.txt"
  wildcard = ".jpg"

  file = open(outfile,"w")
  if not file:
    print ("cannot open the file %s for writing" % outfile)
  ListFilesToTxt(dir,file,wildcard, 1)

  file.close()
Test()