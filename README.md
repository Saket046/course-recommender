# course-recommender
# Data collection

I collected this data set from Kaggle website. This datasets is having records related coursera courses and informations related to each courses. With the availability of numerous paid and free resources on the internet, it becomes overwhelming for students to learn new skills. Therefore, this dataset can be used to create Recommender Systems and recommend courses to students based on the Skills and Difficulty Level entered by the student. The Course Link is also provided, which can be offered by the Recommender System for easy access. The data set have following columns :

1) Course Name
	
2) University	

3) Difficulty Level
	
4) Course Rating	

5) Course URL	

6) Course Description	

7) Skills

The data set have 3522 rows and 7 columns.

link to the data base repository is https://www.kaggle.com/datasets/khusheekapoor/coursera-courses-dataset-2021

# Exploratory Data Analysis

we check for any null values and make sure that every columns in correct format.

# Creating the copy of the dataset

We create a copy of the data set so that we can use columns useful for recommending the similar courses and and dropping the columns that are not very useful for recommending courses. we keep the original dataset because while recommending the courses we need to print all the columns as our output so that user can see all the information related to recommended courses.

# Selecting column for recommending courses

we select skills column for recommending similar courses. so our recommendation engine consider courses having similar skills involved related to each other. we drop every other columns other then skills and name of course columns.

# Cleaning the data for NLP operations

We first declare the TF-IDF vectorizer removing english stop words and symbols then we store this cleaned data in a new row named 'cleaned'.

# Getting sparse matrix by TF-IDF

we create sparse matrix of each rows with all 7498 words found by TF-IDF. Whenever a word is present in that row then the sparse matrix put some vector values for that word in the matrix.

# Making sigmoid kernel

We make a sigmoid kernel which stores the similarity score between each each row of cleaned column with every other rows these similarity scores will tell us how much the given row is related to other rows in the dataset and by this we can find similar courses for recommendations. The values of sigmoid kernel is between 0 and 1 since it uses sigmoid function. This sigmoid kernel makes similarity score using the sparse matrix created by TF-IDF.

# Defining Function for Recommending similar courses

first we store index of each course in a variable name indices. In the function we first get the name of the course name as an input to the function, then we store the index of the course name to find similar courses. Then, we store sigmoid kernel values and give them index numbers. Then we sort the sigmoid score for the given index and get top 10 of them them we store the index of the recommended courses and then reverse map them to get the title of the top 10 courses. Then we return all related information of these courses from original data set as our function output.

# Finding courses using keywords

we find list of similar courses using keywords so that user can find similar courses even without knowing name of the courses available in the data set. we use get_close_matches function to get the closest match of the keyword from difflib library then we take the most closest match and then recommend courses using that closest matching course.

# Handling errors and no output senarioes

if the data given by user is in incorrect format or our recommendation system does not find any similar courses then it will show user a error message that will ask user to fill the values correctly or add more keywords so that our recommendation engine can find some similar courses and our webpage doesn't give a error message or crash. This function is acheived by python try and except error handling technique.

# Creating a Flask Framework

I created Webpage first and created a form in it in order to get the input from the user using get and post methods for course name or keywords, these inputs will be feeded to our recommendation engine system. values given by the user and stored it in some variable. Then we get the closest match for this given word and feed closest matching course of the given keyword to our recommendation function and then we store our output in a variable as a dataframe, if there is no recommendation we store the data as empty dataframe. Now based on weather we get a output or not we store a output message in some other variable. before passing our output dataframe to the webpage we first need to convert this dataframe into html tables. We did using to_html function from markup library of flask that converts the dataframe into html table. Then we pass both output table and message to our webpage to display it as a output.

# Deployment

After creating my app and required files I choose Heroku platform to deploy my recommendation engine. After creating requirements and Procfile that will tell heroku about needed libraries and point from where it have to start excecuting codes, I uploaded these files in Github and then link my repository to my app in Heroku and finally deployed my Coursera course recommendation engine.
