# [리스트 기본 생성 방법]
from collections import namedtuple
import sys
r1 = [1, 2, 3]          # 리스트를 생성하는 가장 일반적인 방법
r2 = []                 # 빈 리스트를 생성하는 방법
r3 = [1, 2, [3, 4]]     # 리스트가 포함된 리스트를 생성하는 방법

# [list함수를 호출해서 생성 하는 방법]

r4 = list('Hello')      # 문자열을 전달해서 리스트를 생성
r5 = list((5, 6, 7))    # 튜플을 전달해서 리스트를 생성
r6 = list(range(0, 5))  # 레인지를 전달해서 리스트를 생성

# [ 1,2,3,4,5 가 포함된 리스트에서 모든 값을 두 배씩 증가시킨 값을 지니는 리스트]

r1 = [1, 2, 3, 4, 5]
r2 = []
for i in r1:
    r2.append(i*2)

# [위 예제 리스트 컴프리헨션 적용]

r1 = [1, 2, 3, 4, 5]
r2 = [x*2 for x in r1]

# x*2 = 리스트를 채울 데이터(x*2)가 무엇인지
# for x in r1 = 앞의 데이터(x)에 관한 정보

# [예제]

r1 = [1, 2, 3, 4, 5]
r2 = [x+10 for x in r1]

# [조건필터]

r1 = [1, 2, 3, 4, 5]
r2 = []
for i in r1:
    if i % 2:
        r2.append(i*2)

r1 = [1, 2, 3, 4, 5]
r2 = [x*2 for x in r1 if x % 2]


# [중첩된 for 루프 형태의 리스트 컴프리헨션]

r1 = ['Black', 'White']
r2 = ['Red', 'Blue', 'Green']
r3 = [t+p for t in r1 for p in r2]  # 뒤에 나오는 for 루프의 경우 앞의 for 루프에 종속된 형태


# [예제 - 구구단]

r = [n*m for n in range(2, 10) for m in range(1, 10)]


# [이중 for문 조건필터 추가]

r = [n*m for n in range(2, 10) for m in range(1, 10) if (n*m) % 2]
print(r)

# iter 함수 예제
# [ 기본적인 for 루프 ]
# ds = [1, 2, 3, 4]
# for i in ds:
#     print(i, end=' ')

# [iterator 객체]

ds = [1, 2, 3, 4]
ir = iter(ds)           # iterator 객체를 얻는 방법
next(ir)                # iterator 객체를 통해 값을 하나 꺼내는 방법,
# >> 1                    # 첫 번째 값 반환
next(ir)
next(ir)
next(ir)

ds = [1, 2]
ir = iter(ds)
next(ir)
# >> 1
next(ir)
# >> 2
# next(ir)             마지막 값을 반환했기 때문에 StopIteration 예외 발생

ir = iter(ds)       # 다시 Iterator 객체 얻음
next(ir)
# >> 1
next(ir)
# >> 2

# Iterable 객체       iter 함수에 인자로 전달 가능한 객체
# Iterator 객체       iter 함수가 생성해서 반환하는 객체

# [기본 예제]
ds = [1, 2, 3]
ir = iter(ds)
next(ir)
# >> 1
next(ir)
# >> 2

# [실제 함수 호출 형태]

ds = [1, 2, 3]
ir = ds.__iter__()         # iter 함수 호출의 실제 모습
ir.__next__()               # next 함수 호출의 실제 모습
# >> 1
ir.__next__()
# >> 2


# [Iterable 객체 - 튜플]
td = ('one', 'two', 'three')
ir = iter(td)
next(ir)
# >> one

# [Iterable 객체 - 문자열]
s = "iteration"
ir = iter(s)
next(ir)
# >> 'i'

# [다른 확인 방법 - dir]
dir([1, 2])

# [다른 확인 방법 - hasattr 함수]
print(hasattr([1, 2], '__iter__'))
# 리스트에 __iter__함수가 있는지?


# [for루프와 iterable 객체]

# for i in [1, 2, 3]:
#     print(i, end='')

# ⬇️ For루프 동작원리

# ir = iter([1, 2, 3])
# while True:
#     try:
#         i = next(ir)
#         print(i, end=' ')
#     except StopIteration:
#         break


ir = iter([1, 2, 3])        # ir에 저장되는 것은 iterator 객체
# for i in ir:                # for 루프에 iterator 객체를 가져다 두었다.
# print(i, end=' ')

ir1 = iter([1, 2, 3])
ir2 = iter(ir1)
ir1 is ir2
# >> True
id(ir1)
# >> 140218604751632
id(ir2)
# >> 140218604751632


# [객체처럼 다뤄지는 함수 그리고 람다]

# [파이썬에서는 함수도 객체]


