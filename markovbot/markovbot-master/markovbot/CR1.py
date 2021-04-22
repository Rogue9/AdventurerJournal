import time
from markovbot import MarkovBot
clockwork_raven=MarkovBot()

# Get the current directory's path
book = open("Lewis.txt")
clockwork_raven.read(book.name)
my_first_text = clockwork_raven.generate_text(30, seedword=["turtle", "dormouse", "rabbit", "jabberwock", "Alice"])
print(my_first_text)

TWITTER_API="7HJDlEmhPVjygVeGrvwaWzs2S"
TWITTER_API_SECRET = "2NVXClmnix8shGbE1HO8uAgO5XWwfrS7fgOlAdVEHKp698W7kQ"
BEARER = "AAAAAAAAAAAAAAAAAAAAAMbcNwEAAAAAyWO4Ms5gpSCi371Qm3YpcOKqzGc%3DfaoL8OsnEFmkAKvJZ6P7CY63DQeehSFruHBoaXme6jmOgcZI4d"
ACCESS_TOKEN = "932469309783322624-IvRsrsSe8VgpwX4J0hcJAoUhs1J8ULU"
ACCESS_TOKEN_SECRET = "HzRM0vnu8fr1Wr72xJGfBTBRL5lU4BkYu5mAN7xJqAVB2"

# Set some parameters for your bot
targetstring = 'MarryMeFreud'
keywords = ['marriage', 'ring', 'flowers', 'children', 'religion']
prefix = None
suffix = '#FreudSaysIDo'
maxconvdepth = None

targetstring = '#Alice'
keywords = ['head', 'dormouse', 'flowers', 'tea', 'cheshire']
prefix = None
suffix = '#FeedYourHead'
maxconvdepth = 2
while 1==1:
    clockwork_raven.twitter_login(cons_key=TWITTER_API,cons_secret=TWITTER_API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    clockwork_raven.twitter_tweeting_start(days=0, hours=0, minutes=5, keywords=keywords, prefix=None, suffix="#FeedYourHead")
    # clockwork_raven.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix,
    #                                  maxconvdepth=maxconvdepth)

    time.sleep(60)
    # clockwork_raven.twitter_autoreply_start(targetstring, keywords=keywords, prefix=prefix, suffix=suffix,
    #                                  maxconvdepth=maxconvdepth)
    time.sleep(60)
