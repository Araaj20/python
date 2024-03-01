# number = 1
# for row in range(1,4):
#     for column in range(1,4):
#         print(number,end=" ")
#         number = number+1
#         print()
# length = 25
# width = 0
# length/width
# try:
#     length = 10
#     width = 0
#     length/width
# except Exception:
#     print("Division by zero is invalid! kindlychange your input")
try:
    width = 0
    length/width
except Exception:
    print("Have caught a new error")
except NameError:
    print("Variable has to be used before defining it")
except ZeroDivisionError:
    print("Division by zero is invalid! kindlychange your input")
finally:
    print("Finally block excuted")