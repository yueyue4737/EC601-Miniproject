# EC601 Mini Project

## Instruction
Run the <strong>gui.py</strong> in the terminal directly. You can input the main keyword and restriction word you want to search, then choose functions via buttons:
* General sentiment(left button):show the recent Twitter Users' sentiment of the searching keywords;
* Top 10 pics(right button):display Top 10 recent popular pictures.

## Target Users
* Fans
* The staff of an entertainment company

## User Story
* I, a big fan of a star, would like to know the recent sentiments about my idol of the public. For instance, as a big fan of Justin Bieber, I am concerned about the public reviews about his marriage. So, I can use the app to search for people’s sentiments about Justin Bieber on Twitter.
* I, the owner of an entertainment company, want to track Twitter Users‘sentiments of the celebrities in my company.
* I, as a big fan of BTS, want to use Twitter to find the most viewed pictures of my idol such as a stunning picture from the concert so that I will compensate for the missed interesting pictures as many as possible.

## MVP
* Analyze the sentiments of tweets.
* Display the Top 10 recent popular pictures.

## Lessons Learned
* What you liked doing?
  * Play with the GUI.
  * Yinqi: Read the documents
  * Ningrong: Use Google Natural Language API
* What you could have done better?
  * Add connected url beside the pictures.
  * Whole results of twitter feedback.
* What you will avoid in the future?
  * Not using bu email address to apply for the authentication.
  * starting code before building whole logic(???)

## APIs,libraies
1. Twitter API(Twython)
2. Google Cloud Natural Language API
3. pyqt5

## Architecture
![architecture](https://user-images.githubusercontent.com/9766409/65824294-6d36de80-e234-11e9-8999-b98ea747e0c3.png)

## Testing
* Test Case 1 for staff
![testCase1](https://user-images.githubusercontent.com/9766409/65824879-f56db180-e23d-11e9-8511-32e39db20d13.png)
* Test Case 2 for fans (Pics)
![testCase2](https://user-images.githubusercontent.com/9766409/65824887-12a28000-e23e-11e9-9471-7c25d3ee38d1.png)
* Test Case 3 for fans (Sentiment)
![testCase3](https://user-images.githubusercontent.com/9766409/65824900-4087c480-e23e-11e9-9ca8-8e4523fe4839.png)
* Test Case 4 for the pubilc (Sentiment)
![testCase4](https://user-images.githubusercontent.com/9766409/65824904-51d0d100-e23e-11e9-8980-ba70d77ee1a2.png)

## License
* BU ©Ningrong Chen
* BU ©Yinqi Zhang
