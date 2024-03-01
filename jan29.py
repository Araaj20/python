# Add=lambda x:x+45
# result=Add(20)
# print(result)
# Add=lambda x,y:x+y
# result=Add(20,35)
# print(result)
Add = lambda x,y:x+y
print(Add(25,45))
def classroom(n):
    square=lambda x:x+n
    return square
demo=classroom(20)
print(demo(30))
def multiplier(n):
    multiply_by=lambda x:x*n
    return multiply_by
multiplier_by_5=multiplier(5)
print(multiplier_by_5(10))
print(multiplier_by_5(80))
