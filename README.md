# A-Music-Community-Website-Based-on-NLP-Sentiment-Analysis

## Abstract
This project aims to solve the lack of social media features on current music platforms, the
expensive and slow manual collection of user feedback, and the reluctance of users to provide
feedback. The method used was to combine a music player with a social media platform to create
an online music community website based on efficient web-development technologies. Additionally,
an NLP model was employed to automatically and effectively collect user feedback based on
sentiment analysis techniques.

The results of this project are a successful development of an online music community platform
where users can enjoy music with music enthusiasts. The platform also provides music companies
with visualized results of user feedback sentiment and trends of popular music.

The project’s conclusion is that this platform provides a possible solution for music companies
seeking to improve their commercial merits by increasing user engagement. Overall, this project
demonstrates the potential for the integration of social media features and NLP techniques to
enhance user engagement and improve commercial success in the music industry.

Project area: Natural language Processing (NLP); Software Engineering; Web Application Development;
Keywords: Music community; Data Visualization; NLP Sentiment analysis; Flask; Vue

## Introduction
User feedback is crucial for internet businesses. However, the traditional way of collecting user
feedback is not comprehensive enough and users are not proactive in giving feedback. With the
continuous development of NLP technology, large language models have gained the ability to
efficiently and accurately analyze and understand user feedback. Thus, we aim to apply NLP
sentiment analysis technology to a social media web application in our project, allowing platform
managers to better understand user preferences and emotions. This will help them adjust product
strategies accordingly, better meet user needs, attract more customers, and provide more benefits
for the platform.

At the same time, most music streaming platforms currently lack social features. We innovatively
combine the music player and user community in our project, allowing users to communicate with
other music enthusiasts through social interaction, and to establish deeper social relationships by
enjoying music together. This enhances the user experience, strengthens user preferences for our
music community platform, and ultimately increases potential consumption for our company.

To achieve this, we built a music community platform with NLP sentiment analysis functionality.
We created a fake traditional record company, Daring, which was the project’s client. At that
time, the company only released albums for offline sales. It didn’t have its own website, so fans
couldn’t access online music resources or the latest information easily. As a result, the business
marketing of the company may not have met the expected performance. Furthermore, fans didn’t
have a proper platform to share their thoughts on new songs. Finally, with the increase in total
customers, the original way of handling consumer feedback emails manually couldn’t efficiently
analyze the user’s requirements. The company required a more efficient and precise way to obtain
users’ preferences to make a future marketing strategy.

DMC (Daring Music Community), our music social platform, aims to solve the aforementioned issues by creating an online music community platform that provides users with more comprehensive
music services. In addition to allowing users to access the latest music resources and information,
the platform provides rich communication features, such as music discussion forums, posting, and
listening together functions. These features help users better explore music, and discover new
artists and music genres. Meanwhile, users can communicate and share experiences with other
music enthusiasts, thereby deepening user engagement with this music community.

Furthermore, the platform will collect user feedback on the company’s songs, including comments
and posts, as a basis for adjusting the company’s song sales strategy. This will help Daring better
understand users’ needs, so the company can apply music products and services that better cater
to users’ preferences and increase user satisfaction, thereby enhancing Daring’s commercial merits.

## NLP Model
Our NLP model is based on the highly regarded RoBERTa pre-trained model,
which can be found in [9], which is an advanced variant of the widely used BERT architecture.
Pre-training involves training a neural network model on a large and diverse corpus of text to learn
general language patterns and relationships so that it can then be fine-tuned for specific tasks.

Fine-tuning is the process of further training a pre-trained model on a task-specific
dataset to adapt it to the specific task at hand. For our model, we performed fine-tuning on the
DMC dataset, which is a multilingual dataset comprising Chinese, English, and Japanese text. By
fine-tuning the model on this dataset, we were able to ensure that the model was well-suited for
handling these specific languages and could effectively classify text in these languages according
to their sentiments.

To accelerate our training process, we utilized a cloud server, which
provides us with access to powerful computing resources that allow us to train our model more
quickly and efficiently than we would be able to use local hardware. This cloud server enabled
us to complete our training in a timely manner and obtain the best possible results for our NLP
model.

To find our model, you can visit /back-end/common/nlp/best_model,
where stores the trained weights and model files. For using this model to predict an input comment,
go to /backend/common/nlp/predict_cloud.py, where you can modify the ’main’ function to get
sentiment analysis result of a single comment. You can also use ’predict’ function as an API
of predicting multiple comments. Moreover, you can find a result in /nlp_code/result.txt which
stores our best model result on test dataset.

## NLP Implementation Module

This module is developed for the staff of the website, allowing the staff to view the analysis results
of the music resources statistics, as well as manually update the analysis results.

### Front-end
The front-end of this module is mainly developed in front-end/src/page/staff/management.vue.
Update Music Score This feature is able to update the music statistics used for analysis.
Statistics for All Music It presents the statistics for the 10 most popular songs and the 10 least
popular songs and music proportions in positive comments or negative comments.
Statistics for a Single Music It presents the statistics for a single song, including the percent￾ages of comments on this song, the popularity of this song at different times, and the number of
different comments on this song at different times.

### Back-end
After training our NLP model, we utilized it to predict comments and generate sentiment analysis
results represented as integers: 1 for positive, 0 for neutral, and -1 for negative. These results were
saved to the database for efficient retrieval. Additionally, we developed two distinct algorithms for
evaluating music and blog trends, considering their respective parameters.
For the music trends algorithm, we incorporated metrics such as views and likes in the numerator,
and the difference between positive and negative comments to gauge user sentiment. The denom￾inator considered factors like music publish time and the latest comment publish time, ensuring
that new songs could achieve higher trend scores.
![这是图片](/1.png "Magic Gardens")
Regarding the blog trends algorithm, we introduced a function that multiplied the blog publish
time (T) by a sentiment direction determinant. Applying a logarithmic operation helped smoothen
the difference between positive and negative comments.
![这是图片](/2.png "Magic Gardens")
Furthermore, we leveraged the music trends results to construct a data visualization module. Backend functions were designed to transfer data as JSON to the front end. Meanwhile, the music trends ranking function is also used for music recommendations for users
Lastly, we employed the OpenAI API to develop a chatbot capable of answering user queries about
music. To tailor the generated responses, we configured the prompt by retrieving music information from the database and filtering out unrelated questions.
You can find the trends algorithm and data visualization functions in /back-end/controllers/visualization.py.
NLP prediction function is in /back-end/common/nlp/predict_cloud.py. ChatAI function is in
/back-end/controllers/chat.py.