x = 3.0                 # 실수 3.0
type(x)                 # 실수는 float형 클래스의 객체임을 확인한다.
# >> <class 'float'>
x.is_integer()          # 소수점 이하에 값이 있는지 묻는 메소드 호출
# >> True


def func1(n):           # 매개변수가 있고 값을 반환하는 함수
    return n


def func2():            # 매개변수가 없고 값의 반환도 업슨 함수
    print('Hello')


type(func1)             # func1은 function 클래스의 객체이다.
# >> <class 'function'>
type(func2)             # func2는 function 클래스의 객체이다.
# >> <class 'function'>


def say1():
    print('Hello')


def say2():
    print('Hi~')


def caller(fct):
    fct()               # fct를 통해 전달된 함수를 호출


caller(say1)            # say1 함수를 caller에 전달
# >> Hello
caller(say2)            # say2 함수를 caller에 전달
# >> Hi~


def fct_fac(n):
    def exp(x):         # 함수 내에서 정의된, x의 n제곱을 반환하는 함수
        return x ** n
    return exp          # 위에서 정의한 함수 exp를 반환한다.


f2 = fct_fac(2)         # f2는 제곱을 계산해서 반환하는 함수를 참조한다.
f3 = fct_fac(3)         # f3는 세제곱을 계산해서 반환하는 함수를 참조한다.
f2(4)                   # 4의 제곱은?
# >> 16
f3(4)                   # 4의 세제곱은?
# >> 64


# [람다]

# 일반적인 함수
def show(s):
    print(s)


ref = show
ref('hi~')

# 람다식


def ref(s): return print(s)


ref('oh~')

# 매개변수가 둘 이상인 람다식의 정의


def f1(n1, n2): return n1+n2


f1(3, 4)
# >> 7

# 람다식에서 함수를 호출하는 경우


def f2(s): return len(s)


print(f2('simple'))
# >> 6


def fct_fac(n):
    return lambda x: x ** n


f2 = fct_fac(2)
f2(4)
# >> 16

# [map 함수]

# 기존 방식


def pow(n):
    return n ** 2        # n의 제곱 값을 계산해서 반환


st1 = [1, 2, 3]
st2 = [pow(st1[0]), pow(st1[1]), pow(st1[2])]  # 값을 일일히 넣어서 반환

# >> [1,4,9]

# map 함수 사용시

st2 = list(map(pow, st1))
# >> [1,4,9]

st = [1, 2, 3]
ir = map(pow, st)
for i in ir:            # ir 은 iterator 객체이므로 for 루프에 올 수 있음
    print(i, end=' ')   # iterator 객체는 iterable


def dbl(e):
    return e * 2


list(map(dbl, (1, 3, 4)))              # 튜플 (1,3,4)를 map에 전달
# >> [2,6,8]
list(map(dbl, 'hello'))             # 문자열 'hello'를 map에 전달
# >> ['hh', 'ee', 'll', 'll', 'oo']


# 인자가 2개 이상일 경우 map함수의 사용
def sum(n1, n2):
    return n1 + n2          # 인자가 2개 인 함수


st1 = [1, 2, 3]
st2 = [3, 2, 1]

st3 = list(map(sum, st1, st2))
# >> [4, 4, 4]

# 일반적인 슬라이싱 연산

st = [1, 2, 3, 4, 5, 6, 7, 8]
st[:]                           # 처음부터 끝까지 모든 값을 꺼내서 리스트 생성
# >> [1, 2, 3, 4, 5, 6, 7, 8]
st[::1]                         # 처음부터 끝까지 한 칸씩 뛰면서 값을 꺼내 리스트 생성
# >> [1, 2, 3, 4, 5, 6, 7, 8]
st[::2]                         # 처음부터 끝가지 두 칸씩 뛰면서 값을 꺼내 리스트 생성
# >> [1, 3, 5, 7]
st[::3]                         # 처음부터 끝까지 세 칸씩 뛰면서 값을 꺼내 리스트 생성
# >> [1, 4, 7]


# map 함수를 사용한 reverse

def rev(s):                 # 전달된 내용(s)의 순서를 뒤집어서 반환하는 함수
    return s[::-1]


st = ['one', 'two', ' three']
rst = list(map(rev, st))
# >> ['eno', 'owt', 'eerht']

# 람다식

rst = list(map(lambda x: x[::-1], st))  # 상위 예제보다 훨씬 간결해보이며,
# >> ['eno', 'owt', 'eerht']            # 별도의 함수를 정의하지 않아도 된다.


# [filter 함수]

def is_odd(n):
    return n % 2    # 홀수이면 True 반환


st = [1, 2, 3, 4, 5]
ost = list(filter(is_odd, st))
# >> [1, 3, 5]

