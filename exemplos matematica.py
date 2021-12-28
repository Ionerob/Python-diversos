import math
a= float(input())
b= float(input())
c= float(input())
d= float(input())

print(f"i) {round(((a**2+3*b)/c)+d,4)}")
print (f"ii) {round(math.log(a,10)+(math.pow(math.e,-b/c))-d**2/math.pi,4)}")
print (f"iii) {round(((math.pow(a**2,1/3))*(math.pow(b,1/3))+(c*d))/(a+b+c+d),4)}")
print (f"iv) {round(((a+b)*(c+d))/(a*b*c*d),4)}")
print (f"v) {round(((a**2+b**2)/(c*d))-((c**2+d**2)/(a*b)),4)}")
print (f"vi) {round((a+b+c+d)**2,4)}")
print (f"vii) {round(a**2+b**2+c**2+d**2,4)}")
print (f"viii) {round(math.pow(a*b*c*d,1/3),4)}")