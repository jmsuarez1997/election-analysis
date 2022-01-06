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
<<<<<<< HEAD

print(voting_data)

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")


for county in counties_dict:
    print(county )


for voters in counties_dict.values():
    print(voters)

for county, voters in counties_dict.items():
    print(county,'county has', voters, 'registerd voters.')

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:

     print(county_dict['registered_voters'])

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registerd voters.")

for registered_voters, county in voting_data:
    print(f"{county} sdafshdkfjahsd {registered_voters} registered voters")

=======
voting_data.pop("Arapahoe")
print(voting_data)
>>>>>>> 7aaf67b2b365a4e367e65ccbb31ee115b26afd74
