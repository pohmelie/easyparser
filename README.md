## **Description**



This script is required to extract information using XPATH




## **How to install**

python setup.py install






## **How to use**


**Find your XPATH in Google Chrome:**

![Chrome XPATH](./images/ex1.png)

read more about XPATH - https://msdn.microsoft.com/en-us/library/ms256086(v=vs.110).aspx

**Example #1:**
Search title of all pages
```

import easyparser

xpath = "/html/head/title/text()"

if __name__ == "__main__":
    for title in easyparser.find_recursive("https://python.org", xpath):
        print("->", title)

```

**Example #2:**
Search images of all pages
```

import easyparser

xpath = "//img/@src"

if __name__ == "__main__":
    for img in easyparser.find_recursive("https://python.org", xpath):
        print("->", img)

```

**Example #3:**
Search for images on specific pages
```

import easyparser

#do not search on URL containing these words
ignore = ['#', 'blog', 'events'] 

#search on URL containing these words
accept = ['doc', 'downloads']

xpath = "//img/@src"

if __name__ == "__main__":
    for img in easyparser.find_recursive("https://python.org", xpath, ignore, accept):
        print("->", img)

```

