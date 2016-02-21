# twitter goggles
see twitter as someone else sees it, by picking someone you follow at random and creating a list populated with everyone they follow. 

### installation
requirements: python 2.7x, tweepy, json, valid twitter API credentials

```pip install tweepy```

```pip install json```

then you'll need to visit https://apps.twitter.com/ to get your API credentials. here's a good guide to doing that: http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/

note the following information, and fill in the corresponding fields of creds.txt:

```Consumer Key```

```Consumer Secret```

```Access Token```

```Access Token Secret```

```Owner ID```

paste all that into the appropriate field in creds.txt, and you should be able to run the script.

### running the script
```python goggles.py```

### generating another list
edit goggles.py line 65 and change the name 'goggles' to a different name

### deleting a list
delete lists from inside twitter at https://twitter.com/yourname/lists