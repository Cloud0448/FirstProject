# n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return
def sol0626_7(n):
        answer = 0
    
    if n % 2 == 0:
        list = [i for i in range(2, n+1, 2)]
        for a in list:
            answer += a * a

    else:
        list = [i for i in range(1, n+1, 2)]
        for a in list:
            answer += a
            
    return answer
