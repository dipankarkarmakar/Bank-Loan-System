def reverse(string):
    if len(string==0):
        return string
    else:
        return(string[1:])+string[0]

a=str(input("Enter String to be reversed: "))
print(reverse(a))
