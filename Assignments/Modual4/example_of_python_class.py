class studinfo:
    stid=101
    stnm="kavita"

    def myfunc(self):
        print("This is studinfo class")

    def getsum(self,a,b):
        print("sum is: ",a+b)

st=studinfo()
print("ID : ",st.stid)
print("Name : ",st.stnm)

st.myfunc()
st.getsum(56,78)