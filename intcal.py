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


# num이 n의 배수이면 1을, 배수가 아니면 0을 return
def solution(num, n):
    if num % n == 0:
        return 1
    else :
        return 0

# number가 n과 m의 공배수이면 1, 아니면 0을 return
def solution(number, n, m):
    if (number % n == 0) and (number % m ==0) :
        return 1
    else:
        return 0

