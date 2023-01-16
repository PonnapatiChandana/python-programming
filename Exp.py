import cmath
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
dis= b**2 - 4*a*c
ans_1=(-b+(((b**2)-(4*a*c))**(1/2)))/2*a
ans_2=(-b-(((b**2)-(4*a*c))**(1/2)))/2*a
if(dis>0):
   print("The roots are real and distinct")
   print("Root1=",ans_1)
   print("Root2=",ans_2)
elif(dis==0):
     print("The roots are real and equal")
     print("Root1=", ans_1)
     print("Root2=",ans_2)
else:
    print("The roots are imaginary")
    print("Root1=",ans_1)
    print("Root2=", ans_2)                


