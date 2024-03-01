# favfruits = ["Apple","Mango","berry","orange"]
# print(favfruits)
# for demo in favfruits:
#     print(demo)
#     for number in range(1,10):
#         print(number)
        # temp = 77
        # while temp >= 68 and temp <=77:
        #     print("room temp is maintened at {} deg F".format(temp))
        #     temp = temp - 1
        #     while True:
        #         print("This loop runs forever")
        #         number = 1
        #         for row in range(1,4):
        #             for column in range(1,4):
        #                 print(number,end='')
        #                 number = number + 1
        #                 print()
for number in range (1,11):
    if number == 5:
        break
    else:
        print(number)
else:
     print("all the numbers were printe without breaking")