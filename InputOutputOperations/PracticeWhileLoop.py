''''Demo reading lines from text from a File '''''
print('\n***************Iterating over lines**********')
''''Reading text from a file with default encoding'''''
with open('hello.txt') as text_file:
    for line in text_file:
        print (line, end='')

print("\n****************Using read() method ***********")
''' Reading text from a file with "us" encoding'''
with open('hello.txt', encodings='us')as text_file:
    text = text_file.read()
print(text)

print('\n***************Using readlines( Method************')

          