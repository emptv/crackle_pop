for number in range (1,101):
    if number % 5 ==0 and number % 3 == 0:
        print ("Crackle Pop")
    elif number % 5 == 0: 
        print ("Pop")
    elif number % 3 == 0:
        print ("Crackle")
    else:
        print (number) 