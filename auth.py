import tweepy

consumer_key = 'ZCKxVxtKbfLWkWXrddfxLrJyy'
consumer_secret = '0GerNmp0HhjEAIqbM3HHvAEWYnqsJQm5UnoK7hX84sCuAK8MpL'
access_token = '1038690560817549313-28D19PamXBJpnQBKwHy5vhp1kp8Wh2'
access_secret = 'moRRmEzXTWMQIrT7dWlAy1tpiI9pxTPBjYAzghmAp7aZ4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

 #Construct the API instance
api = tweepy.API(auth) # create an API object