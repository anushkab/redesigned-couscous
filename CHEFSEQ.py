T = int(input())

while T > 0:
   LS = int(input())
   numbers = list(map(int, input().split()))
   LF = int(input())
   sequence = list(map(int, input().split()))
   if sequence in numbers == True:
       print("Yes")
   else:
        print("No")

   T = T - 1