'''
Label Encoder는 독립 변수가 아닌 종속 변수(라벨)에 대해 사용한다. 문자열이나 정수로된 라벨 값을  0  ~  𝐾−1 까지의 정수로 변환한다. 변환된 규칙은 classes_ 속성에서 확인할 수 있다. 예측 결과에 적용할 수 있도록 역변환을 위한 inverse_transform 메서드도 지원한다.
'''

# labelencoding example
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

le.fit([1,2,2,6]) # 1,2,6 종류로 학습
print(le.classes_) # 1,2,6순으로 0,1,2 로 인코딩 --> 이거 순서대로 안해도 괜찮나?
print(le.transform([1,1,2,6])) # 결과 보여줌
print(le.inverse_transform([0,0,1,2])) #반대로


from sklearn.preprocessing import LabelEncoder
le_A = LabelEncoder()
y = ['A', 'B', 'A', 'A', 'B', 'C', 'C', 'A', 'C', 'B']
le_A.fit(y)
le_A.classes_

# [task] 지역구를 label-encoding한 피쳐로 생성하기
le.fit(df['gu'].unique()) # 지역구 유니크한 값 학습.
print(le.classes_)
print(le.transform(['강남구','강동구','은평구'])) # 결과 보여줌
print(le.inverse_transform([0,1,2,3])) #반대로
