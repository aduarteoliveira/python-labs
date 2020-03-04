#Função ListToDic¶
#A função ListToDic retorna um dicionário a partir de duas ou mais listas informadas.
#
#ListToDic.<Module>(KeyList,OtherLists) where:
#
#- KeyList é o nome da lista de chaves do dicionário
#- OtherLists demais listas de valores.
#Exemplo:  
#
#import ListToDic
#a = ["nome","idade","sexo"]
#b = ["Alex","Maria","Joana"]
#c = [25,30,18]
#d = ["M","F","F"]
#
#
#dic1 = ListToDic.CorrenpKey(a,b,c,d)
#print(dic1)
#
#Return:
#{'nome': ['Alex', 'Maria', 'Joana'], 'idade': [25, 30, 18], 'sexo': ['M', 'F', 'F']}
#
#dic2 = ListToDic.SimpleDic(b,c,d)
#print(dic2)
#
#Return:
#{'Alex': [25, 'M'], 'Maria': [30, 'F'], 'Joana': [18, 'F']}
import locale

def SimpleDic(a,*args):

    dic = {}
    key = ''
    for m in a:
        args = list(args)
        for p in args:
            #print("P:",p)
            key = m
            dic[key] = []
            for arg in args:
                dic[key].append(arg[a.index(m)])
            break
    return(dic)

def CorrenpKey(a,*args):

    dic = {}
    key = ''
    cont_a = len(a)
    cont_args = len(args)
    vals = None
    if cont_a > cont_args:
        print("There are not enough arguments to create a dictionary with the provided lists. Verify the relation keys/values provided in the arguments. For help, use ListToDic.help().")
    else:
        for m in a:
            args = list(args)
            for p in args:
               tmp = args.index(p)
               vals = args[args.index(p)]
               if tmp == a.index(m):
                    key = m
                    dic[key] = []
                    n = 0
                    while n < len(vals):
                        #dic[key] = vals[n]
                        dic[key].append(vals[n])
                        n = n+1
        return(dic)
