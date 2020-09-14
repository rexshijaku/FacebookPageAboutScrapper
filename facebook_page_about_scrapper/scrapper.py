import urllib.request
from bs4 import BeautifulSoup
from facebook_page_about_scrapper import globals
from facebook_page_about_scrapper import helpers

def getFacebookPageAbout(url):

    req = urllib.request.Request(
        helpers.getPageUrl(url),
        data=None,
        headers=globals.headers
    )

    response = dict()

    try:
        content = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(content, features="lxml")

        info = dict()
        info["is_verified"] = True if globals.verified_icon_src in content else False
        for key in globals.elem_info:
            elem = soup.findAll("img", {"src": globals.elem_info[key]})
            info[key] = helpers.getSingleValue(elem)

        response['success'] = True
        response['info'] = info
        return response
    except Exception as e:
        response['success'] = False
        response['message'] = e
        return response