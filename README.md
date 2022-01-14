# twitter-giveaway-picker

This is a quick 'n dirty codebase I use to pick winners for my Twitter giveaways.
The giveaway instructions are that the 3 winners are randomly selected from those who liked and retweeted the giveaway tweet and follow me. The code saves the likes and retweets, and keeps randomly selecting winners, checking that the account follows me, until we have all three winners.

I used it for this giveaway:
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Have 2 surprises for my 20k milestone!<br><br>First: A BOOK GIVEAWAY🎁<br><br>I&#39;m autographing and giving 3 special color editions of <a href="https://twitter.com/abhi1thakur?ref_src=twsrc%5Etfw">@abhi1thakur</a>&#39;s book &quot;Approaching Almost Any Machine Learning Problem&quot; (which I helped review)<br><br>To enter: like, RT this tweet &amp; follow me by Jan 14th 10am PST <a href="https://t.co/Hi5VQuGepU">pic.twitter.com/Hi5VQuGepU</a></p>&mdash; Tanishq Mathew Abraham (@iScienceLuvr) <a href="https://twitter.com/iScienceLuvr/status/1479928224377303042?ref_src=twsrc%5Etfw">January 8, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## How it works
1. I tweet the giveaway tweet.
2. The ID of this tweet is put in [`twitter_save_likes.py`](twitter_save_likes.py) and [`twitter_save_retweets.py`](twitter_save_likes.py) as `tweet_id`.
3. I run `twitter_save.sh` during the duration of the giveaway which occassionally checks for new likes and retweets using the previously mentioned Python scripts.
4. At the end of the giveaway I run `twitter_pick_winners.py` which picks the winners.


# Acknowledgements
This code was mainly based on [Alexey Grigorev](https://github.com/alexeygrigorev)'s great [blog post](https://towardsdatascience.com/doing-giveaways-on-twitter-a5adc02d1ac0) but updated for the Twitter v2 API.
