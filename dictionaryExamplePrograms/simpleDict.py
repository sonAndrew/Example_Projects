"""
    File   :  simpleDict.py
    About  :  Exmples of Dictionaries
"""
info = {}
info["name"] = "Sandy"
info["occupation"] = "hacker"
print(info)

# Use [] also to replace a value at an existing key:
info["occupation"] = "manager"
print(info)

# If key is not present in dictionary, an error is raised
print(info["name"]) # This is wont throw an error

# print(info["job"]) # This will throw an error

if "job" in info:
    print(info["job"])
else:
    print("No [key] named 'job'. ")

"""
    About: Removing Keys
"""
print(info.pop("job", None))
print(info.pop("occupation"))
print(info)

"""
    About: To print all of the keys and their values
"""
for key in info:
    print(key, info[key])

"""
    About: Alternative: Use the dictionary method items()
"""
grades = {90: "A", 80: "B", 70: "C"}
print(list(grades.items()))

"""
    About: Entries are represented as tuples within the list
"""
for(key, value) in grades.items():
    print(key, value)

"""
    About: You can sort the list first then traverse it to print 
            the entries of the dictionary in alphabetical order:
"""
theKeys = list(info.keys())
theKeys.sort()
for key in theKeys:
    print(key, info[key])