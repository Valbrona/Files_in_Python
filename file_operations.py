# define a function which opens a file with a context manager and writes a content to it
# if the file does not exist, it gets created automatically
def save_to_file(content, filename):
    with open(filename, "w") as filename:
        filename_write = filename.write(content)
        return filename_write

# a second function which takes the file, opens the file name with a context manager and reads it fully as a string and returns it
def read_content(filename):
    with open(filename, "r") as filename:
        return filename.readlines()

content = "Hello,\n \tnice to meet you.\n\t\t Hope you are enjoying your day\t." # content can also be changed
file_name = "new_file.txt"  # here a new file name can be provided, and it will create a new one
save_to_file(content,file_name)
read_content(file_name)




