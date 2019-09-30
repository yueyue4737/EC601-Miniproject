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

## APIs,libraies used
1. Twitter API (Twython)
2. Google Cloud Natural Language API
3. pyqt5

## Testing Cases
* Test Case 1 (Sentiment for fans): positive case
![testCase3](https://user-images.githubusercontent.com/9766409/65824900-4087c480-e23e-11e9-9ca8-8e4523fe4839.png)
* Test Case 2 (Sentiment for funs): neutral case
![testCase4](https://user-images.githubusercontent.com/9766409/65824904-51d0d100-e23e-11e9-8980-ba70d77ee1a2.png)
* Test Case 3 (Pictures for fans)
![testCase2](https://user-images.githubusercontent.com/9766409/65824887-12a28000-e23e-11e9-9471-7c25d3ee38d1.png)
* Test Case 4 (Sentiment for staff)
![testCase1](https://user-images.githubusercontent.com/9766409/65824879-f56db180-e23d-11e9-8511-32e39db20d13.png)

## Lessons Learned
__1. What you liked doing?__
  * Play with the GUI.
  * Yinqi: I like reading the documents to find out details about how to use a function. For instance, what is this fucntion for? What's the meaning of each parameters. What's the return value type. There are quite a few more, and figuring out them is interesting.
  * Ningrong: I like learning a lot of new things such as pyqt5 to build a graphic user interface, twython and google Natural Language API, which makes me feel I am stepping into a new field.
  
__2. What you could have done better?__

If we have more time, we would like to add the following two functions:
  * Not only display the sentiment of stars but also the relevent tweets for users to read.
  * Display top 10 popular pictures with urls of tweets where pictures extracted from. In this way, we will feed our users with more information they concerned about.
  
__3. What you will avoid in the future?__

In the process of doing this project, we found it took much more effort than we thought to work together efficiently.
  * First of all, do remember to use bu email address to apply for twitter keys and tokens or you're very likely to be rejected. We wasted almost three days on this issue :(
  * Before you get down to write code, only establish the whole logic of your program is crucial yet not enough. Once the program structure was decided, we also figured out most functions' name, their parameters, their return value and how these functions would work with each other, which enabled us to write different modules of our program simultaneously.
    The logic of our program, however, changed from time to time, leading to conflicts between modules. So, next time woking on a team, we think it's better to stop to revise all descriptions of functions after changes.

## Architecture (Modules)
Our program will interact with both users and APIs, so `gui.py` and `communication.py` are needed. Data obtained by these two modules will be translated to `analysis.py` module to get results. Because the program will request for pictures from twiiter APIs, a `storage.py` module is added to download pictures from the remote server and store it in usrs' computers.
![architecture](https://user-images.githubusercontent.com/9766409/65824294-6d36de80-e234-11e9-8999-b98ea747e0c3.png)

## License
* BU ©Ningrong Chen
* BU ©Yinqi Zhang
