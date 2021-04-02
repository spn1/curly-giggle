# Always close the file. Either do it in \finally\ block or use \with\
try:
    left = open('.env-dev', mode='r', encoding='utf-8')

finally:
    left.close()

with open('write-to-me.txt', mode='w', encoding='utf-8') as file:
    file.write('Help Me I\'m\n')
    file.write('Trapped in a\n')
    file.write('Python Tutorial\n')

with open('write-to-me.txt', mode='r', encoding='utf-8') as file:
    first_four = file.read(4)
    print(first_four)
    print('Current file cursor position is: {}'.format(file.tell()))
    file.seek(0) # Send cursor back to beginning of file
    contents = file.read()
    print(contents)
    file.seek(0)

    # Read line by line
    for line in file:
        print(line, end='')
    
    file.seek(0)
    print(file.readline())

# Directories
import os

print(os.getcwd())
os.chdir('C:/Users/snnew/Development/curly-giggle')
print(os.getcwd())
print(os.listdir('{}/learning/python'.format(os.getcwd())))
print(dir(os))