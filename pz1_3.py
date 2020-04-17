def Move(n, x, y):
  if y + x == 3: 
    tmp = 3
  if y + x == 4: 
    tmp = 2 
  if y + x == 5: 
    tmp = 1 
 
  if n > 0: 
    Move(n-1, x, tmp) 
    print (n, x, y) 
    Move(n-1, tmp, y) 
  return n,x,y 
 
Move(3, 1, 3)
