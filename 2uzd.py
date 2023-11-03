""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.
1)RSS?
2) plūsmu no google.lv



pip install feedparser

...pip upgrade...
"""
import feedparser

# URL uz RSS plūmu

rss_url='https://ltv.lsm.lv/rss?c=1'

# iegūstam RSS plūsmas datus un veicam analīzi...
kkk=feedparser.parse(rss_url)

# informēšana...
for entry in kkk.entries:
    print("Virsraksts:", entry.title)
    print("Saite:", entry.link)
    print("Publicēšanas datums:", entry.published)
    print("\n")

