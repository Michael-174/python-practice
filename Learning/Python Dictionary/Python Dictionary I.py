marks = {"Math":45,
         "Science":23,
         "Social Science":38}

print(marks["Math"])
print(marks["Science"])

print("***********************************************")
print(marks["Science"])
marks["Science"] = 32
print(marks["Science"])

#use pop to remove an element
marks.pop("Science")
print(marks)

#use clear to delete everything
marks.clear()
print(marks)

