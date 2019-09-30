# EC601 Mini Project 1

## License
* BU ©Ningrong Chen
* BU ©Yinqi Zhang

## Usage Instruction
1. Download this repository to your computer using command`git clone git://https://github.com/Bunny-Nora/EC601-Miniproject.git`, then unzip the file
2. Fill in your Twitter `Consumer API keys` and `Access token & access token secret` in `communication.py` with comment `# Fill in your keys and tokens`
3. Run `gui.py` to start our graphical user interface. 
4. In this interface, you can enter a star's name you would like to search as the main keyword as well as a restriction keyword. For example: `main kayword: Justin Bieber` `restriction keyword: concert`
Then click either of the two buttons:
* Click `General sentiment` to see Twitter Users' recent sentiment of the star you search for.
* Click `Top 10 Pics` to see top 10 popular pictures of the star extracted from recent tweets.

## Architecture
![Architecture1](https://user-images.githubusercontent.com/9766409/65462122-1c357d80-de23-11e9-9e6b-e129ca285e70.png)


## User Story
* I, a big fan of a star, would like to know the recent sentiments about my idol of the public. For instance, as a big fan of Justin Bieber, I am concerned about the public reviews about his marriage. So, I can use the app to search for people’s sentiments about Justin Bieber on Twitter.
* I, the owner of an entertainment company, want to track Twitter Users‘sentiments of the celebrities in my company.
* I, as a big fan of BTS, want to use Twitter to find the most viewed pictures of my idol such as a stunning picture from the concert so that I will compensate for the missed interesting pictures as many as possible.


## Goal
* Analysis the sentiments of tweets.
* Display the Top 10 recent popular pictures.
* Write a graphic user interface to get the keyword and to display results.
* A web(pending) that people can use to search for the top ten popular pictures of their favorite celebrities in Twitter, get the sentiments of relevant tweets.

## APIs
1. Twitter API
2. Google Cloud Natural Language API
