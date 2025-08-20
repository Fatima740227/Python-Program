import os

with open("sample_file.txt", "w") as f:
    f.write("My name is Fatima Munib. I am in Grade 6 at Roots Millennium Schools. "
            "I love coding, cooking, and drawing. My favorite subjects are English, "
            "Math, and History. My favorite foods are pasta and biryani.")


with open("sample_file.txt", "r") as f:
    contents = f.read()
    words = contents.split()
    print("Words in file:", words)


if os.path.exists("My_File.txt"):
    print("My_File.txt exists")
else:
    print("My_File.txt does not exist")

    with open("My_File.txt", "w") as f:
        f.write("My name is Fatima Munib. I am in Grade 6 at Roots Millennium Schools. "
                "I love coding, cooking, and drawing. My favorite subjects are English, "
                "Math, and History. My favorite foods are pasta and biryani.")

if os.path.exists("sample_doc.txt"):
    os.remove("sample_doc.txt")
    print("sample_doc.txt deleted")
else:
    print("sample_doc.txt does not exist")
