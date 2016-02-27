# twitter goggles v1.1
see twitter as someone else sees it, by picking someone you follow at random and creating a list populated with everyone *they* follow. 

### installation
requirements: python 2.7x, tweepy, valid twitter API credentials

```pip install tweepy```

then you'll need to visit https://apps.twitter.com/ to create an application (if you don't have one already) and get your API credentials. here's a guide that explains how to do that: http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/

note the following information:

```Consumer Key```

```Consumer Secret```

```Access Token```

```Access Token Secret```

```Owner ID```

paste each of those (and your twitter handle) into its appropriate field in creds.txt, and you should be able to run the script.

### running the script
```python goggles.py```

### generating another list
edit goggles.py line 70 and change the name 'goggles' to a different name

### deleting a list
delete lists from inside twitter at https://twitter.com/yourname/lists

### release notes

v1.1
---
lists go up to 5,000 now (@hugovk)
list opens in browser when complete (@hugovk)
lists are now private by default
added user handle to creds.txt


v1.0
---
initial release