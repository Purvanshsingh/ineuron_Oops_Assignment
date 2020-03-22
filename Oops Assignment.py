class A:
    def Test(self,a):
        print("Test of Class A ",a)
        super(A,self).Test(a,10)
class B:
    def Test(self,a,b):
        print("Test of Class B ",a,b)
class C(A,B):
    def test_of_AB(self):
        super(C,self).Test(5)
        ''' Or Can be Accessed with Class name directly'''
        #B.Test(self,5,10)
        
obj = C()
obj.test_of_AB()
#Verifing result
print(C.__mro__)
