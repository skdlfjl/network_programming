'''
4. 2개의 복소수를 저장하는 MyComplex 클래스를 정의하고자 한다. 

클래스의 멤버 변수로
첫번째 복소수의 실수 부분을 나타내는 real_1과 허수 부분을 나타내는 imaginary_1,
두번째 복소수의 실수 부분을 나타내는 real_2과 허수 부분을 나타내는 imaginary_2를 가진다. 

지원하는 연산은 곱셈이다. 2개의 복소수 a=3-4i, b=-5+2i를 클래스에 저장하고,
a×b의 결과를 출력하는 프로그램을 작성하라. 

- 파이썬에 내장되어 있는 복소수 클래스 사용 불가
- 곱셈 연산을 클래스 내 메소드로 구현하고, 해당 메소드 내에서 결과를 출력하도록 함
- (a + bi) x (c + di) = ac – bd + (ad + bc)i
'''

class MyComplex:
    def __init__(self, a, b):
        self.real_1 = a.real
        self.imaginary_1 = a.imag
        self.real_2 = b.real
        self.imaginary_2 = b.imag
    
    def Complex(self):
        #(a + bi) x (c + di) = ac – bd + (ad + bc)i
        c = str(int(self.real_1 * self.real_2 - self.imaginary_1 * self.imaginary_2))
        c2 = str(int(self.real_1 * self.imaginary_2 + self.real_2 * self.imaginary_1)) + 'j'
        if '-' in c2:
            pass       
        else:
            c2 = '+' + c2
        com = c + c2
        return com

a=3-4j
b=-5+2j
com = MyComplex(a, b)
print(com.Complex())
