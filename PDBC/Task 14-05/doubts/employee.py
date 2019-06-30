class emp:
    def __int__(self,eno,name,sal,dsg):
        self.eno=eno
        self.name=name
        self.sal=sal
        self.dsg=dsg
    def dispEmpData(self):
        print(self.eno,"\t",self.name,"\t",self.sal,"\t",self.dsg)
