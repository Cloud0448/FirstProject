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


# 배열 안의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return
def solution(num_list):
    a = ''
    b = ''
        
    for num in num_list :
        if num % 2 == 1 :
            a += str(num)
        if num % 2 == 0 :
            b += str(num)

    return int(a)+int(b)


#  정수 리스트에서 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return
  def solution(num_list):
    odd = sum(num_list[0::2])
    even = sum(num_list[1::2])
    return max(odd, even)      


# 정수 start_num에서 end_num까지 1씩 감소하는 수들을 차례로 리스트에 담기
def solution(start_num, end_num):
    answer = [i for i in range(end_num, start_num+1)]
    return answer[::-1]

        
