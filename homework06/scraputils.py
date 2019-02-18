import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    main = []
    not_main = []
    main_list = []

    news = news_table.findAll("tr", class_="athing")
    for i in news:
        new = i.findAll("td", class_="title")
        title = new[1].find("a", class_="storylink").text
        link = new[1].find("span", class_="sitestr")
        if link == None:
            link = "No link"
        else:
            link = link.text
        main.append([title, link])

    subtext = news_table.findAll("td", class_="subtext")
    for i in subtext:
        sub = i.findAll("a")
        points_text = i.find("span", class_="score").text
        points, _ = points_text.split(" ")
        points = int(points)
        author = sub[0].text
        comments = sub[5].text
        if comments == 'discuss':
            comments = 0
        not_main.append([comments, author, points])

    for i in range(len(main)):
        main_dict = {'author': not_main[i][1],
                     'comments': not_main[i][0],
                     'points': not_main[i][2],
                     'title': main[i][0],
                     'url': main[i][1]}
        main_list.append(main_dict)

    return main_list


def extract_next_page(parser):
    """ Extract next page URL """
    # PUT YOUR CODE HERE


def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news

