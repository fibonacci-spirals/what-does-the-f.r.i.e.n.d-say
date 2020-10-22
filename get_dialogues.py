import mechanicalsoup
import sys
Url = 'http://www.livesinabox.com/friends/scripts.shtml'
browser = mechanicalsoup.StatefulBrowser()
browser.open(Url)
browser.get_url()
browser.get_current_page()
lists = browser.get_current_page().find_all('li')
name = sys.argv[1]
name_corpus = []
try:
    if name:
        for each in lists:
            browser.open('http://www.livesinabox.com/friends/' + each.find('a')['href'])
            val = browser.get_current_page().text.split('\n')
            i = 0
            while i < len(val):
                if name.title() + ':' in val[i]:
                    name_corpus.append(val[i][len(name) + 2:])
                    i = i + 1
                    while i < len(val):
                        if val[i] and ':' not in val[i] and val[i][0] != '(':
                            name_corpus[-1] += ' ' + val[i]
                            i += 1
                        else:
                            break
                else:
                    i += 1
except ValueError:
    print("give a god damnnn name!!!")
f = open('data/'+name.lower()+'_script.txt', 'w')
f.writelines(name_corpus)
f.close()
