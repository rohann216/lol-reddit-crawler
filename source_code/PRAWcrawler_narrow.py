import praw
import pandas as pd

# Create praw object using reddit app script details
reddit = praw.Reddit(client_id="CLIENT_ID",         # your client id
                     client_secret="CLIENT_SECRET",      # your client secret
                     username='USERNAME',
                     password='PASSWORD.',
                     user_agent="USER_AGENT")        # your user agent

# Set subreddits to crawl
subreddits = ['LeagueofLegends', 'SummonerSchool']

# Set keywords to search for
keywords = ['Creep Score', 'Last Hit', 'Last Hitting', 'Last-hit', 'Last-hitting', 
'Kiting', 'Trading', 'Skillshots', 'KDA', 'Clear Speed', 'Combos', 'Communication', 
'Smite timing', 'Mechanics', 'APM', 'Camera', 'Mousework', 'Button Pressing', 'Micro', 
'Inputs', 'Mechanical Skill', 'Pings', 'Micromechanics', 'Clicking', 'Clicks', 'Mouse', 'Movement', 
'Spacing', 'Click', 'Click Duration', 'Tracking', 'Aiming', 'Tab', 'Edge Panning', 'Chat', 'Outplay', 
'Pattern', 'Smart Cast', 'Quick Cast', 'A Click', 'Attack Move', 'Attack Command', 'Submovements', 
'Fundamentals', 'cancel', 'auto', 'pilot', 'piloting', 'Animation Canceling', 'Animation Cancel']

# Create an empty DataFrame to store the post information
columns = ['Subreddit', 'Score', 'Comments', 'Title', 'Keyword Count', 'URL']
df = pd.DataFrame(columns=columns)

# Iterate through each subreddit
for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)

    import re
    # need this because just using `in` doesn't account for phrases like 'Creep Score'
    def count_keywords(keywords, combined_text):
        keyword_count = 0
        for keyword in keywords:
            # Check if the keyword or phrase exists in the combined text
            if re.search(r"\b" + re.escape(keyword.lower()) + r"\b", combined_text.lower()):
                keyword_count += 1
        return keyword_count

    posts = set() # set doesn't include duplicates
    for keyword in keywords:
        # can search by title or selftext because we account for it later 
        # with keyword_count >= 6
        query = f'title:({keyword}) OR selftext:({keyword})'
        for post in subreddit.search(query, sort='relevance', time_filter='all', limit=None):
            combined_text = post.title + ' ' + post.selftext
            # count number of unique keywords present in post
            keyword_count = count_keywords(keywords, combined_text)
            # posts must have at least 6 keywords to be included
            if keyword_count >= 6:
                posts.add((post, keyword_count))
    sorted_posts = sorted(list(posts), key=lambda x: x[1], reverse=True)

    # Fill dataframe with relevant posts
    for post, keyword_count in sorted_posts:
            post_info = {
                'Subreddit': subreddit_name,
                'Score': post.score,
                'Comments': post.num_comments,
                'Title': post.title,
                'Keyword Count': keyword_count,
                'URL': post.url
            }
            df = pd.concat([df, pd.DataFrame(post_info, index=[0])], ignore_index=True)

# extract dataframe as csv output
df.to_csv('posts.csv', index=True)