def parse_html_url(url):
    import requests
    from bs4 import BeautifulSoup
    return list(map(lambda e: e.text, BeautifulSoup(requests.get(url).text, 'html.parser').select('#block-menyuukhederi > ul > li:nth-child(2) > div > div > div.col-lg-9.col-md-12 > div > ul:nth-child(1)')))[0].split("\n")[1:-1]

if __name__ == "__main__":
    print(parse_html_url("https://ukd.edu.ua"))