import urllib.request
import bs4 as bs
import xml.etree.cElementTree as et
import re

url = "http://indianexpress.com/section/india/"

html_doc = urllib.request.urlopen(url)
soup = bs.BeautifulSoup(html_doc, 'html.parser')

tag_news = et.Element("news")

# Number of articles to store in the xml file
count = 30

for temp in soup.find_all('div', class_='snaps'):
    link = temp.a.get('href')
    article = urllib.request.urlopen(link)
    article = bs.BeautifulSoup(article, 'html.parser')

    xml_headline = article.h1.text.lstrip().rstrip()
    xml_description = article.h2.text.lstrip().rstrip()
    xml_content = ''
    xml_place = ''

    author = article.find('div', class_='editor').find('a')
    xml_author = author.text.lstrip().rstrip()

    content = article.find('div', attrs={"class": "full-details"}).findAll('p')
    for x in content:
        str = x.text
        if str.find('jQuery') > 0:
            break
        else:
            xml_content += str

    date = article.find('div', class_='editor').find('span')
    xml_date = date['content']

    place = article.find('div', class_='editor').text
    m = re.search('\|(.+?)\|', place)
    if m:
        xml_place = m.group(1).lstrip().rstrip()

    print("---------------------------------------- Article ----------------------------------------")
    print("Headline =", xml_headline)
    print("Description =", xml_description)
    print("Author =", xml_author)
    print("Content =", xml_content)
    print("Date Published =", xml_date)
    print("Place =", xml_place)
    print("-----------------------------------------------------------------------------------------")

    tag_article = et.SubElement(tag_news, "article")

    tag_headline = et.SubElement(tag_article, "headline")
    tag_headline.text = xml_headline

    tag_description = et.SubElement(tag_article, "description")
    tag_description.text = xml_description

    tag_author = et.SubElement(tag_article, "author")
    tag_author.text = xml_author

    tag_content = et.SubElement(tag_article, "content")
    tag_content.text = xml_content

    tag_date = et.SubElement(tag_article, "date")
    tag_date.text = xml_date

    tag_place = et.SubElement(tag_article, "place")
    tag_place.text = xml_place

    count = count - 1
    if count == 0:
        break

# et.dump(tag_news)
tree = et.ElementTree(tag_news)
tree.write("temp.xml")
