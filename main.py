from bs4 import BeautifulSoup
import requests,openpyxl

# to store data in excel
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="Top Movies"
sheet.append(['Rank','Movie Name','Year','Rating'])
try:# use try and catch to avoid code crash
    response= requests.get("https://www.imdb.com/chart/top/")# store complete html content to response variable
    # to store complete website code using beautiful soup
    soup =BeautifulSoup(response.text,"html.parser")
    #print(soup)
    movies =soup.find('tbody',class_="lister-list").findAll('tr')
    for movie in movies:

      #print(movie)# to get first tr's complete data
      rank= movie.find('td',class_="titleColumn").getText(strip=True)# strip is true to avoid tags
      rank=rank.split('.')[0]# to get only the number(1.The Shawshank Redemption(1994))
      movie_name= movie.find('td',class_="titleColumn").a.text
      rate=movie.find('td',class_="ratingColumn").strong.text
      year=movie.find('td',class_="titleColumn").span.text.replace('(',"")
      year=year.replace(')',"")
      #print(rank,movie_name,year,rate)
      sheet.append([rank,movie_name,year,rate])# append data as list to excel
      #break-- to get only the first record
# fetched records from website """1 The Shawshank Redemption 9.2 1994--> all 250


except Exception as e:
   print(e)
excel.save("Top""Movies.xlsx")# to save
