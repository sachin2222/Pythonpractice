file = open('test.txt')
# print(file.read())

# print(file.readline())

# line = file.readline()
#
# while line != '':
#     print(line)
#     line = file.readline()

print('*****************ReadLines**********')

list = file.readlines()

for i in list:
    print(i)
file.close()
