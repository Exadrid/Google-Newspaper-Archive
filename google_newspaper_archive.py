from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ast


def gna(url):
    html = urlopen("%s" % url).read()
    soup = bs(html, features="html.parser")

    id = soup.findAll(attrs={"name": "id"})[0]['value']

    page_str = str(soup.findAll(attrs={"id": "jtp_form"})[0])
    page_loc = page_str.find('of ')
    num_page = int(page_str[page_loc + 3:page_loc + 6])

    pid_long_list = str(soup.findAll("script")[-1])
    pid_loc_start = pid_long_list.find("\"page\":")
    pid_loc_end = pid_long_list.find("\"prefix\":")

    pid_short_list = ast.literal_eval(pid_long_list[pid_loc_start + 7:pid_loc_end - 1])
    pid_list = []
    for i in range(0, num_page):
        pid_list.append(pid_short_list[i]['pid'].split(","))

    url_list = []
    for i in range(0, num_page):
        pid_construct = "%s%%2C%s" % (pid_list[i][0], pid_list[i][1])
        url_list.append("https://news.google.com/newspapers?id=%s&sjid=%s&pg=%s&img=1&hl=en&h=1000"
              % (id, id, pid_construct))

    return url_list


if __name__ == "__main__":
    import sys
    url_list = gna(sys.argv[1])
    for i in range(0, len(url_list)):
        print(url_list[i])

