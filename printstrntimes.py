a = 'string'
   
def solution1():

    answer =''
    n = 1
    
    while n <= 3:
        answer = answer + a
        n = n + 1
    print(answer)
    

def solution2() : 
    answer = a*3
    print(answer) 


# 문자열 한글자씩 한줄에 출력하기
def solution3(str) :
    for s in str:
        print(s)

