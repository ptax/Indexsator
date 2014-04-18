
t = {'http://alternativ.com.ua/lechenie-alkogolizma/lecheniya-zhenskogo-alkogolizma': 1, 'http://alternativ.com.ua/ua/likuvannya-narcomanii/viklik-narcologa-do-domu': 5, 'http://alternativ.com.ua/lechenie-alkogolizma': 1, 'http://alternativ.com.ua/ua/rehab': 5, 'http://alternativ.com.ua/ua/': 5, 'http://alternativ.com.ua/ua/likuvannya-alkogolizmu': 5, 'http://alternativ.com.ua/lechenie-narkomanii': 1, 'http://alternativ.com.ua/o-tsentre': 1, 'http://alternativ.com.ua/ua/contact': 5, 'http://alternativ.com.ua/price': 1, 'http://alternativ.com.ua/lechenie-alkogolizma/lecheniya-domashnego-alkogolizma': 1, 'http://alternativ.com.ua/ua/pro-centr': 5, 'http://alternativ.com.ua/lechenie-alkogolizma/kodirovanie-ot-alkogolizma-kiev': 1, 'http://alternativ.com.ua/reabilitatsiya': 1, 'http://alternativ.com.ua/lechenie-narkomanii/vyzov-narkologa-na-dom': 1, 'http://alternativ.com.ua/ua/likuvannya-narcomanii': 5, 'http://alternativ.com.ua/ua/likuvannya-alkogolizmu/koduvannya-vid-alcogolizmu-kiev': 5, 'http://alternativ.com.ua/kontakty': 1, 'http://alternativ.com.ua/ua/price': 5}
t = sorted(t.items(), key=lambda x: x[1])
print t
def IterPageCout(Num):

    if Num == 1:
        return 1
    elif Num == 2:
        return 2
    elif Num == 3:
        return 3
    elif Num == 4:
        return 4
    elif Num > 2:
        ListLevelePage = []
        for minus in xrange(Num):
            ListLevelePage.append(minus)
        #NextLevel =  Num - minus + 1
        return ListLevelePage[-3]

print IterPageCout(5)
'''

for key in t:
    if key[1] == 1:
        print 'Lala'
    elif key[1] > 1:
        print '222'
'''
