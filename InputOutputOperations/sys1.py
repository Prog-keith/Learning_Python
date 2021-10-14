import sys
print("script name is : ",sys.argv[0])

if len(sys.argv)>1:
    print("There are ", len(sys.argv)-1, " arguments")
    for arg in sys.argv[1:]:
        print(arg) 

else:
    print("there are no arguments")        