road_consumption = int(input("Fogyasztás országúton literben :"))
urban_consumption = int(input("Fogyasztás városban literben :"))
country_road = int(input("Órszágúti szakasz hossza km-ben :"))
urban_road = int(input("Városi útszakasz hossza km-ben :"))
petrol = int(input("Benzin ára Ft-ban :"))

# Auto fogyasztása csak oda
auto = (road_consumption * country_road + urban_consumption * urban_road) / 100

# Auto fogyasztása oda-vissza
auto_return = 2 * auto

# A teljes út ára
total_cost = petrol * auto_return
print("A fogyasztás oda-vissza: ", auto_return, " liter")
print("Az utazás költsége: ", total_cost, " Forint")
