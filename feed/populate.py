import os
import nltk

nltk.download('punkt')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vurb.settings')

import django

django.setup()
from feed.models import Article
from newspaper import Article as Art
import newspaper
import requests
from io import BytesIO
from colorthief import ColorThief

verge_source = newspaper.build('https://www.theverge.com/', memoize_articles=False)
builtsources = []

sources = ['https://www.theverge.com/', 'https://slate.com/', 'https://www.espn.com/']
url_list = []

for i in sources:
    builtsources.append(newspaper.build(i, memoize_articles=False))
for i in builtsources:
    for article in i.articles:
        print(article.url)
        if (article.url[:-9] not in url_list):
            url_list.append(article.url)


def brightness(rgb):
    return (rgb[0] * 299 + rgb[1] * 587 + rgb[2] * 114) / 1000


def light(rgb, x=140):
    return brightness(rgb) > x


for url in url_list:
    try:
        article = Art(url, language="en", keep_article_html=True)  # en for English
        article.download()
        article.parse()
        article.nlp()
        title = article.title
        keywords = ', '.join(article.keywords)
        article_html = article.article_html
        image = article.top_image
        source = article.source_url
        authors = ', '.join(article.authors)
        publish_date = article.publish_date
        summary = article.summary

        color_thief = ColorThief(BytesIO(requests.get(image).content))
        colors = color_thief.get_palette(color_count=6)
        dominant_color = color_thief.get_color(quality=1)
        contrast = 0
        if light(dominant_color):
            for i in colors:
                if (not light(i)):
                    contrast = i
                    break
            if contrast == 0:
                contrast = (0, 0, 0)

        else:
            for i in colors:
                if (light(i)):
                    contrast = i
                    break
            if contrast == 0:
                contrast = (255, 255, 255)

        dominant_color = str(dominant_color)[1:-1]
        contrast_color = str(contrast)[1:-1]
        article_url = url

        j = Article.objects.create(
        title=title, keywords=keywords, article_html=article_html, image_url=image, source=source, authors=authors,
        publish_date=publish_date, summary=summary, dominant_color=dominant_color, contrast_color=contrast_color, article_url=article_url
        )
        j.save()
    except:
        print('skipped')
