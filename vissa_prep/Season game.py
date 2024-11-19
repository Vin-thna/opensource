n=int(input())
if n in  range(3,6):
    print("Spring")
elif n in range(6,9):
    print("Summer")
elif n in range(9,12):
    print("Autumn")
elif n==12 or n==1 or n==2:
    print("Winter")
else:
    print("Invalid")
