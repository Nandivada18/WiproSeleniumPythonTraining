import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement

#read xml file

tree = ET.parse("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//employee.xml")
root = tree.getroot() #get the root element
print(root.tag)

#get the first child node / tag
print(root[0].tag)

#get the attributes of thr child node
print(root[0].attrib)
#fetch all the attributes in child node
for x in root.find("employee"):
    print(x.tag, x.text)

for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)
    emp_name = employee.find("name").text
    print(emp_name)

for emp in root.findall("employee"):
    name = emp.find("name").text
    role = emp.find("role").text
    exp = emp.find("experience").text
    print(name,role,exp)

#root ---> child nodes ----> attributes of thr child nodes ----> text of the attribute

#create the child nodes
#create the root element
root = ET.Element("employees")

#create the child elements
emp1 = ET.SubElement(root,"employee", id = "101")
ET.SubElement(emp1,"name").text = "Harsha"
ET.SubElement(emp1, "role").text = "Tester"
ET.SubElement(emp1, "experience").text = "5"

#create the child node 2
emp2 = ET.SubElement(root,"employee", id = "102")
ET.SubElement(emp2,"name").text = "Amit"
ET.SubElement(emp2, "role").text = "Developer"
ET.SubElement(emp2, "experience").text = "3"

#write to the file
tree = ET.ElementTree(root)
ET.indent(tree, space="    ", level=0)
tree.write("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//writexml.xml",encoding="utf-8", xml_declaration=True)

#updating the xml
tree = ET.parse("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//updatexml.xml")
root = tree.getroot()

for emp in root.findall("employee"):
    if emp.get("id") == "101":
        emp.find("experience").text = "16"
ET.indent(tree, space="    ", level=0)
tree.write("C://Users//prasa//PycharmProjects//PythonAdvancePrograming//Dataformats//updatexml.xml",encoding="utf-8", xml_declaration=True)
