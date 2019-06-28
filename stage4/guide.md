# Selenium Scrapping JS
## Part 9 - Scrapping JS website
Let's leave our last example and see something else, some websites use javascript to make content dynamic or just to avoid scrapping. Selenium is perfect solution for that because it can handle JS as normal browser (since basically it is normal browser).

First let's run our http server again:
```
python3 server.py
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('http-server', this)">Run http server</button>

Let's curl again on our website but this time to subpage "/js" to see what we can find there.
```
curl http://http-server:8080/js
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run curl command</button>

Website returns some button. And div tag without content in it.
Let's run selenium again this time on "/js" subpage:

```
python3
from selenium import webdriver # import Selenium to Python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-gpu')

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("http://http-server:8080/js")
print(browser.page_source)
```

<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

As in previous lesson we have to tell selenium what object it has to operate on. To do that we have to find object on page. This time we will use find_elements_by_tag_name, this function returns list of elements since there may be more than one button/div/span etc. at the same on webpage.
```
button = browser.find_elements_by_tag_name("button")[0] #we now our button has id 0 because there is only one button on page.
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

Since we have button in variable we can now perform click to load additional content to website with js.
```
button.click()
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

Let's see what happened:
```
print(browser.page_source)
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

Can you see the difference? Yes! secret data was inserted into div element!

## Part 10 - Invoking js function
What if there was no button and a lot of weird actions had to be performed to access that data?
Sometimes it may be possible to just call js function we want to use. In above HTML source we could see that there was js function called jsLoad().
This function can be easily invoked from browser, with selenium without need to click button!
First let's reload page:
```
browser.get("http://http-server:8080/js") # refresh site to hide output
print(browser.page_source)
```

<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

Invoke js function:
```
browser.execute_script("jsLoad();")
print(browser.page_source)
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

In the end don't forget to close webdriver:

```
browser.quit()
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Close webdriver</button>

