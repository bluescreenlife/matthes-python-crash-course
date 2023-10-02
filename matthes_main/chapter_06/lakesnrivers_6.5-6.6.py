## 6.5 ------------------------------------------------------------------------
# rivers = {
#     "amazon" : "south america",
#     "congo" : "africa",
#     "yangtze" : "china",
#     "mississippi" : "north america",
#     "yenisei" : "russia"
# }

# for river, location in rivers.items():
#     print(f"The {river.title()} runs through {location.title()}")

# print("")

# for river in rivers: #reminder for self - default will access just the keys
#     print(river)

# print("")

# for location in rivers.values():
#     print(location)

## 6.6 ------------------------------------------------------------------------
favorite_languages = {"jen" : "python", "sarah" : "c", "edward" : "rust", "phil" : "python"}

poll_candidates = ["andrew", "jen", "marshall", "edward", "penelope"]

for candidate in poll_candidates:
    if candidate in favorite_languages:
        print(f"Thank you, {candidate.title()} for taking the poll.")
    else:
        print(f"{candidate.title()}, please consider taking the survey.")