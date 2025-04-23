friends= ["balmond","aldous","belerick"]
classmates=["tigreal","kufra","franco"]

friends.pop(2)
print("who among your friends loves food?:", friends,"\n")

classmates.insert(0,"johnson")
classmates.append("oddete")
print("Name of your classmates:\n", classmates,"\n")

names =classmates + friends
print("So the students in Section E are the following:\n", names,"\n","\n")

names.sort()
print("Sorted Names:",names,"\n")

result = friends is classmates
print("Same ba akong classmates ug friends?:", result,"\n")

pwends=friends
print("How about the Oa na friends:?", friends is pwends,"\n")

classmates.clear()
friends.clear()
x= friends + classmates
print("Kinsay nabagsak sa ila?:",x)