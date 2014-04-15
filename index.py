
from grab.spider import Spider, Task
import logging
import sys

class Walker(Spider):
    base_url = 'http://alternativ.com.ua/'
    initial_urls = [base_url]
    links  = [base_url]
    TempLevel = []




    Globalid  = 0
    TempIterapor = 0

    def GetId(self):
        return self.Globalid
    def GenId(self):
        self.TempIterapor += 1
        self.Globalid = self.TempIterapor


    def task_initial(self, grab, task):
        if grab.response.code == 200:
            return self.find_links(grab)
    def find_links(self, grab):
        links = grab.doc.select('//a')
        host = self.initial_urls[0]
        self.GenId()
        for iterLink,link in enumerate(links):
            try:
                myurl = link.attr('href')

                if myurl.startswith("/"):
                    myurl = host + myurl

                if not myurl.find(self.base_url) == -1:
                    if not myurl in self.links:
                        self.links.append(myurl)
                        self.add_task(Task('trip', url=myurl, priority=len(self.links),numurl  = self.GetId(), caontLinks=len(links) ))
            except:
                pass



    def task_trip(self, grab, task):

        print 'Nomer Partii: ' + str(task.numurl), 'Url: ' +  str(task.url), str(task.priority) + ' Kolichesvo linkov: ' + str(task.caontLinks)
        self.TempLevel.append({task.url:task.numurl})
        self.find_links(grab)

    def shutdown(self):
        print self.TempLevel


if __name__ == '__main__':
    #logger = logging.getLogger('grab.spider.pattern')

   # logging.basicConfig(level=logging.DEBUG)
    bot = Walker(thread_number=1)


    bot.run()