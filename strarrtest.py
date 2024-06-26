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
def sol0626_5(my_string, s, e):
  
    a = my_string[:s]
    b = my_string[s:e+1][::-1]
    c = my_string[e+1:]
  
    answer = a+b+c
    print(answer)



