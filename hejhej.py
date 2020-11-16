save = float(input("jag vill spara i månaden:"))
time = int(input("under så många år:"))
intrest = int(input("ränta i %"))
balance = 0


balance = 0

for i in range (0,year):
    balance += save * 12
    balance += ((intrest / 100 +1))
    print("år {i} har du sparat {balance:1'2}kronor")



balance = float(input("Ditt startkapital: "))
save float(input("jag vill spara i månaden"))
year = int(input("under så många år:"))
intrest = int(input("ränta i %"))
balanceWithIntrest = balance