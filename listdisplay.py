list = ["Dog", "Cat","Cow","Bird"]

result = ""

for i in range(len(list)):
    if i == len(list) - 1 and len(list) != 1:
        result += "and " + list[i]
    else:
        result += list[i] + ", "

print(result)