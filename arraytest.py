str_test = "hello world"
arr_str = list(str_test)

#1. array에서 맨 앞글자 출력하기
def sol1() :
    print(arr_str[0])


#2. array에서 몇번째 글자부터 몇번째 글자까지 출력하기
# 끝 인덱스는 포함 안됨!
def sol2() :
    print(arr_str[0:5])
    

#3. array의 길이 알아내서 출력하기
def sol3() :
    print(len(arr_str))
    

#3. array의 길이가 짝수면 hello, 홀수면 world를 출력하기
def sol4() :
    if len(arr_str) % 2 == 0 :
        print(arr_str[:5])
    else :
        print(arr_str[6:])
        
        
#4. for문을 돌면서 array 안의 글자를 한줄씩 출력하기
def sol5() :
    for i in arr_str :
        print(i)
        
        
#5. array 마지막에 느낌표를 추가하기
def sol6() :
    arr_str.append('!')
    print(arr_str)



# 정수 리스트 num_list가 주어질 때, 
# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return

def sol7(num_list):
    if num_list[-1] > num_list[-2] :
        num_list.append(num_list[-1] - num_list[-2])
    else :
        num_list.append(num_list[-1] * 2)
    
    return num_list
    

# 문자열을 공백 기준으로 잘라서 배열에 담기
def sol8(my_string):
    answer = my_string.split(' ')
    return answer



# 특정 문자열만 대문자로 바꾸기

def sol9() :
    my_string = 'programmers'
    alp = 'p'
    print(my_string.replace(alp, alp.upper()))   
 


# start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 배열에 담아
def sol10() :
    start_num = 3
    end_num = 10
    
    answer = []
    
    for i in range(start_num, end_num+1):
        answer.append(i)
    
    print(answer)
    
sol10()