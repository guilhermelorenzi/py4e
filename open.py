# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:',count)

# fhand = open('mbox.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        count = count + 1
print('There were', count, 'from lines in', fname)