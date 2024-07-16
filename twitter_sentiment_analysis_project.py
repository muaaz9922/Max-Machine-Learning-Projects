{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"name":"python","version":"3.10.13","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kaggle":{"accelerator":"none","dataSources":[{"sourceId":1375,"sourceType":"datasetVersion","datasetId":740}],"dockerImageVersionId":30673,"isInternetEnabled":false,"language":"python","sourceType":"script","isGpuEnabled":false}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"!pip install tweepy\n!pip install textblob\nfrom textblob import TextBlob\nimport tweepy\nimport sys\n\nmykeys = open('twitterkeys.txt','r').read().splitlines()\napi_keys = mykeys[0]\napi_key_secret = mykeys[1]\naccess_token = mykeys[2]\naccess_token_secret = mykeys[3]\n\nauth_handler = tweepy.OAuthHandler(consumer_key = api_key,consumer_secret = api_key_secret)\nauth_handler.set_access_token(access_token, access_token_secret)\n\napi = tweepy.API(auth_handler)\nsearch_term = 'happiness/war' #Type any negative/positive topic of your choice\n\ntweet_ammount = 200\n\ntweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(tweet_amount)\n\npolaroty = 0\npositive = 0\nneutral = 0\nnegative = 0\n\nfor tweet in tweets:\n    final_text = tweet.text.replace('RT','')\n    if final_text.startswith(' @'):\n        postition = final_text.index(':')\n        final_text = final_text[position+2:]\n    if final_text.startswith('@'):\n        postition = final_text.index(' ')\n        final_text = final_text[position+2:]\n    \n    analysis = TextBlob(final_text)\n    tweet_polarity = analysis.polarity\n    if tweet_polarity > 0.00:\n        positive +=1\n    elif tweet_polarity < 0.00:\n        negative +=1\n    elif tweet_polarity == 0.00\n        neutral +=1 \n    polarity += analysis.polarity\n    print(final_text)\n    \nprint(polarity)\nprint(f' Amount of Positive Tweets are {positive}')\nprint(f' Amount of Positive Tweets are {negative}')\nprint(f' Amount of Positive Tweets are {neutral}')\n\n    \n    \n    \n    \n    \n    \n    \n\n","metadata":{"_uuid":"963e9bc9-cfa8-4432-a47c-c37fd9cb58c0","_cell_guid":"1b933efc-167f-4505-bd71-a29a3ae38a3a","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}