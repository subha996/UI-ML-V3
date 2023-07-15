import warnings
warnings.filterwarnings("ignore")

import streamlit as st


def app():

    # function that will change the width of the web page
    def _max_width_():
                max_width_str = f"max-width: 950px;"
                st.markdown(
                    f"""
                <style>
                .reportview-container .main .block-container{{
                    {max_width_str}
                }}
                </style>    
                """,
                    unsafe_allow_html=True,
                )
    # calling the function for full page
    _max_width_()
    st.markdown("<h1 style='text-align: center;'>🤖 UI-ML 🤖™</h1>", unsafe_allow_html=True)

    # writing overview of the project
    overview = """
        I am Subhabrata Nath, the developer behind this project. The platform I have created enables users to upload datasets, 
        either by selecting from a set of provided sample datasets or by using their own. 
        Through this platform, users can effortlessly create basic machine learning models for both `Regression` and `Classification` tasks. 
        They can evaluate the `Performance` of their models and, if unsatisfied with the results, 
        `fine-tune` the model's `hyperparameters` and re-run the analysis using the selected hyperparameters. 
        It is important to note that this platform does not operate as an AutoML tool. Users are expected 
        to possess some prior knowledge about the algorithms and the influence of hyperparameters on the model's performance.

        Once a model has been created, users can conveniently download the trained model for future use. 
        The entire process is user-friendly and does not require any coding. 
        The platform offers a graphical user interface `(UI)` where users simply need to make selections and clicks 
        to carry out their desired actions. Additionally, there is a section dedicated to `Data Profiling.` In this section, 
        users can upload their datasets and obtain an Exploratory Data Analysis (EDA) report. This report enables users to 
        thoroughly explore and gain insights from their data.

        It is worth mentioning that all progress within each tab is `temporary.` 
        If you navigate away from a page during your work, your progress will be lost. 
        Therefore, it is advisable to complete your tasks within each section without interruption.

        Thank you for using this platform, and I hope you find it valuable for your machine learning endeavors.
        """
    st.markdown("<h2 style='text-align: center;'>🎈 Overview 🎈</h1>", unsafe_allow_html=True)
    st.write(overview)

    # wrting about regressions
    about_regession = """Regression is a type of Machine Learning that is used 
    to predict the value of a target variable based on the values of the independent variables.
    When You are in `Regression` page, there you have to upload your data, in this satge i only create this for `csv` file only.
    Also if you do not have any data in your hand you can choose sample data, that option you can find from `sidebar` after that you have to select
    the `target` column of your data, after that you have to choose which algorithm you will use, after choosing the algorithm
    you will be given some basic hyperparameter to tune them on the right side of the page. after selecting parameter you need to click
    the `Train and Give Socre` button, then after few secceon latter you can see the performance of the model. And if you are not satisfied 
    with the result change hyperparameter values and again click that button untill you find good result."""
    
    st.subheader('🏂 About Regression [Read More](https://en.wikipedia.org/wiki/Regression_analysis)')
    st.write(about_regession)

    #wrting about classification
    about_classification = """Classification is a type of Machine Learning that is used to predict class based on some independent feature
    The processs is same as Regression, you have to upload dataset or have to choose from the sample data, and the you will be given some 
    and then you will be given performance metrics for the classification problem from which you can judge your model. you will get `f1_score` and `confusion_matrix`, 
    based on that the performance on test data can be measured."""
    st.subheader('⛹️‍♂️ About Classification [Read More](https://en.wikipedia.org/wiki/Classification)')
    st.write(about_classification)
    
    # wrting about data profiling
    about_data_profiling = """Data Profiling is a type of data analysis that is used to understand the data. and to understand the distribution of the data.
    You can upload your data, or choose from the sample data, after that you will be given a report, which will tell you the distribution of the data,
    and also the basic statistics of the data. You can also see the `correlation` matrix of the data, which will tell you the relation between the features.
    You can also see the `covariance` matrix of the data, which will tell you the relation between the features.
    You can also see the `scatterplot` of the data, which will tell you the relation between the features.
    You can also see the `histogram` of the data, which will tell you the distribution of the data. The report is created by `pandas_profiling`
    library. you will get all the features that the library provied."""
    st.subheader('📊 About Data Profiling [Read More](https://en.wikipedia.org/wiki/Data_profiling)')
    st.write(about_data_profiling)

    # writing about how things done
    about_how_things_done = """
    Now I will describe how all things are going. If you are not interested in reading this, you can watch the video explanation that i also created where I show the full demonstration and code walkthrough.
    
    1. Now let me tell you how the thing is going. First, you are uploading data(or choosing from samples) you will show the dataset is load on the web page. 
    
    2. After that, you have to select your `target` column on the data. otherwise, the process will through error message to tell you to select the target column, you will be provided a list of all the columns present on the uploaded data and you have to select the target column for your problem. Internally the data will be divided into taring data and testing data, so i can give you some performance measures about the model on unseen data also.

    3. After selecting the target column you have to choose the `Algorithm` you want to use, there I provided the 4 most used and common algorithms for `Regression` and `Classification` problems. after selecting the algorithm you will given hyperparameter for tuning them, the default parameters are set by default, if you want to run the algorithm by default parameter, then leave those control as it is.

    4. Then click the `Train and Give Score` button to train the model and after training the model it will show you the general performance measure that you usually do after creating a model. 
    In the case of the `Regression Problem`, you will be provided `r2_score` the common measurement for the regression problems. the value lies between `0 to 1` and the more closer the value is to `1` the good model it is. 

    5. Also there will be `training` and `testing` plots where you get the idea about how the model is predicting values on training data as well as testing data. and `Residual` plot also be there to check the residual of prediction, the residual is the difference between target values to the predicted value, if the mean of your residual distribution is close to zero, it can be a good sign, if the distribution is spread far from mean that can sign of bad model.

    6. Now when you create your first model, and of course you will not be satisfied with the result(if yes then you are very lucky). then tune the `hyperparameters` from the widget I provided. 
    `Note` here, in the time of tuning hyperparameter wait at least for `2 seconds` and then change the other hyperparameter, because when changing some hyperparameter the model will run by that new hyperparameter, so it is recommended wait at least few sec before tune others hyperparameters, also you can get the notification from the `top right side` where a `RUNNING` sign will pop-up which tells you the code is running inside. Then run experiments as long as you want, you might change the `algorithm` from the sidebar menu if a particular algorithm is not working well with your data. you have 4 different algorithm there for both problem types.

    7. There is one checkbox `Apply Preprocessing`, you will find it when you will build the model not before that. If your data is come with some column with categorical value and not completely ready for feeding to the ml algorithms, then you can check that button, unless if you have preprocessed data, means you have taken care all categorical encoding and scaling the data if needed, then leave `uncheck` that box. if not then that function will do some preprocessing for your data before feeding it to the model. Only `OneHotEncoding` and `StandardScaling` will apply,  and also you will download the full pipeline. so it is recommended to use preprocess data.
    
    7. Now when you finish the model-building part, now you can download the trained model you will be given at the bottom of the page. Click on that link to download the model as `pickle` file.
    
    """
    
    st.subheader('🛠 About How things are going.')
    st.write(about_how_things_done)

    bye = """That's all till now I am able to build, in future I have the intention to make some up-gradation on this project, like add some more functionality and adding more preprocess steps and more algorithms."""
    st.write(bye)
    st.markdown("<h1 style='text-align: center;'> Until then ❤ </h1>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center;'>subhanath91@gmail.com</h4>", unsafe_allow_html=True)