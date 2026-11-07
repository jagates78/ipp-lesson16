import pprint
with open("jazz_greats_3.txt") as file:
    jazz_greats_nl = file.readlines()
jazz_greats = [great.rstrip("\n") for great in jazz_greats_nl]
pprint.pprint(jazz_greats[0:2], width = 100)
print("-"*25)
def non_us_jazz_greats(x):
    non_us = []
    for i in x:
        if "US" not in i:
            non_us.append(i)
    return non_us
pprint.pprint(non_us_jazz_greats(jazz_greats))