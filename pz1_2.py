n = int(input())
if(n <= 9):
  Str = "" 
  for i in range(n):
    i+=1
    for j in range(i):
      j+=1
      Str+=str(j)
    print(Str)
    Str = ""
else:
  print("Input Error!")

