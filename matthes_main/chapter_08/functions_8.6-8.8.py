# def city_country(city, country):
#     print(f"{city} is the place to be in {country}.")

# city_country("Minneapolis", "USA")
# city_country("Barcelona", "Spain")
# city_country("Oslo", "Norway")

## ----------------------------------------------------------

def make_album(artist_name, album_title, track_num = None):

    release = {"Artist":artist_name, "Album":album_title, "Number of tracks":track_num}
        
    if track_num:
        print(f"Artist: {release['Artist']} | Album: {release['Album']} | No. of tracks: {release['Number of tracks']}", sep = "")
    else:
        print(f"Artist: {release['Artist']} | Album: {release['Album']}", sep = "")

user_input = True

while user_input:
    artist_name = input("Enter an artist name, or enter \"q\" to quit.\nArtist name: ")

    if artist_name == "q":
        break
    album_title = input("Enter an album title, or enter \"q\" to quit.\nAlbum title: ")
    if album_title == "q":
        break
    track_num = input("Enter a number of tracks, or enter \"q\" to quit.\nNo. of tracks: ")
    if track_num == "q":
        break

    make_album(artist_name, album_title, track_num)

    repeat = input("\nWould you like to enter another release? (Y/N) ")

    if repeat.lower() == "n":
        break