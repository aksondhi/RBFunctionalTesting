from robobrowser import RoboBrowser

print "Testing link titles and page titles"
browser = RoboBrowser(history=True, parser='html.parser')
browser.open('http://ames.craigslist.org/search/apa')
currentLevelLinks = browser.select('.result-title')

print len(currentLevelLinks), "Links Found on", browser.url

print "Checking link titles and page titles match"
for link in currentLevelLinks:
    browser.follow_link(link)
    if link.text != (browser.select('#titletextonly'))[0].text:
        print "Titles did not match on "+ link.href

print ""
print "Testing placeholder value"
browser.open('http://ames.craigslist.org/search/ccc')
search = browser.select('#query')[0]
if search['placeholder'] != 'search apartments / housing rentals':
    print "Incorrect placeholder. Actual: "+ search['placeholder'] + ". Expected: 'search apartments / housing rentals'"

print ""
print "Testing search results"
browser.open('http://ames.craigslist.org/search/sss')
# Find the form
upload_form = browser.get_form(class_='search-form')
upload_form['query'] = 'iPhone'
browser.submit_form(upload_form)
results = browser.select('.result-title')

for item in results:
    if 'iPhone' not in item.text:
        print "Expected: 'iPhone' Actual: '"+item.text+"'"