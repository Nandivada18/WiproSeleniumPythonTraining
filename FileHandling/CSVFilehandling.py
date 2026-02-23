import csv

# reading the csv file
with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#writing to the csv file
with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//writecsv.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1,"Rahul",85])
    writer.writerow([2,"Anita",90])

#appending the to csv file
with open("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([3,"kiran",88])
