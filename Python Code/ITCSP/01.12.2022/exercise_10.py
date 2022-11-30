# write a simple program for airport fast check in
# conditions = countries EU or USA, money between 100 and 1000, luggage less than or eq to 20 => pass


country = input("write your country \n")
money = input("write the amount of money you have (use numbers) \n")
luggageWeight = input("write how much your luggage weighs (use numbers \n")

if (country == "EU" or country == "USA") and (int(money) >= 100 and int(money) <= 1000) and (int(luggageWeight) <= 20):
    print("you may pass")
else:
    print("you cannot fast check in")
