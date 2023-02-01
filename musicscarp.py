import requests
from bs4 import BeautifulSoup
from musicimdb import Musicimdb

url = "https://www.imdb.com/search/tizztle/?genres=music&languages=hi&sort=user_rating"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# html parser
# print(response.text)
# tags = soup.find_all("title")
# for tag in tags:
#     text = tag.text.strip()
# print(tag.text)
Names = []
years = []
Ratings = []
#Directors=[]
no_of_votes = []
Ranks = []
songs = []

Years = soup.find_all("span",   class_="lister-item-year text-muted unbold")
for i in Years:
    year = i.text.strip()
    newstring = ''.join([i for i in year if i.isdigit()])

    years.append(int(newstring))

print(years)


names = soup.find_all("div", class_="lister-item-content")
for name in names:
    nva = name.find("h3", class_="lister-item-header").a.text
    if nva.__contains__(','):
        news = nva.replace(",", "")
        nva = news

    Names.append(nva)

print(Names)

ratings = soup.find_all("div", class_="inline-block ratings-imdb-rating")
for rating in ratings:
    Ratings.append(float(rating.text.strip()))

print(Ratings)

ranks = soup.find_all("span", class_="lister-item-index unbold text-primary")
for rank in ranks:
    Rank = rank.text

    ranking = (Rank[-len(Rank):-1])
    Ranks.append(int(ranking))

print(Ranks)

# directors = soup.find_all("div", class_="lister-item-content")
# for director in directors:
#     nva = director.find("p", class_="").a
#     print(director.text)
# if ((nva == None )or (director.text.__contains__("Stars"))):
#     Directors.append("missing")
#     continue
#     dir=(nva.text)
#     (Directors.append(dir))
# print(Directors)
# print(Directors)


votes = soup.find_all("p", class_="sort-num_votes-visible")
for vote in votes:
    newtext = (vote.text).split('\n')
    Votes = (newtext[2])
    if Votes.__contains__(","):
        new_vote = Votes.replace(",", "")
        Votes = new_vote
    no_of_votes.append(int(Votes))
print(no_of_votes)

for idx in range(len(years)):
    object_music = Musicimdb(year=years[idx], name=Names[idx], rating=Ratings[idx], vote=no_of_votes[idx],
                             rank=Ranks[idx])

    songs.append(object_music)

file = open("mydata.csv", "w+")

for song in songs:
    file.write(song.to_csv())

print("thank you")
