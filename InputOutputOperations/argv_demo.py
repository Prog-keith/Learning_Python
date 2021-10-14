'''Accept command line arguments to the module'''

program = 'agrv_demo.py'
source = 'default.src'
dest = 'default.dst'

def show_config():
    print('Here is the currant configuration : ')
    print('Program : %s' % program)
    print('Source : %s' % source)
    print('Destination : &s' % dest)

    if __name__ == '__main__' :
        import sys
        print('here is sys.argv : %s ' % sys.argv)
        if len(sys.argv) > 2: #Two or more arguments passed
            program, source, dest = sys.argv[:3]
        elif len(sys.argv) > 1: #Only one argument passed
            program, source = sys.argv[:2] 
        else: #No arguments passed
            program = sys.argv[0]
    show_config()    
