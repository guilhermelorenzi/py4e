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

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)