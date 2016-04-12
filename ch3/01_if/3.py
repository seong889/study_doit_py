#if, else if, else는 C와 비슷한 방식으로 사용
#단, else if는 파이썬에서 elif로 쓴다.

score = 90
if score == 100:
    print("A")
elif score > 90:
    print("B")
elif score > 80:
    print("C")
elif score > 70:
    print("D")
else:
    print("F")
