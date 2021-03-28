# reverse = ""
# for i in s1:
#     reverse = i + reverse
#
# for i in range(len(s1)):
#     if s1[i] != ' ':
#         j = 0
#         count = 0
#         while j < len(s1) - 1:
#             if s1[i] == s1[j]:
#                 count = count + 1
#             j = j + 1
#         print(s1[i], count)

# s1 = "Hello World!"
# frequency = dict()
# for char in s1:
#     if char != ' ':
#         count = s1.count(char)
#         frequency[char] = count
#
# print(frequency)
str1 = "Emma-is-a-data-scientist"
subtring = str1.split("-")

print(subtring)
