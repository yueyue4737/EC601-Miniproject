# EC601 Mini Project

## Usage Instruction
1. Download this repository to your computer using command`git clone git://https://github.com/Bunny-Nora/EC601-Miniproject.git`, then unzip the file
2. Fill in your Twitter `Consumer API keys` and `Access token & access token secret` in `communication.py` where there is a comment `# Fill in your keys and tokens`
3. Run `gui.py` to start our graphical user interface. 
4. In this interface, you can enter a star's name you would like to search as the main keyword as well as a restriction keyword. For example: `main kayword: Justin Bieber` `restriction keyword: concert`
Then click either of the two buttons:
* Click `General sentiment` to see Twitter Users' recent sentiment of the star you search for.
* Click `Top 10 Pics` to see top 10 popular pictures of the star extracted from recent tweets.

## Target Users
* Fans who concerns about public's sentiment of their idol
* Fans who would like to keep abreast of their idols' dynamics but have little time browsing tweets
* The staff of an entertainment company who would like to know public's attitude of artists of their company

## User Story
* I, a big fan of a star, would like to know the recent sentiments about my idol of the public. For instance, as a big fan of Justin Bieber, I am concerned about the public reviews about his marriage. So, I can use the app to search for people’s sentiments about Justin Bieber on Twitter.
* I, as a big fan of BTS, want to use Twitter to find the most viewed pictures of my idol such as a stunning picture from the concert so that I will compensate for the missed interesting pictures as many as possible.
* I, the owner of an entertainment company, want to track Twitter Users' sentiments of the celebrities in my company.

## MVP
* Analyze the sentiments of tweets.
* Extract pictures from tweets and display them in a graphical user interface.

## Lessons Learned
1. What you liked doing?
  * Play with the GUI.
  * Yinqi: Read the documents
  * Ningrong: Use Google Natural Language API
2. What you could have done better?
  * Add connected url beside the pictures.
  * Whole results of twitter feedback.
3. What you will avoid in the future?
  * Not using bu email address to apply for the authentication.
  * starting code before building whole logic(???)

## APIs,libraies used
1. Twitter API (Twython)
2. Google Cloud Natural Language API
3. pyqt5

## Architecture (Modules)
![architecture](https://user-images.githubusercontent.com/9766409/65824294-6d36de80-e234-11e9-8999-b98ea747e0c3.png)

## Testing
* Test Case 1 (Sentimen for fans): positive case
![testCase3](https://user-images.githubusercontent.com/9766409/65824900-4087c480-e23e-11e9-9ca8-8e4523fe4839.png)
* Test Case 2 (Sentiment for funs): neutral case
![testCase4](https://user-images.githubusercontent.com/9766409/65824904-51d0d100-e23e-11e9-8980-ba70d77ee1a2.png)
* Test Case 3 (Pictures for fans)
![testCase2](https://user-images.githubusercontent.com/9766409/65824887-12a28000-e23e-11e9-9471-7c25d3ee38d1.png)
* Test Case 4 (Sentiment for staff)
![testCase1](https://user-images.githubusercontent.com/9766409/65824879-f56db180-e23d-11e9-8511-32e39db20d13.png)

## License
* BU ©Ningrong Chen
* BU ©Yinqi Zhang
