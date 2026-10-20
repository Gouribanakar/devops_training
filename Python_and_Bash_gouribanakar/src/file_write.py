# Create a file and write content to it
file = open("sample.txt","w")

file.write("Hello, this is my first file.\n")
file.write("This file was created using open() and write().\n")

file.close()

print("File created and content written successfully.")
