from functools import reduce

def add(x,y):
      print(x,y)
      return x+y

def Multi(x,y):
    print(x,y)
    return x*y

def Even(x):
    if x%2==0:
        return True
    else:
        return False

#Custom function for filter() built-in#    
def Custom_filter(Meth,my_list):
   list_r=[]
   for i in range(len(my_list)):
        if Meth(my_list[i])==True:
            list_r.append(my_list[i])
   return list_r

#Custom function for reduce() built-in#         
def Custom_reduce(Meth,my_list):
     
     Ad = Meth(my_list[0],my_list[1])
     for i in range(2,len(my_list)):
               Ad=Meth(Ad,my_list[i])
     return Ad
my_list =[2,4,5,6,7,8]

print("Reduce()  Built-in Function:-")
ln=reduce(add,my_list)     
print("Sum:- ",ln)
ln=reduce(Multi,my_list)     
print("Product:- ",ln)
print("Custom Reduce() like Function:-")
ln1=Custom_reduce(add,my_list)       
print("SUM:- ",ln1)
ln1=Custom_reduce(Multi,my_list)       
print("Product:-",ln1)
print("filter() Built-in Function")
list_f = list(filter(Even,my_list))
print("Even Numbers",list_f)
print("Custom filter() function")
list_cf= list(Custom_filter(Even,my_list))
print("Even Numbers",list_cf)

