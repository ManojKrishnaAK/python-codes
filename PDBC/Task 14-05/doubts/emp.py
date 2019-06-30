class Emp:
    def setEmpDetails(self):
        self.eno=int(input("enter emp number:"))
        self.ename=input("enter emp name:")
        self.sal=float(input("enter emp salary:"))
        self.des=input("enter emp designation:")
    def dispEmpDet(self):
        print("employee details")
        print("emp number=",self.eno)
        print("emp name=",self.ename)
        print("emp sal=",self.sal)
        print("emp designation=",self.des)
eo=Emp()
eo.setEmpDetails()
eo.dispEmpDet()
