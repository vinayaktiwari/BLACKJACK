a = int(input("enter the no. 1st no."))
b = int(input("enter the 2nd  no."))
operation= input("""c = a+b
d = a-b
m = a*b
div = a/b""")
if operation == "c":
    print("the sum is {}".format(a+b))
elif operation == "d":
    print("the difference is {}".format(a-b))
elif operation == "m":
    print("the multiplication is {}".format(a*b))
elif operation == "div":
    print("the division is {}".format(a//b))
else:
    print("nothing")
    
    //added a comment
