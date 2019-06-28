# Selenium Basics 
## Part 6 - Login to website.
Now we will finally interact with website using selenium.

First let's run our http server again:
```
python3 server.py
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('http-server', this)">Run http server</button>

Let's curl again on our website to see once again what is happening there.
```
curl http://http-server:8080/login
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run curl command</button>

As u may remember website returns login form. We can see there are multiple html tags, but we are only interested in "\<form\>\</form\>" for now. This is place user needs to insert his credentials. It is quite easy with Selenium to do that.



## Part 7 - Run Selenium
```
python3
from selenium import webdriver # import Selenium to Python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox') 
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-gpu')

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("http://http-server:8080/")
print(browser.page_source)
```

<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

As in previous lesson we navigate to that page and see form, there are some elements like login, password, and submit button fields. We want our scrapper to fill these and click sumbit button. To do this, we have to find them on webpage, to tell Selenium how to access them. This time we are lucky because these items have id's (id in html document is unique for whole website).

```
login = browser.find_element_by_id("login")
passw = browser.find_element_by_id("password")
button = browser.find_element_by_id("submit_button")
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

Now we have our elements in variables we can easily perform some operations on them.

Let's write login and password and then click submit button. To write something to text field on website we need to emulate sending keystrokes to do that we need to import them from Selenium library:

```
from selenium.webdriver.common.keys import Keys #import keys method
login.send_keys("little_cat") #write "little_cat" to that field
passw.send_keys("is_cute")
button.click() # click button
```

<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>

Let's see what happened:
```
print(browser.page_source)
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run code</button>
