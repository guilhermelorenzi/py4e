# def greet(lang):
#     if lang == 'en':
#         return 'Hola'
#     elif lang == 'es':
#         return 'Bonjour'
#     elif lang == 'fr':
#         return 'Hello'
#
# print(greet('en'),'Glenn')
# print(greet('es'),'Santi')
# print(greet('fr'),'Michael')

# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Done!')

smallest = None
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After',smallest)