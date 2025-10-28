def calculate_bmi(height,weight):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi = weight / (height**2)
    print(bmi)
    if(bmi>25.0):
        print("You are Over Weight")
    elif(bmi>=18.5):
        print("You are Normal Weight")
    else:
        print("You are Under Weight")

calculate_bmi(weight=57,height=1.73)