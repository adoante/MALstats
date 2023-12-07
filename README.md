# MAL Stats 

Data based on [Reddit Anime List](http://www.redditanimelist.net/users.php) 
and [My Anime List](https://myanimelist.net/)

Used [Jikan API: UNOFFICIAL MYANIMELIST API](https://kijan.moe)

I'm no data scientist buy are python api calls nice.

`MALStats.py` will sum all user stats based on the users in `mal_reddit_user_list.txt` into `data_counts.txt`. <br>
Users in `mal_reddit_user_list.txt` was web scraped using `BeautifulSoup` from [Reddit Anime List](http://www.redditanimelist.net/users.php).<br>

If your wondering about the `time.sleep(0.5)` in `MALStats.py` it's because the API calls are limited to `3/sec`.<br>
I found that it would throw a `Bad Status: 429` when using that `3/sec` API calls. <br>
To avoid these I added the `time.sleep(0.5)`. <br>
