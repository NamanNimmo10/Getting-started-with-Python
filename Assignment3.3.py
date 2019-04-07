hrs = input('enter the number of hours!: ')
h = float(hrs)

rph = input('enter the rate per hour!: ')
r = float(rph)

if h <= 40:
    print(h*r)
else:
    print(float(40)*r + float(h-40)*float(1.5)*r)
