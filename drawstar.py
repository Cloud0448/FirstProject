import time

def drawstar():
    print('*')

#1. 숫자형변수 선언
#2. 반복문 조건주기
#3. 별 찍기
#4. 반복문을 끝내는 조건 주기
    
def testwhile(times):
    num = 1
    while num <= times:
        drawstar()
        num = num + 1


#숙제1. 숫자 입력받아서 높이가 그 수만큼인 직각삼각형 별 찍기

def draw_right_triangle_1(times):
    
    num = 1
    while num <= times:
        print( '*' * num )
        num = num + 1
    
draw_right_triangle_1(5)
    
    
#숙제2. 숫자 입력받아서 높이가 그 수만큼인 정삼각형 별 찍기

#숙제3. 입력받은 숫자가 가장 긴 row의 별 개수인 마름모 별 찍기