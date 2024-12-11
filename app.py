import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel
import difflib
from flask import Flask,request, url_for, redirect, render_template
from markupsafe import Markup

def create_sim(search):
    df_org=pd.read_csv('Coursera.csv')
    df=df_org.copy()
    df.drop(['University','Difficulty Level','Course Rating','Course URL','Course Description'], axis=1,inplace=True)
    tfv = TfidfVectorizer(min_df=3,  max_features=None, 
            strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
            ngram_range=(1, 3),
            stop_words = 'english')

    # Filling NaNs with empty string
    df['cleaned'] = df['Skills'].fillna('')
    # Fitting the TF-IDF on the 'cleaned' text
    tfv_matrix = tfv.fit_transform(df['cleaned'])
    # Compute the sigmoid kernel
    sig = sigmoid_kernel(tfv_matrix, tfv_matrix)
    # Reverse mapping of indices and titles
    indices = pd.Series(df.index, index=df['Course Name']).drop_duplicates()
    
    def give_rec(title, sig=sig):
        # Get the index corresponding to original_title
        idx = indices[title]

        # Get the pairwsie similarity scores 
        sig_scores = list(enumerate(sig[idx]))

        # Sort the courses
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        # Scores of the 10 most similar courses
        sig_scores = sig_scores[1:11]

        # courses indices
        course_indices = [i[0] for i in sig_scores]

        # Top 10 most similar courses
        return df_org.iloc[course_indices]

    namelist=df['Course Name'].tolist()
    word=search
    simlist=difflib.get_close_matches(word, namelist)
    try: 
        findf=give_rec(simlist[0])
        findf=findf.reset_index(drop=True)
    except:
        findf=pd.DataFrame()
    
    return findf

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if (request.method == 'POST'):
        namec=(request.form['course'])
    
    output=create_sim(namec)
    if output.empty:
        ms='Sorry! we did not find any matching courses, Try adding more keywords in your search.'
        ht=' '
    else:
        ht=output.to_html(render_links=True, index=True)
        ht= Markup(ht)
        ms='Here are some recommendations :'
    return render_template('index.html',message=ms,pred=ht)

if __name__ == '__main__':
    app.run(debug=True)