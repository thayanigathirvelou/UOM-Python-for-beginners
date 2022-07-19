i = int(input())
j = 2
while (j <= (i/j)):
    if not(i%j): 
        print("not a prime")
        break
    j = j + 1 # fix the code (3)
if (j > i/j): 
    print ("prime")
