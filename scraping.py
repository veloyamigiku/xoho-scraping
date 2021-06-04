from bs4 import BeautifulSoup


def scraping_now_playing(html):
  soup = BeautifulSoup(html, "html.parser")
  movies_item_list = soup.find_all(class_="movies-item")
  result = []
  for movies_item in movies_item_list:
    title = movies_item.find("h2").text
    img_url = movies_item.find(class_="movies-image-inner")["style"].replace(
        'background-image: url("', "").replace('");', "")
    result.append({
        "title": title,
        "img_url": img_url
    })
  return result


def scraping_coming_soon(html):
  soup = BeautifulSoup(html, "html.parser")
  movies_list = soup.find_all(class_="movies")
  result = []
  for movies in movies_list:
    mm_dd_day = movies.find("h3").text
    movies_item_list = movies.find_all(class_="movies-item")
    for movies_item in movies_item_list:
      title = movies_item.find("h4").text
      img_url = movies_item.find("span")["style"].replace(
          'background-image: url("', "").replace('");', "")
      result.append({
          "mm_dd_day": mm_dd_day,
          "title": title,
          "img_url": img_url
      })
  return result
