import os
if os.path.exists("demofile.txt"):
    print("File exists!!!")
else:
    print("The file does not exist")
#delete the file
os.remove("Codingal.txt")