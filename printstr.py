a = 'string'

# 문자열 a를 한줄로 n번씩 출력
# 방법 1 : While 사용
def sol1(a, n) :
    answer =''
    times = 1
    while times <= n :
        answer += a
        times += 1
    print(answer)

# 방법 2 : * 사용
def sol2(a, n) : 
    answer = a * n
    print(answer) 
    

# 문자열을 한 줄에 한 글자씩 나누어 출력하기
def sol3(str) :
    for s in str :
        print(s)
        

# 두 개의 문자열을 한글자씩 번갈아서 출력하기
def sol4(str1, str2) :
    answer = ''
    for i in range(len(str1)) :
        answer = answer+(str1[i]+str2[i])
    print(answer)


# 문자열 앞의 n글자를 출력하기
def sol5(my_string, n) :
    print(my_string[:n])


# 문자열을 대문자로 바꿔서 출력하기
def sol6(myString) :
    myString = 'aBcDefgH'
    print(myString.upper())
    

# 특정 문자열만 대문자로 바꾸기
def sol7(my_string, alp) :
    print(my_string.replace(alp, alp.upper()))   


# 문자열의 글자를 대소문자 바꿔서 출력하기
def sol1():
    str = 'aBcDeFg'
    answer = ''

    for s in str :
        if s.islower() :
            answer += s.upper()
        else :
            answer += s.lower()
    print(answer)
    
## 하지만 swapcase를 쓰면 한줄로 끝낼 수 있다
def sol2():
    str = 'aBcDeFg'
    print(str.swapcase())


# 문자열인 숫자의 각자리 합을 9로 나눈 나머지 구하기
def sol8(numbers):
    numbers = ''
    answer = 0

    for num in numbers :
        answer += int(num)

    return answer % 9
