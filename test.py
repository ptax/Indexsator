import urllib2
import urlparse
import re
 
class Crawler:
    _source = ''
    _depth = 0
    _links = []
    _wp_entries = []
    _debug = False
 
    def __init__(self, source, depth):
        self._source = source
        self._depth = depth
        self._links = [] 
        self._wp_entries = []
     
    def get_childs(self, url, level):
        if (level <= self._depth):
            if self._debug : print 'Crawling ', url
            try:
                page = urllib2.urlopen(url)
 
                # Discard non html files
                page_info = '<span class="skimlinks-unlinked">page.info</span>'(A)['content-type']
                if not(re.search('text\/html', page_info)):
                    if self._debug: print 'Found a non-html file ', url, ' :', <span class="skimlinks-unlinked">page.info</span>()['content-type']
 
                else:
                    for line in page:
                        # Find every link in source code
                        if ((re.search('a href=', line) != None)):
                            # If several links in a line -->  Iterate through all
                            links_in_line = re.findall('a href="(.*?)"', line)
                            for link in links_in_line:
                                # For each link found
                                #   0 - Check the link its internal (regex source or a page in same dir)
                                #   1 - Create the new page (only if it's without source in link)
                                #   2 - Check it doesnt been crawled (check self._links)
                                #   3 - Add to the list (self._links)
                                #   4 - Crawl the new one according to the rules (match 'page' in this case)
                                new_link = ''
                                crawl_link = False
                                if (<span class="skimlinks-unlinked">re.match(self._source</span>, link)):
                                    # Subpage sharing source (source/sthing) -> use that link
                                    if self._debug: print 'Found internal link ', link
                                    new_link = link
                                    crawl_link = True
 
                                elif (<span class="skimlinks-unlinked">re.match('http</span>:\/\/', link)):
                                    # External link -> do nothing
                                    if self._debug: print 'Found external link ', link
 
                                elif (<span class="skimlinks-unlinked">re.match('\w|\_</span>|\.', link)):
                                    # Internal link -> construct full url
                                    if self._debug: print 'Found internal link', link
                                    new_link = urlparse.urljoin(url, link)
                                    crawl_link = True
 
                                else:
                                    # Weird link
                                    if self._debug: print  'Found weird link ', link
 
                                if ((<span class="skimlinks-unlinked">self._links.count(new_link</span>) == 0) & crawl_link):
                                    # Found a new link, store & crawl it
                                    self._links.append(new_link)
 
                                    # WP specific actions
                                    # Store only h2 links (meaning entries)
                                    # Just crawl whenever link contains 'page' 
                                    if(re.search('h2', line)): 
                                        if self._debug: print 'WP entry ', new_link
                                        self._wp_entries.append(new_link)
 
                                    level += 1
                                    if(re.search('page', new_link)): self.get_childs(new_link, level)
                                    level -= 1
 
            except urllib2.HTTPError as e:
                if self._debug: print 'Found error while crawling ', url, e
 
            except urllib2.URLError as e:
                if self._debug: print 'Found error while crawling ', url, e
        else:
            if self._debug: print 'Maximum depth level reached, skipping'
                 
    def show_childs(self):
        print len(self._links),' links were found, listing:'
        for link in self._links:
            print link
 
    def show_wp_entries(self):
        print len(self._wp_entries),' WP entries were found, listing:'
        for head in self._wp_entries:
            print head
 
 
# Create a new crawler with page and maximu depth level
crawler = Crawler('<span class="skimlinks-unlinked">http://hoyhabloyo.wordpress.com</span>/', 5)
 
# Get childs for that page (could have used defaults params in method)
crawler.get_childs('<span class="skimlinks-unlinked">http://hoyhabloyo.wordpress.com</span>/', 0)
 
# Show me what you found
crawler.show_wp_entries()