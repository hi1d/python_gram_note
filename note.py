# [리스트 기본 생성 방법]
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
