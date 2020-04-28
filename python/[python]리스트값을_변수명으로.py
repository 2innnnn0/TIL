# 리스트에 있는 값을 변수명으로 치환해주기.
# https://stackoverflow.com/questions/19122345/to-convert-string-to-variable-name


x='buffalo'
exec("%s = %d" % (x,2))
print(buffalo)



# 아래는, 딕셔너리형태
# https://stackoverflow.com/questions/11118486/python-list-as-variable-name

# Applist = [
# ['Apple', 'red', 'circle'],
# ['Banana', 'yellow', 'abnormal'],
# ['Pear', 'green', 'abnormal']
# ]

variables = {}
for name, colour, shape in Applist:
    variables[name] = {"name": name, "colour": colour, "shape": shape}

print("Apple shape: " + variables["Apple"]["shape"])
