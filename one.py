import two
print("top level in two.py")
two.func()
if __name__=='__main__':
    print("two.py is being run directly")
else:
    print("two.py has been imported")