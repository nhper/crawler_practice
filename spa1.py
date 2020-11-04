import requests
import pandas as pd
import json
ajax_url = "https://spa1.scrape.center/api/movie/?limit={}&offset={}"

res = requests.get(ajax_url.format(100,0))
res = json.loads(res.text)

my_df = pd.DataFrame(res["results"])
my_df.to_excel("file/spa1.xlsx",index = False)