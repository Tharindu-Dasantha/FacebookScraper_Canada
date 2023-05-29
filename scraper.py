from bs4 import BeautifulSoup
import requests


# scraper
def scraper_Yellow_page(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "lxml")
    # getting the name of the page
    title = soup.find("h1", class_="merchantInfo-title merchant__title").text
    print("Scraping the page of " + title)
    # getting the facebook link
    SocialMedia = soup.find(class_="merchant__useful_item mlr__item--website")
    sociallist = SocialMedia.find("li")
    try:
        tmp = sociallist.find("a").get("href")
        link = "https://www.yellowpages.ca" + tmp 
        print(link)
    except:
        link = False
        print("Could not find a facebook page of " + title)


def scraper_FB(url):
    from facebook_scraper import get_profile
    get_profile("zuck") # Or get_profile("zuck", cookies="cookies.txt")
    # infor_tab = soup.find(class_="x1yztbdb")
    # print(infor_tab)
    # email_tab = soup.find(class_="x78zum5 xdt5ytf xz62fqu x16ldp7u")
    # print(email_tab)
    # email_tab_link = email_tab.find(class_="xu06os2 x1ok221b")
    # link = email_tab_link.find("span", class_="x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u x1yc453h").text
    # print(link)
    
    
if __name__ == "__main__":
    url = "https://www.yellowpages.ca/gourl/7424b60872d44e3bef2867ce4948eb681fc206e7?redirect=https%3A%2F%2Fwww.facebook.com%2Fpages%2FBread-and-Rose-Bakery-Cafe%2F131937646827582"
    scraper_FB(url)