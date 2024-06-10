def find_the_redheads(dict):
    redheads = []
    for name, hair in dict.items():
        if hair == "red":
            redheads.append(f"{name}")
    return redheads

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red",
"gina": "red"
}
print(find_the_redheads(dupont_family))