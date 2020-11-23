sugar=input("enter your fasting sugar level:")
sugar=float(sugar)

if sugar<80:
    print("your sugar is low, go eat some candies")
elif sugar>100:
    print("your sugar is high,stop eating candies")
else:
    print("your sugar is normal, just sit back and relax")