class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass


print("mro of A class=",A.mro()) #  A O
print("mro of B class=",B.mro()) #  B O
print("mro of C class=",C.mro())#  C O
print("mro of X class=",X.mro())#  XABO
print("mro of Y class=",Y.mro())#  YBCO
print("mro of P class=",P.mro())#  




