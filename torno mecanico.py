import math
print("Escolha o que deseja calcular: digite R para raio ou A para ângulo: ")
escolher=input(())
if escolher[0] == 'R' or escolher[0] == 'r':
   print("Digite V para raio convexo ou X para raio concavo")
   raio=input(())
   if raio[0] == 'v' or raio[0] == 'V':
     r1=float(input("Digite o raio a executar: "))
     r2=float(input("Digite o raio do inserto: "))
     in1=float(input("Digite o incremento em X: "))
     sob=float(input("Digite o sobremetal em Z: "))
     in1=in1/2
     in2=in1
     r3=r1+r2
     ca=r3
     co=0
     x=0
     while in1 < r3:
          ca=r3-in1
          co=(math.pow(r3**2-ca**2,1/2))
          x=(co-r3)+sob
          print(f"Z = {x:.3f}")
          in1=in1+in2
   if raio[0] == 'x' or raio[0] == 'X':
      r1=float(input("Digite o raio a executar: "))
      r2=float(input("Digite o raio do inserto: "))
      in1=float(input("Digite o incremento em X: "))
      sob=float(input("Digite o sobremetal em Z: "))
      in1=in1/2
      in2=in1
      r3=r1-r2
      co=0
      while in1 < r3:
          co=(math.pow(r3**2-in1**2,1/2))
          print(f"Z= -{co:.3f}")
          in1=in1+in2
          
if escolher[0] == 'A' or escolher[0] == 'a':
   r1=float(input("Digite o ângulo a executar partindo da face(transversal): "))
   r2=float(input("Digite comprimento do ângulo em Z: "))
   in1=float(input("Digite o incremento em X: "))
   sob=float(input("Digite o sobremetal em Z: "))
   in1=in1/2
   r3=r2/(math.tan(r1*math.pi/180))
   co=0
   while r3 > 0:
      r3=(r3-in1)
      co=sob-(r3*(math.tan(r1*math.pi/180)))
      print(f"Z = {co:.3f}")
   
input()  
