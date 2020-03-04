import ListToDic

a = ["nome","idade","sexo"]
b = ["Alex","Maria","Joana"]
c = [25,30,18]
d = ["M","F","F"]

dic1 = ListToDic.CorrenpKey(a,b,c,d)
print(dic1)
dic2 = ListToDic.SimpleDic(b,c,d)
print(dic2)