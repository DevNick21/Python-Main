travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country, visit_times, list_of_states):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visit_times
    new_country["cities"] = list_of_states
    travel_log.append(new_country)


# 🚨 Do not change the code below
statesdb = []
more = True
countrydb = input("What country? ")
visitdb = input("How many vists? ")
while more == True:
    statesdb.append(input("What state? "))
    more_states = (input("Do you want to add more states? Yes or No ").lower())
    if more_states == "no":
        more = False

add_new_country(country=countrydb, visit_times=visitdb,
                list_of_states=statesdb)
print(travel_log)
