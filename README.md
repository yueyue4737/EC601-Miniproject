# EC601 Mini Project
An app that people can use to search for the top ten popular pictures of their favorite K-pop group, find the similar clothing the singer wear for them and get the sentiments of the K-pop merchandise the picture may contain. 

## User Story
* I, as a big fan of BTS, want to use Twitter to find the most viewed pictures of my idol such as a stunning picture from the concert so that I will compensate for the missed interesting pictures as many as possible.
* I, as a fashion chaser, want to find K-pop fashionable pictures in order to get the similar clothing.
* I, as the designer of K-pop merchandises, would like to use Twitter to find out fans' feedback of new released product from their tweets, so that I can know the reason why they like or dislike our product and help us to improve it in the future.

## Architecture
![](https://github.com/Bunny-Nora/EC601-Miniproject/tree/master/img/Architecture.png)

## Basic Plan
* We will use Twitter APIs to get pictures from tweets only about the K-pop group name users assigned and read the number of their comments, likes and retweets. Then, we will use a pre-trained model to classify the pictures into two types (funny or stunning) and use the pre-decided threshold to determine the top ten popular pictures in each type. Finally, we will send them to our users.
* Users can circle the clothing people wear or a K-pop merchandise which may shown in the picture we displayed. For the former,we will use other API(pending) to find the buying link. For the latter,we will then use the name of the K-pop group to retrieve more pictures from the official account on Twitter and apply a machine learning model judge the similarity between the circled merchandise and the pictures. The comments of pictures with high similarity will be used to figure out fans’ feedbacks about this merchandise, which will be send back to our users.

## License
* BU ©Ningrong Chen
* BU ©Yinqi Zhang
