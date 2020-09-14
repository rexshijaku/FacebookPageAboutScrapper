def getSingleValue(elem):
    info = dict()
    if len(elem) > 0:
        info['exists'] = True
        info['value']  = elem[0].findNext("div").getText()
    else:
        info['exists'] = False
    return info

def getPageUrl(raw):
    # if full url sent
    if 'facebook.com' in raw:
        raw = raw.strip()
        if raw.endswith('/'):
            raw = raw[:-1]
        if raw.startswith('https'):
            url = raw.replace("https://www.facebook", "https://m.facebook")
            url = url.replace("https://facebook", "https://m.facebook")
        else :
            url = raw.replace("http://www.facebook", "http://m.facebook")
            url = url.replace("http://facebook", "http://m.facebook")
    else : #if only username sent
        url = 'https://m.facebook.com/'+raw

    url += "/about/?ref=page_internal&mt_nav=0"
    print(url)
    return url