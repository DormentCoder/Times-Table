# Times Table by Dc117 Corp.

print('Times Table V1.00')
xtable = int(input("Enter the table to print? "))
xtable = int(xtable)
for i in range(1, 13):
    answer = xtable * i
    print (str(xtable) + ' x ' + str(i) + ' = ' + str(answer))