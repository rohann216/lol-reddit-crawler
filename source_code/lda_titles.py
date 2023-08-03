import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from gensim.corpora import Dictionary
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordnet_lemmatizer = WordNetLemmatizer()

# Preprocess text data
def preprocess_text(df):
    df = df[~df['Title'].isin(['[removed]', '[deleted]'])].dropna()
    preprocessed_selftexts = []
    for text in df['Title']:
        # lowercase
        text = text.lower()
        # remove punctuation
        text = ''.join(ch for ch in text if ch not in string.punctuation)
        # tokenize
        tokens = word_tokenize(text)
        # lemmatize
        lemmas = ' '.join([wordnet_lemmatizer.lemmatize(token) for token in tokens])
        # save
        preprocessed_selftexts.append(lemmas)
    return preprocessed_selftexts

df = pd.read_csv('posts.csv', lineterminator='\n')
clean_posts = preprocess_text(df)

import gensim
from gensim import models
from gensim.utils import simple_preprocess

# Further preprocess the post titles
simple_posts = [simple_preprocess(title) for title in clean_posts]
stop_words = set(stopwords.words('english'))
filtered_titles=[]
for i in simple_posts:
    title=[]
    for j in i:
        if j not in stop_words:
            title.append(j)
    filtered_titles.append(title)

# Create a dictionary from the preprocessed titles
dictionary = Dictionary(filtered_titles)

# Filter out extreme values from the dictionary
dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=100000)

# Create a bag-of-words representation of the posts
bow_corpus = [dictionary.doc2bow(post) for post in filtered_titles]

# Train the LDA topic model
lda_model = models.LdaModel(bow_corpus, num_topics=5, id2word=dictionary, passes=10)

# Extract the top 20 words and their frequencies as percentages for each topic
for topic_id in range(lda_model.num_topics):
    word_probs = lda_model.get_topic_terms(topic_id, topn=20)
    
    print(f"Topic #{topic_id} Top 20 Words and Probabilities:")
    for word_id, prob in word_probs:
        word = dictionary[word_id]
        print(f"{word}: {prob:.4f}")
    
    print()

# Number of posts and average upvotes/comments
print("Total # of Posts: " + str(len(df)))
print("Average # of Upvotes: " + str(df['Score'].mean()))
print("Average # of Comments: " + str(df['Comments'].mean()))

# Generate word clouds and word frequency for each topic
color_map = 'cool'  # Choose a predefined color map or specify custom colors
fig, axes = plt.subplots(1, 5, figsize=(20, 5))
for i, (topic_num, topic_words) in enumerate(lda_model.show_topics(num_topics=-1, num_words=20)):
    # Extract word frequencies for the current topic
    word_frequencies = []
    for word_info in topic_words.split('+'):
        word = word_info.split('*')[1].strip().strip('"')
        word_frequencies.append(word)
    
    # Generate the word cloud for the current topic
    wordcloud = WordCloud(width=400, height=200, background_color='white', colormap=color_map).generate(' '.join(word_frequencies))

    # Plot the word cloud in the corresponding subplot
    axes[i].imshow(wordcloud, interpolation='bilinear')
    axes[i].set_title(f"Topic #{topic_num} Word Cloud")
    axes[i].axis('off')

# Adjust spacing between subplots
plt.tight_layout()

# Show the combined word cloud figure
plt.show()
