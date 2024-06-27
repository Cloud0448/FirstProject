# 두 수의 연산값 비교해 더 큰 값 출력하기 (181938)
def solution(a, b):
    
    cal1 = int(str(a) + str(b))
    cal2 = 2 * a * b
    
    answer = cal1
    if cal1 < cal2 :
        answer = cal2
    print(answer)

##다른 사람 풀이를 보니 이렇게도 된다? 근데 비교하는 두 수 값이 같은 경우는 고려 안 한듯
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)
