'''주어진 정수가 짝수면 Even 홀수면 Odd를 출력하는 코드(12937)'''
def solution3():
    a = int(input())
    if a % 2 == 0 :
        answer = 'Even'
    else :
        answer = 'Odd'
    print(answer)

def solution3_1():
    a = int(input())
    result = 'Odd'
    if a % 2 == 0 :
        result = 'Even'
    print("계산 결과: {0}".format(result))

    
# flag가 true면 a+b를, false면 a-b를 return
def solution(a, b, flag):
    if flag:
        return a+b
    else:
        return a-b
