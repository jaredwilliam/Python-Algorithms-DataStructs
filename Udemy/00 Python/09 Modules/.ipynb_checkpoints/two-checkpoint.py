# two.py

import one

print('Top level in two.py')

one.func()

if __name__ == '__main__':
    print('two.py is being run directly')
else: # normally you don't have an else statement here, but this is for clarity
    print('two.py has been imported')
    