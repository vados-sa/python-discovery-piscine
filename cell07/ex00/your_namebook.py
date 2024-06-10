def array_of_names(dictionary):
    full_names = []
    for firs_name, last_name in dictionary.items():
        full_names.append(f"{firs_name.capitalize()} {last_name.capitalize()}")
    return full_names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(array_of_names(persons))