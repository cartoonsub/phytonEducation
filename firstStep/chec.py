# countBio = int(input())
# countIt = int(input())

# if (countBio >= countIt):
#     maxC = countBio
# else: maxC = countIt

# nod = 1;
# i = 1
# while (i <= maxC):
#     if (countBio % i == 0) and (countIt % i == 0):
#         nod = i
#     i += 1

# print(int((countBio * countIt) / nod))
# a = int(input())
# b = int(input())
# d = a
# while d%b:
#     d += a
# print(d)

# class A:
#     val = 1

#     def foo(self):
#         A.val += 2

#     def bar(self):
#         self.val += 1


# a = A()
# b = A()

# a.bar()
# a.foo()

# c = A()

# print(a.val)
# print(b.val)
# print(c.val)



# class Base:
#     def __init__(self):
#         self.val = 0

#     def add_one(self):
#         self.val += 1

#     def add_many(self, x):
#         for i in range(x):
#             self.add_one()

# class Derived(Base):
#     def add_one(self):
#         self.val += 10


# a = Derived()#0
# a.add_one()#1

# b = Derived()#0
# b.add_many(3)#3

# print(a.val)
# print(b.val)




# class A:
#    def foo(self):
#       print("A")

# class B(A):
#    pass

# class C(A):
# #    def foo(self):
#     #   print("C")
#     pass

# class D:
#    def foo(self):
#       print("D")

# class E(B, C, D):
#    pass

# E().foo()


class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, D):
    pass