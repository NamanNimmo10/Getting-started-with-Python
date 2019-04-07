def computepay():
    h = int(input("hours"))
    r = float(input("rate"))
    if h > 40:
        return 40*r+ (h-40)*r*1.5
    else:
        return h*r
print (computepay())