# 람다식을 사용한 filter 이용

st1 = [1, 2, 3, 4, 5]
ost = list(filter(lambda x: x % 2, st))  # 홀수값만 필터
# >> [1, 3, 5]

st = list(range(1, 11))
fst = list(filter(lambda x: not(x % 3), st))  # 3의 배수만 반환
# >> [3, 6, 9]

st = list(range(1, 11))
fst = list(filter(lambda n: not(n % 3), map(lambda n: n**2, st)))
# >> [9, 36, 81]         map함수부분에서 제곱된 반환 값을 객체(iterable)로 받아,
#                        3의 배수가 아닌 것을 필터한 값을 반환


# [두 함수를 대신하는 리스트 컴프리 헨션]

# map과 filter를 대신하는 리스트 컴프리헨션

# map 예제
st1 = [1, 2, 3]
st2 = list(map(lambda n: n**2, st1))
# >> [1, 4, 9]

# map 예제 리스트 컴프리헨션
st1 = [1, 2, 3]
st2 = [n**2 for n in st1]
# >> [1, 4, 9]

# filter 예제
st = [1, 2, 3, 4, 5]
ost = list(filter(lambda n: n % 2, st))


# >> [1, 3, 5]

# filter 예제 리스트 컴프리헨션
st = [1, 2, 3, 4, 5]
ost = [n for n in st if n % 2]
# >> [1, 3, 5]

# map & filter 예제
st = list(range(1, 11))
fst = list(map(lambda n: n**2, filter(lambda n: n % 2, st)))
# >> [1, 9, 25, 49, 81]

# map & filter 예제 리스트 컴프리헨션
fst = [n**2 for n in st if n % 2]
# >> [1, 9, 25, 49, 81]

# 함수 기반 제너레이터 예


def gen_num():                  # 제너레이터 함수의 정의
    print('fist number')
    yield 1                     # yield가 하나라도 들어가면 제너레이터가 된다.
    print('second number')
    yield 2
    print('third number')
    yield 3


gen = gen_num()                 # 제너레이터 객체 생성
type(gen)
# >> <class 'generator'>
next(gen)
# >> first number
# >> 1
next(gen)
# >> second number
# >> 2

# 일반적인 예제


def pows(s):
    r = []
    for i in s:
        r.append(i ** 2)
    return r


