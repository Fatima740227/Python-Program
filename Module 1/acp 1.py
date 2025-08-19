file_read = open('Sample_File.txt', 'r')
#read the file
print(file_read.read())
file_read.close()
#write in the file
file_write = open('Sample_File.txt', 'w')
print(file_write.write)
file_write.write("Hi! Today u will learn about coding")
file_write.close()

file_append = open ('Sample_File.txt', 'a') 
file_append.write(" I  hope u enjoy learning")
file_append.close()