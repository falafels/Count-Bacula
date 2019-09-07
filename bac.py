#numDrinks = input("Hey name, how much did you drink today? Be honest, I gotchu")
#gender = input("Hey name, what's your gender?")
#hours = input("Hey name, how long has it been since you started drinking?")
#weight = input("Hey name, how much do you weigh? Don't lie!")

def BAC_calculation(numDrinks, gender, hours, weight):
    if gender == "male":
        bodwat = 0.58
    elif gender == "female":
        bodwat = 0.49
    else:
        bodwat = 0.535

#	a = 0.806*numDrinks*1.2
#	b = bodwat*weight
#	c = a/b
#	d = 0.017*hours
#	e = c - d
#	f = e*10

#	print(a)
#	print(b)
#	print(c)
#	print(d)
#	print(e)
#	print(f)

    EBAC = (((0.806*numDrinks*1.2)/(bodwat*weight)) - (.017*hours))*10.0
    print (EBAC)
    return EBAC
BAC_calculation(3, 'female', 3, 55)

a = 0.806*3*1.2
b = 0.49*55
c = a/b
d = 0.017*3
e = c - d
f = e*10
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)