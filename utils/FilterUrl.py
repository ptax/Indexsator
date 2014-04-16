

def FilterUrl(url):

    if '.jpg' in url:
        pass
    elif '.gif' in url:
        pass

    else:
        return url

if __name__ == '__main__':
    print FilterUrl("http://alternativ.com.ua/wp-content/uploads/2014/02/our-team02")
