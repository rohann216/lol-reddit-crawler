# lol-reddit-crawler

## Keywords used as of 8/3/2023
['Creep Score', 'Last Hit', 'Last Hitting', 'Last-hit', 'Last-hitting', 
'Kiting', 'Trading', 'Skillshots', 'KDA', 'Clear Speed', 'Combos', 'Communication', 
'Smite timing', 'Mechanics', 'APM', 'Camera', 'Mousework', 'Button Pressing', 'Micro', 
'Inputs', 'Mechanical Skill', 'Pings', 'Micromechanics', 'Clicking', 'Clicks', 'Mouse', 'Movement', 
'Spacing', 'Click', 'Click Duration', 'Tracking', 'Aiming', 'Tab', 'Edge Panning', 'Chat', 'Outplay', 
'Pattern', 'Smart Cast', 'Quick Cast', 'A Click', 'Attack Move', 'Attack Command', 'Submovements', 
'Fundamentals', 'cancel', 'auto', 'pilot', 'piloting', 'Animation Canceling', 'Animation Cancel']

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
### Example narrow word cloud
![image](https://github.com/rohann216/lol-reddit-crawler/assets/122564738/3c21588a-c782-4082-86a2-402c472c695e)
