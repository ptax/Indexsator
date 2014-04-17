
from urlparse import urlparse
def FilterUrl(url):
    uri = urlparse(url)
    if '//' in uri.path:
        return uri.path.replace('//','/')
    elif '///' in uri.path:
        return  uri.path.replace('///','/')
    elif '////' in uri.path:
        return  uri.path.replace('////','/')
    elif '.jpg' in uri.path:
        pass
    elif '.gif' in uri.path:
        pass
    elif '.pdf' in uri.path:
        pass
    elif '.png' in uri.path:
        pass
    elif '.doc' in uri.path:
        pass
    elif '.xls' in uri.path:
        pass
    else:
        return uri.path

if __name__ == '__main__':
    print FilterUrl("http://alternativ.com.ua/wp-content/uploads/2014/02//our-team.")
