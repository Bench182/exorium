import mysql.connector

token = 'AUTHTOKEN'

color = (COLOR)

pixabaykey = 'pixabay api key'

e621key = 'apikey' # Your e621 api key (you need an account)
e621username = 'username' # Your e621 username (you need an account)
e621agent = 'examplegithubaccount/repo' # User agent, some way e621 can reach you, for example discord username#0000

nsfwexceptions = [channelid, channelid, channelid] # Add channel IDs here the bot will still send NSFW in, regardless of the NSFW setting

DBdata = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database name"
)
