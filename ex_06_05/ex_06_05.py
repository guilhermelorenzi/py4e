# Exercise 5: Take the following Python code that stores a string:

# str = 'X-DSPAM-Confidence:0.8475'

#Use find and string slicing to extract the portion of the string after 
# the colon character and then use the float function to convert the 
# extracted string into a floating point number.

print('Exercise 6.5')


str = 'X-DSPAM-Confidence:0.8475'
print(str)

ipos = str.find(':')
print(ipos)

piece = str[ipos + 1:]
print(piece)

value = float(piece)
print(value)