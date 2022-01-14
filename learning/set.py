def print_elements(element):
    for element in element:
        print(element)


myList = ["Ankit", "Kumar", "Chaudhary", "Chaudhary", "Ji"]
myList.remove("Chaudhary")
myList.remove("Chaudhary")

print_elements(myList)

print("==============================")

mySet = {"Ankit", "Kumar", "Chaudhary", "Chaudhary"}
mySet.add("Ankit")
mySet.remove("Ankit")
print_elements(mySet)
