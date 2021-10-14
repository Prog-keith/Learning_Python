def main():
    infile = open('file.txt','r')
    outfile = open('newfile1.txt', 'w')


    for line in infile:
        print(line,file = outfile, end='')
        
    print('Completed wiriting to newfile txt')    

main()

