string = input() 
filter = "h"
if(string.find(filter) == -1):
    print("There is no any " + filter)
else: print(string[0 : string.find(filter)] + string[(string.rfind(filter) + 1):len(string)]) 
 
