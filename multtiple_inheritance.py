""" this is the first time i am writting my  documentation
So this program consists of inheritance method resolution order"""


class A1:
    def who_am_i(self):
        print("I am a A1")


class A2:
    def who_am_i(self):
        print("I am a A2")


class A3:
    def who_am_i(self):
        print("I am a A3")


class B(A1, A2):
    # def who_am_i(self):
    # print("I am a B")
    pass


class C(A3):
    def who_am_i(self):
        print("I am a C")


class D(B, C):
    # def who_am_i(self):
    # print('I am a D')
    pass


d1 = D()
d1.who_am_i()  # i_am A1

"""Some lines have been made comment for testing"""
