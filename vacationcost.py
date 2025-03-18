#Write a program to calculate the total trip expenditure: Calculate the hotel cost per day Calculate the plane cost Price of the vehicle rented during the trip
def hotel_cost(night):
    return(150*night)
def plane_cost(city):
    if "newyork"==city:
        return 200
    elif "losangeles"==city:
        return 250
def total(night, city):
    return (hotel_cost(night)+plane_cost(city))
print(total(3, "newyork"))