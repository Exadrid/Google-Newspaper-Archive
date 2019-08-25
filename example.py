from google_newspaper_archive import *

url_list = gna("https://news.google.com/newspapers?nid=pk6FPx6l9xIC&dat=20060427&printsec=frontpage&hl=en")
for i in range(0, len(url_list)):
    print(url_list[i])
