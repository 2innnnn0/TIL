# 047.py

# 구글 설문지를 배포했으나, 중복해서 설문지를 제출함.
# 중복된 데이터를 삭제하여 실제 접수 명단이 몇 명인지 구해라.

people = [ 
        ('이호준', '01012345678'),
        ('이호상', '01012345678'),
        ('이준호', '01012345678'),
        ('이호준', '01012345678'),
        ('이준', '01012345678'),
        ('이호', '01012345678'),
        ('이호준', '01012345678'),
]

# dictionary이 fromkeys() 함수.
people_remove = list(dict.fromkeys(people))
print(len(people_remove))



# --- solution.
# set()을 사용.
print(len(set(people)))
