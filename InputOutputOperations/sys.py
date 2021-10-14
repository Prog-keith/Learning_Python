import sys
print("script name is : ",sys.argv[0])

try:
   print("script argument passsed is ", sys.argv[1])

except:
    print("There are no more agrguments")
