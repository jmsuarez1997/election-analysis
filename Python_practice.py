print("hello World")

'creating arrays- methods of menipulating the list'
counties=["Arapahoe","Denver","Jefferson"]
print(counties[0])
print(len(counties))
print(counties[1:3])
counties.append("El Paso")
counties.insert(2,"El Paso")
print(counties)
counties.remove("El Paso")
print(counties)
counties.pop(-1)
print(counties)

'Creating tuples - tuples are like arrays but placements can not be changed'
counties_tuple=("Arapahoe","Denver","Jefferson")
print(len(counties_tuple))
print(counties_tuple[:-1])

'creating dictionaries'
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438
print(counties_dict)
print(counties_dict['Arapahoe'])
print(counties_dict.get("Denver"))
'lists of dictionaries'
voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data.insert(2,{"county":"El Paso","registered_voters":461149})
voting_data.pop("Arapahoe")
print(voting_data)