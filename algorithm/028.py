# 028.py
# 28번
user_input = input()

user_input
len(user_input)
user_input[0:2]
user_input[1:3]
.
.
user_input[4:6]


for i in range(len(user_input)):
    print(user_input[i:i+2])


for i in range(len(user_input)-1):
    print( user_input[i]+user_input[i+1] )

