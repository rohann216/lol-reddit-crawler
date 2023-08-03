# lol-reddit-crawler

## PRAWcrawler_wide
- looks for posts that have at least one keyword in the title
### Post stats as of 8/3/2023
![image](https://github.com/rohann216/lol-reddit-crawler/assets/122564738/d2e8b7ba-eee4-43c9-81f0-24216ce44fc9)

## PRAWcrawler_narrow
- looks for posts that have at least 6 keywords in the title or selftext
### Post stats as of 8/3/2023
![image](https://github.com/rohann216/lol-reddit-crawler/assets/122564738/02381580-bf9e-4ffc-84ad-7899ed8b3cb7)

## lda_titles
- uses lda model to topic model the filtered posts and outputs post stats (count/avg upvotes/avg comments)
- also uses the model to create five word clouds that represent 5 topics found in the posts (represented by 20 frequently used words)
