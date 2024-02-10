class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return '{b} menu available from {s} to {e}'.format(b=self.name, s=self.start_time, e=self.end_time)

  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
     total_bill += self.items[item]
    print("Total Bill: {}".format(total_bill))

# Quantity Calculation
# Tax and Tip Calculation

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu("brunch", brunch_items, 1100, 1600)  
brunch.calculate_bill({"pancakes": 7.50, "home fries":4.50, "coffee": 1.50})

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu("early_bird", early_bird_items, 1500, 1800)  

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("dinner", dinner_items, 1700, 2300)  


kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids = Menu("kids", kids_items, 1100, 2100)  

# print(brunch)


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "Address: {}".format(self.address) 

  def available_menus(self, time):
    available_menus = []  
    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available_menus.append(menu)
    return available_menus
# TODO: Format menu.start_time, menu.end_time and time with the date module.

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    
flagship_store = Franchise('1232 West End Road', [brunch, kids])
new_installment = Franchise('12 East Mulberry Street', [dinner, kids, early_bird])
print(flagship_store.available_menus(1700))


basta = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

arespas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arespas_menu = Menu("Take a' Arepa", arespas_items, 1000, 2000)

arepas_place = Franchise('189 Fitzgerald Avenue', [arespas_menu])

arepa  = Business('Take a\' Arepa', [arepas_place])

print(arepa.franchises[0].menus[0])

