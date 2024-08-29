from transformers import AutoTokenizer,AutoModelForSequenceClassification
from scipy.special import softmax


tweet = "I am really sad today @ home"


#preprocess tweets
tweet_words= []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'

    elif word.startswith('http'):
        word = 'http'
    tweet_words.append(word)

tweet_proc = ' '.join(tweet_words)

# load model and tokenizer

roberta = "cardiffnlp/twitter-roberta-base-sentiment"

model = AutoModelForSequenceClassification.from_pretrained('roberta-base')
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ["Negative", "Neutral", "Positive"]

#Sentiment Analysis
encoded_tweet = tokenizer(tweet_proc, return_tensors = 'pt')
print(encoded_tweet)