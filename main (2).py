#Implement a recursive function  to calculate  the factorial  number 

def fact_rec (n):
  if n==0 or n==1:
    return  1
  else:
    return  n*fact_rec (n-1)
number =int(input ("Enter  the value:"))
rec=fact_rec (number )
print("They factorial of {}is {}".format(number,rec))
