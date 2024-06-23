'''두 정수가 주어질 때 덧셈 계산식을 출력하는 코드(181947)'''

def solution1():
    a, b = map(int, input().strip().split(','))
    print('{0} + {1} = {2}'.format(a, b, a+b))
    
    
'''두 정수가 주어질 때 값을 출력하는 코드(181951)'''

def solution2():
    a, b = map(int, input().strip().split(','))
    print('a = {0}'.format(a))
    print('b = {0}'.format(b))
    

'''주어진 정수가 짝수면 Even 홀수면 Odd를 반환하는 코드(12937)'''
def solution3():
    a = int(input())
    if a % 2 == 0 :
        return 'Even'
    else :
        return 'Odd'

def solution3_1():
    a = int(input())
    result = 'Odd'
    if a % 2 == 0 :
        result = 'Even'
    print("함수 결과:{0}".format(result))
    return result

print(solution3_1())
