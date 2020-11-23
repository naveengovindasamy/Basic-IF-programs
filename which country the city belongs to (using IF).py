India=["Chennai","Delhi","Banglore"]
Usa=["newyork","california","boston"]
Bangladesh=["Dhaka","rangpur"]

city=input("Enter a city name:")

if city in India:
    print("it is in India")
elif city in Usa:
    print("it is in Usa")
elif city in Bangladesh:
    print("it is in Bangladesh")
else:
    print("don't know which country the city belongs to")

