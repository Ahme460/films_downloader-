import requests
from bs4 import BeautifulSoup

# إرسال طلب POST بمعلومات البحث
def correct_link (search_query):
    url = "https://we1mycima.space/category/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA/"
    payload = {"s": search_query}
    response = requests.post(url, data=payload)
    response.raise_for_status()  # التحقق من نجاح الطلب

    # تحليل صفحة البحث باستخدام BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # العثور على الروابط الصحيحة
    links_dr = []
    grid_items = soup.select(".Thumb--GridItem")
    for grid_item in grid_items:
        link = grid_item.find("a")
        if link:

            link_url = link["href"]
            links_dr.append(link_url)

    for link in links_dr:
        return link
    