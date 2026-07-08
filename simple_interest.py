def simple_interest(p, n, r):
    return (p*n*r)/100

dataset = [
    {"customer": "A", "principle": 56000, "noofyears": 4, "rateofinterest": 9.8},
    {"customer": "Arr", "principle": 5600, "noofyears": 8, "rateofinterest": 9.8},
    {"customer": "Ae", "principle": 7000, "noofyears": 4, "rateofinterest": 9.8},
    {"customer": "rw", "principle": 5000, "noofyears": 6, "rateofinterest": 9.8},
    {"customer": "w", "principle": 5000, "noofyears": 4, "rateofinterest": 9.8},
    {"customer": "r", "principle": 5600, "noofyears": 4, "rateofinterest": 9.8},
    {"customer": "f", "principle": 560, "noofyears": 5, "rateofinterest": 9.8},
    {"customer": "b", "principle": 56000, "noofyears": 4, "rateofinterest": 9.8}
]

for i in dataset:
    si = simple_interest(i["principle"], i["noofyears"], i["rateofinterest"])
    # print(f"customer {i["customer"]}'s interest is: {si}")
    print("customer interest is ", si)
