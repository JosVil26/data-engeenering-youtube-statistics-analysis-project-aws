# YouTube Statistics Data Analytics | Data Engineering AWS Project

## Introduction
This data engineering project aims to leverage AWS services to analyze YouTube statistics. By utilizing S3 for data storage, Lambda for event-driven processing, Glue for ETL tasks, Athena for interactive querying, QuickSight for data visualization, and IAM for secure access control, we will create a robust and scalable solution to extract valuable insights from YouTube data. This project will enable us to explore trends, user behavior, and performance metrics to make data-driven decisions.

## Architecture
![Project Architecture](Youtube.drawio.png)

## Technology Used
1. Python
2. SQL
3. Amazon Web Services:
    - IAM
    - S3
    - Lambda
    - Glue
    - Athena
    - QuickSight

## Dataset Used
This Kaggle dataset includes several months (and counting) of data on daily trending YouTube videos. Data is included for many locations, with up to 200 listed trending videos per day. Each region’s data is in a separate file(CSV files). Data includes the video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count. The data also includes a category_id field, which varies between regions. To retrieve the categories for a specific video, find it in the associated JSON. One such file is included for each of the five regions in the dataset.

### More Information About Dataset
- Original Data Source - https://www.kaggle.com/datasets/datasnaek/youtube-new

## Analytic ETL Job
![ETL Job](ETL%20Analytics.png)

## Script for Project
1. [Lambda function for process JSON files](lambda_function.py)
2. [Glue Job for process CSV files](csv_to_parquet.py)
3. [Glue ETL Jor for Analytic](youtube-project-parquet-analytics-version.py)

## Conclusions
This project give me some new knowledgement about AWS and present some issues like change the data type of a column created by the Glue crawler, in that sense the crawler has difficults to parse the appropiate data type when the data is an integer for example, I had to do exploratory data analysis to assure the quality of the data, in that sense I discover null values in some important fields of the CSV files which I had to drop. Furthermore I deleted duplicate rows in the job that join the parquet files which storage the data from CSV and JSON files. I think that is possible to use some machine learning algorithms to do sentiment analysis in a variety of forms, Categorising YouTube videos based on their comments and statistics, statistical analysis over time, etc

## Author: José Villegas

## Follow me on
- GitHub: [@JosVil26](https://github.com/JosVil26)
- LinkedIn: [@josevillegasm](https://www.linkedin.com/in/josevillegasm/)
