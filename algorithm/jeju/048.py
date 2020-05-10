# 048.py

# 문자열이 주어지면 대문자,소문자를 바꿔서 출력하는 프로그램 만들기.
user_input = input()



result= ""
for i in range(len(user_input)):
    if user_input[i].isupper() == True:
        result += user_input[i].lower()
    else :
        result += user_input[i].upper()
print(result)



# ---- solution

s = input()
result = []
for i in s:
    if i.islower():
        result.append(i.upper())
    else:
        result.append(i.lower())
print(''.join(result))