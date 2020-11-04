import requests
from lxml import etree
import pandas as pd
url = "https://ssr1.scrape.center/page/"

data = []

for i in range(1,11):
    res = requests.get(url+str(i))
    tree = etree.HTML(res.text)
    movie = tree.xpath("//div[@class = 'el-card item m-t is-hover-shadow']")
    movie = [etree.tostring(i,encoding='utf-8').strip().decode('utf-8') for i in movie]
    for j in range(len(movie)):
        movie_tree = etree.HTML(movie[j])
        img_urls = movie_tree.xpath("//img[@class='cover']/@src")
        movie_scores = movie_tree.xpath("//p[@class='score m-t-md m-b-n-sm']/text()")
        movie_scores = [i.strip() for i in movie_scores]
        movie_name = movie_tree.xpath("//h2[@class = 'm-b-sm']/text()")
        movie_country = movie_tree.xpath("//div[@class = 'p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16']/div[@class = 'm-v-sm info'][1]/span[1]/text()")
        movie_duration = movie_tree.xpath("//div[@class = 'p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16']/div[@class = 'm-v-sm info'][1]/span[3]/text()")
        movie_time = movie_tree.xpath("//div[@class = 'p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16']/div[@class = 'm-v-sm info'][2]/span[1]/text()")
        img_urls = img_urls[0] if img_urls else ""
        movie_scores = movie_scores[0] if movie_scores else ""
        movie_name = movie_name[0] if movie_name else ""
        movie_country = movie_country[0] if movie_country else ""
        movie_duration = movie_duration[0] if movie_duration else ""
        movie_time = movie_time[0] if movie_time else ""
        data.append({
            "img_url":img_urls,
            "movie_scores":movie_scores,
            "movie_name":movie_name,
            "movie_country":movie_country,
            "movie_duration":movie_duration,
            "movie_time":movie_time
            })
# print(data)
my_df = pd.DataFrame(data)
my_df.to_excel("file/ssr1.xlsx",index = True)

