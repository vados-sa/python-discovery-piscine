def famous_births(dict):
    sorted_dates = sorted(dict.items(), key=lambda x: x[1]["date_of_birth"])
    for name, info in sorted_dates:
        full_name = info["name"]
        b_year = info["date_of_birth"]
        print(f"{full_name} is a great scientist born in {b_year}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)