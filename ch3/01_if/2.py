#블록내의 문장은 들여쓰기를 지켜줘야 한다.
#들여쓰기는 탭 / 스페이스 중 택1, 혼합해서 사용X
money = 1
if money:
    print("택시를")
 print("타고")
     print("가자") # Error, 들여쓰기 깊이에 의한 오류
else:
    print("걸어")
 print("가라") # Error, 탭, 스페이스를 혼합해 사용한 경우
