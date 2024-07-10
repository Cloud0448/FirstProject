# 문자열을 한글자씩 나눠서 각각의 요소로 이루어진 배열 만들기 

def sol1(str):
    answer = list(str)
    print(answer)

# 문자열을 배열의 하나의 요소로 담기

def sol2(str):
    answer = [str]
    print(answer)


# 문자열 my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열 구하기
    # 내 풀이
def sol0626_5(my_string, s, e):
    str_arr = list(my_string)

    a = str_arr[:s]
    b = list(reversed(str_arr[s:e+1]))
    c = str_arr[e+1:]

    answer = ''.join(a + b + c)
    print(answer)

    # 다른 사람 풀이 참고
def sol0626_6(my_string, s, e):
    answer = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    print(answer)


#문자열 뒤의 n글자 return
def solution(my_string, n):
    answer = my_string[-n:]
    return answer


# my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 
def solution(my_string, index_list):
    answer = ''
    
    for i in index_list :
        answer += my_string[i]
    
    return answer


# is_prefix가 my_string의 접두사라면 1, 아니면 0을 return
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix :
        return 1
    else:
        return 0  
## startswith 이라는 함수도 있음! return int(my_string.startswith(is_prefix)) 접미사는 endswith.



#두 정수 q, r과 문자열 code가 주어질 때, code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를 앞에서부터 순서대로 이어 붙인 문자열을 return
def solution(q, r, code):
    arr = [i for i in range(0,len(code))]
    answer = ''

    for i in arr :
        if i % q == r:
            answer += code[i]
    
    return answer

## 그런데 다른 사람의 풀이를 보니 이렇게도 된다...?! WHy..
def solution(q, r, code):
    return code[r::q]


# 문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return
def solution(my_string, indices):
    answer = ''
    for i in range(0,len(my_string)):
        if i not in indices:
            answer += my_string[i]
            
    return answer


# 문자열 안에서 중복된 글자들은 빼고 중복되지 않는 글자들만 남기기
def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
# >dict로 쓰는 방법도 있다는데?!
