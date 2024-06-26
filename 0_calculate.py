''' 더하기, 빼기, 곱셈 함수 만들어서 계산 결과 print 하기 '''


def addNumber(a, b):
    return(a + b)
    
def subtractNumber(a, b):
    return(a - b)

def multiplyNumber(a, b):
    return(a * b)
    
def divideNumber(a, b):
    return(a / b)
    

print(addNumber(1, 2))


'''두 정수가 주어질 때 두 정수를 더하는 덧셈 계산식을 출력하는 코드(181947)'''
def solution1():
    a, b = map(int, input().strip().split(','))
    print('{0} + {1} = {2}'.format(a, b, a+b))
    
    
'''두 정수가 주어질 때 각각의 정수를 a, b에 할당해 출력하는 코드(181951)'''
def solution2():
    a, b = map(int, input().strip().split(','))
    print('a = {0}'.format(a))
    print('b = {0}'.format(b))