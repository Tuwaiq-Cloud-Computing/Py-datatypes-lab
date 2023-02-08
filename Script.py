from operator import index
#Qu 1 

FList=[1,2,3];
FList.append(4);
FList.remove(1);
FList.reverse();
FList.sort();
FList.insert(0, 10);
print(FList);
print(FList[-1]);
 


 # Qu 2 


people=["Ahmad", "Nasser", "Mohammed"];
Coma=", "
ListComma=Coma.join(people);
print(ListComma);


# Qu 3 
ParentDict=[ 
     {
    "name" : "Emil",
    "PhNumber" : 2004
  },
  {
    "name" : "Tobias",
    "PhNumber" : 2007
  },
  {
    "name" : "Linus",
    "PhNumber" : 2011
  } ];



ParentDict.append({ 
    "name" : "Tobias",
    "PhNumber" : 2007})


print(ParentDict);

ParentDict[0].pop("name");


ParentDict[3].update( { "PhNumber" : 2009 });
print(ParentDict);

if ParentDict[0].keys == "name":
    print("Correct");

else:
    print("Not Correct");



