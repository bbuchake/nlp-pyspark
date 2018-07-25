#Get dependencies
import pyspark

#Spark configuration settings to allow for faster processing
conf = pyspark.SparkConf()
conf.set("spark.executor.memory", "8g")
conf.set("spark.driver.memory", "8g")
conf.set("spark.core.connection.ack.wait.timeout", "1200")

from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.linalg import Vector
from pyspark.ml import Pipeline

from pyspark.sql.functions import col, udf
from pyspark.sql.types import FloatType
import time
import pandas as pd
import csv
from classifiers import dt_classifier, rf_classifier, nb_classifier, ovr_classifier, gbt_classifier

#Initialize Spark Session
spark = SparkSession.builder.appName('pyspark_compare_project').getOrCreate()

#Import csv for training data
start_data = spark.read.format("csv").option("header", "true").load("data/sepsis.csv")
#DATA CLEANUP
#Remove NULLs
start_data = start_data.na.drop(subset=["CATEGORY","COMMENT"])
#Filter to ensure that category is pulled in correctly
start_data = start_data.filter(start_data['CATEGORY'].isin('include','exclude'))

#BUILD FEATURES
# Create a length column to be used as a future feature 
from pyspark.sql.functions import length
data = start_data.withColumn('length', length(start_data['COMMENT']))

# Create all the features to the data set
include_exclude_to_num = StringIndexer(inputCol='CATEGORY',outputCol='label')
tokenizer = Tokenizer(inputCol="COMMENT", outputCol="token_text")
stopremove = StopWordsRemover(inputCol='token_text',outputCol='stop_tokens')
hashingTF = HashingTF(inputCol="stop_tokens", outputCol='hash_token')
idf = IDF(inputCol='hash_token', outputCol='idf_token')

# Create feature vectors
# See https://spark.apache.org/docs/latest/ml-features.html#vectorassembler
# This just creates a new, single vector of features that is the concatenation
# of tf-idf data and the length of the email
clean_up = VectorAssembler(inputCols=['idf_token', 'length'], outputCol='features')

#DATA PROCESSING PIPELINE
# Create a and run a data processing Pipeline
# See https://spark.apache.org/docs/latest/ml-pipeline.html#pipeline
data_prep_pipeline = Pipeline(stages=[include_exclude_to_num, tokenizer, stopremove, hashingTF, idf, clean_up])

# Fit and transform the pipeline
cleaner = data_prep_pipeline.fit(data)
cleaned = cleaner.transform(data)

#TRAINING AND TESTING DATA
# Break data down into a training set and a testing set
(training_60, testing_40) = cleaned.randomSplit([0.6, 0.4])
(training_70, testing_30) = cleaned.randomSplit([0.7, 0.3])
(training_80, testing_20) = cleaned.randomSplit([0.8, 0.2])

#List of models
models = ['Decision Tree Classifier', 'Random Forest Classifier', 'Naive Bayes Classifier', 'One-vs-Rest Classifier', 'GBT Classifier']
#Initialize master dictionary
models_master_list = []
trainingsets = [training_60, training_70, training_80]
testingsets = [testing_40, testing_30, testing_20]

for model in models:
    if(model == 'Decision Tree Classifier'):
        for num in range(0,3):
            start = time.time()
            accuracy = dt_classifier(trainingsets[num], testingsets[num])
            end = time.time()
            dict = {'model': model,
                        'train_test_split': num,
                        'accuracy': accuracy,
                        'duration': end-start,
                        'complexity': 3}
            models_master_list.append(dict)

    if(model == 'Random Forest Classifier'):
        for num in range(0,3):
            start = time.time()
            accuracy = rf_classifier(trainingsets[num], testingsets[num])
            end = time.time()
            dict = {'model': model,
                        'train_test_split': num,
                        'accuracy': accuracy,
                        'duration': end-start,
                        'complexity': 3}
            models_master_list.append(dict)

    if(model == 'Naive Bayes Classifier'):
        for num in range(0,3):
            start = time.time()
            accuracy = nb_classifier(trainingsets[num], testingsets[num])
            end = time.time()
            dict = {'model': model,
                        'train_test_split': num,
                        'accuracy': accuracy,
                        'duration': end-start,
                        'complexity': 2}
            models_master_list.append(dict)
    
    if(model == 'One-vs-Rest Classifier'):
        for num in range(0,3):
            start = time.time()
            accuracy = ovr_classifier(trainingsets[num], testingsets[num])
            end = time.time()
            dict = {'model': model,
                        'train_test_split': num,
                        'accuracy': accuracy,
                        'duration': end-start,
                        'complexity': 4}
            models_master_list.append(dict)

    if(model == 'GBT Classifier'):
        for num in range(0,3):
            start = time.time()
            accuracy = gbt_classifier(trainingsets[num], testingsets[num])
            end = time.time()
            dict = {'model': model,
                        'train_test_split': num,
                        'accuracy': accuracy,
                        'duration': end-start,
                        'complexity': 5}
            models_master_list.append(dict)

print(models_master_list)
#Convert to dataframe
master_df = pd.DataFrame(models_master_list)
master_df.to_csv('models_analysis.csv')

