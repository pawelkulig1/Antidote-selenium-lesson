# Selenium Basics 
## Part 3 - Login to website.
Sometimes some resources that user want to scrap are hidden behind some login cookie session. It is hard then to scrap that kind of content with curl and conventional methods. Here selenium comes with help.

Let's assume that to get some data from webpage we have to login, if we are not logged in, webserver is going to redirect us automatically to login webpage.

First let's run our http server again:
```
python3 server.py
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('http-server', this)">Run http server</button>

First let's curl our webserver:
```
curl http://http-server:8080/login
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run curl command</button>

As can be seen website returns just login form, data that is behind login page cannot be accessed. With curl it is possible to overcome this problem but it is material for another tutorial :).



## Part 4 - Run Selenium
First thing we want to do is to run selenium to get to this webpage. We will use python to communicate with Selenium API.

To run Python:
```
python3 
```

<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Run python</button>

## Part 5 - Navigate to our webpage
Now we will navigate to webpage with Selenium and print website source, to check if everything works properly.

```
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
In above example we use Chromedriver as backend to Selenium [Read the docs].
There are some options that are passed to chromedriver to run it in proper mode (without GUI - since we are running it from terminal).
In the end it is important to close webdriver:

```
browser.quit()
```
<button type="button" class="btn btn-primary btn-sm" onclick="runSnippetInTab('selenium', this)">Close webdriver</button>
