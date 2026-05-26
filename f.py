#variables:-
name="Mishti"

#Datatypes:-
print(type(name))
u = 9
print(type(u))
lst=['name',12,True]
print(lst)  
print(lst:1) # To access list by index

#control flow :-
#1.if/elif/else
#2.for loop
#3.while loop

age=input("Enter age") #By default input is of type string in python , we do typecasting to change in another type of data
if age >= 18:
    print("adult")
elif age >=13:
    print("Teen")
else:
    print("Kid")

#Loops:-
#1.For loop
list=[1,2,3,4,5,6,7,78]
for element in list:
    print(element)#by default it leaves one line after every print
    print(element,end= ' ')# to basically give how to print in which format or give ending sequence
for indx,value in enumerate(list): #enumerate:-
  print(f'{indx}-{value}')

#2.While loop
count = 0
while count<3:
  print(f'attempt {count}')
  count+=1

#Functions:-
#Eg1:-
def funct_name(name):
   #body
   return name

funct_name(name)
#Eg2:-
def stats(nums,label="data"): #default arguments
   return{
      "label":label,
      avg:sum(nums)/len(nums),
      "min":min(nums),
      "max":max(nums)
   }
result = stats([12,23,54,56],label='scores')
print(result)
print(stats)