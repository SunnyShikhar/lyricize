def get_lyrics(url):
    request = urllib2.Request(url)
    request.add_header("Authorization", "Bearer " + "your-client-access-token")
    request.add_header("User-Agent",
                       "curl/7.9.8 (i686-pc-linux-gnu) libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")
    page = urllib2.urlopen(request)
    soup = BeautifulSoup(page, "lxml")
    lyrics = soup.find("div", class_= "lyrics")
    return lyrics.text