st = pows([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in st:
    print(i, end=' ')
# >> 1 4 9 16 25 36 49 64 81
sys.getsizeof(st)
# >> 200

# 제너레이터 함수 사용시


def gpows(s):
    for i in s:
        yield i ** 2


st = gpows([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in st:
    print(i, end=' ')
# >> 1 4 9 16 25 36 49 64 81
sys.getsizeof(st)
# >> 128           메모리 공간을 적게 사용하는 것을 확인 할 수 있다.

# [yield from]

# [제너레이터 표현식]


def show_all(s):
    for i in s:
        print(i, end=' ')


st = [2 * i for i in range(1, 10)]
print(type(st))
show_all(st)
# >> 2 4 6 8 10 12 14 16 18

# 제너레이터 함수


def times2():               # 제너레이터 함수의 정의
    for i in range(1, 10):
        yield 2 * i


g = times2()                # 제너레이터 객체의 생성
show_all(g)
# >> 2 4 6 8 10 12 14 16 18

# 제너레이터 표현식
g = (2 * i for i in range(1, 10))
show_all(g)
# >> 2 4 6 8 10 12 14 16 18


def two():
    print('two')
    return 2


g = (two() * i for i in range(1, 10))
next(g)
# >> two
# >> 2
next(g)
# >> two
# 4


def get_nums():
    ns = [0, 1, 0, 1, 0, 1]
    for i in ns:
        yield i

# yield from 사용시


def get_nums():
    ns = [0, 1, 0, 1, 0, 1]
    yield from ns

# [제너레이터 함수 직접 전달]

# 비교를 위한 예제 - 제너레이터 표현식을 직접 전달


def show_all(s):
    for i in s:
        print(i, end='')


show_all((2*i for i in range(1, 10)))

# 제너레이터 함수 실행시
show_all(2*i for i in range(1, 10))


# [튜플 패킹과 언패킹]

# 튜플패킹

tri_one = (12, 15)      # 밑변 길이 12와 높이 길이 15를 묶어 놓은것
tri_two = 23, 12        # 튜플 패킹은 소괄호가 없어도 된다.
# >> (23, 12)

# 튜플 언패킹 / 단, 튜플 언패킹 진행시에는 저장된 값의 수와 이를 저장할 변수의 수가 일치해야한다.

tri_three = (12, 25)
bt, ht = tri_three      # 튜플 언패킹
# >> bt = 12 , ht = 25

# 언패킹시 둘 이상의 값을 리스트로 묶어서 하나의 변수에 저장

nums = (1, 2, 3, 4, 5)
n1, n2, *others = nums      # 둘 이상의 값을 리스트로 묶을 때 *를 사용한다.
# n1 = 1
# n2 = 2
# others = [3,4,5]          # 튜플이 아닌 리스트로 묶인다.

first, *others, last = nums
# first = 1
# others = [2,3,4]
# last = 5

# 언패킹은 리스트 대상으로도 동일하게 작동

nums = [1, 2, 3, 4, 5]
n1, n2, *others = nums      # 리스트도 언패킹 됨.
# n1 = 1
# n2 = 2
# others = [3, 4, 5]

# 함수 호출 및 반환 과정에서의 패킹과 언패킹


def ret_nums():
    return 1, 2, 3, 4, 5        # 튜플의 소괄호가 생략된 형태,


    # 즉 패킹되어 반환
nums = ret_nums()
# >> (1, 2, 3, 4, 5)

n, *others = ret_nums()         # 반환값이 언패킹 되어 변수들에 저장
# n = 1
# others = [2, 3, 4, 5]         # 리스트로 패킹된다는 점.

# 매개변수 선언


def show_nums(n1, n2, *others):         # 세 번째 이후의 값드은 튜플로 묶여 other에 전달
    print(n1, n2, others, sep=', ')


show_nums(1, 2, 3, 4)
# >> 1, 2, (3, 4)
show_nums(1, 2, 3, 4, 5)
# >> 1, 2, (3, 4, 5)


def sum(*nums):     # 전달되는 모든 값들을 하나의 튜플로 묶어서 nums에 저장
    s = 0
    for i in nums:
        s += i
    return s


sum(1, 2, 3)
# >> 6

# *의 함수호출시 사용


def show_man(name, age, height):
    print(name, age, height, sep=', ')


p = ('Yoon', 22, 180)
show_man(*p)            # p 에 담긴 값을 풀어서 각각의 매개변수에 전달
# >> Yoon, 22, 180

p = ['Park', 21, 177]   # 리스트도 가능하다.
show_man(*p)
# >> Park, 21, 177

# 튜플 안의 튜플 언패킹
t = (1, 2, (3, 4))  # 튜플 안의 튜플
a, b, (c, d) = t     # 튜플 안의 값의 구조와 동일한 형태로 변수를 선언
# a=1
# b=2
# c=3
# d=4

p = 'Hong', (32, 178), '010-1234-56xx', 'korea'  # 튜플의 소괄호 생략
na, (ag, he), ph, ad = p
# na = Hong
# ag = 32
# he = 178
# ph = 010-1234-56xx
# ad = korea

# 특정 값만 가져오기
na, (_, he), _, _ = p
# na = Hong
# he = 178

# [for 루프에서의 언패킹]

ps = [('Lee', 172), ('Jung', 182), ('Yoon', 179)]   # 리스트 안의 튜플
for n, h in ps:
    print(n, h, sep=', ')

# Lee, 172
# Jung, 182
# Yoon, 179

ps = (['Lee', 172], ['Jung', 182], ['Yoon', 179])   # 튜플에 담긴 리스트
for n, h in ps:
    print(n, h, sep=', ')

# Lee, 172
# Jung, 182
# Yoon, 179

# [네임드 튜플]

# 튜플의 패킹
tri_one = (12, 15)

# 네임드 튜플 생성
Tri = namedtuple('Triangle', ['bottom', 'height'])  # 네임드 튜플 클래스 만듬
t = Tri(3, 7)       # 네임드 튜플 객체 생성
print(t[0], t[1])
# 3 7
print(t.bottom, t.height)
# 3 7

# t[0] = 15

# 클래스의 이름과 변수의 이름을 동일하게 하는 것을 권장
Tri = namedtuple('Tri', ['bottom', 'height'])


# [네임드 튜플 언패킹]
t = Tri(12, 79)     # 네임드 튜플 객체 생성
# a, b = Tri          # 언패킹
print(a, b)
# 12 79

# [dict의 생성과 zip]
# dict의 다양한 생성방법
# 기본적인 방법
d = {'a': 1, 'b': 2, 'c': 3}

# dict함수와 리스트를 사용한 방법
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
# >> {'a': 1, 'b': 2, 'c': 3}

# 문자열의 경우 사용할 수 있는 방법
d = dict(a=1, b=2, c=3)
print(d)
# >> {'a': 1, 'b': 2, 'c': 3}

# 키는 키끼리 값은 값끼리 리스트에 묶어서 생성하는 방법
d = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(d)
# >> {'a': 1, 'b': 2, 'c': 3}
