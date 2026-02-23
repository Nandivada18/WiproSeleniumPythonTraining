#Destructors - when we want to destroy the object
#post conditions - closing of the browser, db connecting closing, releasing of certain resources
#clean up operations
#for proper memory usage destructors should be used
#when do connection has to be closed
# free the memory (garbage Collection) which is automatically cleaned
#Destructor runs when program ends or object is garbage collected
class Dest:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Closing the db connection")

a = Dest()
print("End of the program")
del a

#destructor in file handling
class FileHandler:
    def __init__(self,filename):
        self.file = open(filename, 'w')
        print("File is opened")

    def readfile(self,filename):
        print("Reading the file")

    def __del__(self):
        self.file.close()
        print("File closed")

f = FileHandler("text.txt")
f.readfile("text.txt")
del f





