values = [1, 2, 3, 4, "sachin", 5]
print(values)
print(values[0])
print(values[-1])
print(values[2:4])
values.insert(5,"sharma")
print(values)
values.append("End value")
print(values)

#values.remove()

#Updating value
values[0]="First Value"
print(values)

del values[0]
print(values)

del values[-2]
print(values)


