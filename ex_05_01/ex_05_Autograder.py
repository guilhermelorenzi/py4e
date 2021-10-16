# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# num = 0
# tot = 0.0
# while True :
#     sval = input('Enter a number: ')
#     if sval == 'done' :
#         break
#     try:
#         fval = float(sval)
#     except:
#         print('Invalid input')
#         continue
#     # print(fval)
#     num = num + 1
#     tot = tot + fval

# print(tot,num,tot/num)



largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        intval = int(num)
    except:
        print('Invalid input')
        continue
    

    if largest == None :
        largest = intval
    elif intval > largest :
        largest = intval

    if smallest == None :
        smallest = intval
    elif smallest > intval :
        smallest = intval
   

print("Maximum is", largest)
print("Minimum is", smallest)