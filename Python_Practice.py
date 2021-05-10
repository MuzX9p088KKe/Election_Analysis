print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]

counties[1] = 'El Paso'
print(counties)
counties.pop(0)
print(counties)
counties.insert(2, "Denver")
print(counties)
counties.append("Arapahoe")
print(counties)

counties_dict = {"Arapahoe":422829}
print (counties_dict)