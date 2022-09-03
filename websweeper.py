import requests
from bs4 import BeautifulSoup

def find_images(keyword, num):
    result = []
    count = 0;
    url = "https://www.google.com/search?q=" + keyword +"&hl=en&sxsrf=ALiCzsaBzWBDKTv0Y2uKDyoWDjkX-kT3Pg:1662163521825&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiPm5vSqff5AhUvVTABHdZ7CmsQ_AUoAXoECAIQAw&biw=200&bih=2372&dpr=0.75"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    boxes = soup.findAll("a")
    for box in boxes:
        images = box.findAll("div")
        for image in images:
            if image.find("img") != None:
                if count >= num:
                    return result
                else:
                    photo = image.find("img")
                    result.append(photo.get("src"))
                    count += 1