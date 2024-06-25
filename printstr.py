a = 'string'

# 문자열 a를 n번씩 출력
# 방법 1 : While 사용
def solution1():
    answer =''
    n = 1
    while n <= 3:
        answer = answer + a
        n = n + 1
    print(answer)

# 방법 2 : * 사용
def solution2() : 
    answer = a*3
    print(answer) 


# 문자열 한글자씩 한줄에 출력하기
def solution3(str) :
    for s in str:
        print(s)
       

# 문자열 두개를 한글자씩 번갈아가면서 출력하기
def solution4(str1, str2) :
    answer = ''
    for i in range(len(str1)) :
        answer = answer+(str1[i]+str2[i])
    print(answer)


# 문자열의 앞의 n글자를 출력하기
def solution5() :
    my_string = 'hello world'
    n = 3
    
    print(my_string[:n])


# 문자열을 대문자로 바꿔서 출력하기
def solution6() :
    myString = 'aBcDefgH'
    
    print(myString.upper())
    

# 특정 문자열만 대문자로 바꾸기
def sol9() :
    my_string = 'programmers'
    alp = 'p'
    print(my_string.replace(alp, alp.upper()))   


# 문자열인 숫자의 각자리 합을 9로 나눈 나머지 구하기
def sol10():
    numbers = '123'
    answer = 0

    for num in numbers :
        answer += int(num)

    return answer % 9


