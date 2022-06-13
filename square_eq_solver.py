import math  
   
def findRoots(a, b, c):  
  
    dis_form = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis_form))  
  
    if dis_form > 0:  
        print(((-b + sqrt_val) / (2 * a),(-b - sqrt_val) / (2 * a)))  
  
    elif dis_form == 0:  
        print(-b / (2 * a))  
  
    else:  
        print("No Roots") 
    
a = int(input('Enter a:'))  
b = int(input('Enter b:'))  
c = int(input('Enter c:'))  
  
if a == 0:  
    print("Input correct quadratic equation")  
  
else:  
    findRoots(a, b, c)  