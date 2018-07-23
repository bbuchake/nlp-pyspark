##FUNCTIONS FOR MODEL ACCURACY

#Get dependencies
#For evaluation of models
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

#DECISION TREE CLASSIFIER
def dt_classifier(training, testing):
    #MODEL 1: DECISION TREE CLASSIFIER
    from pyspark.ml.classification import DecisionTreeClassifier

    #Initialize model
    dt = DecisionTreeClassifier()
    #Fit data into model
    dt_model = dt.fit(training)
    #Test model
    dt_predictions = dt_model.transform(testing)

    #Evaluate model
    dt_evaluator = MulticlassClassificationEvaluator(metricName='accuracy')
    dt_accuracy = dt_evaluator.evaluate(dt_predictions)
    return dt_accuracy

def rf_classifier(training, testing):
    #MODEL 1: DECISION TREE CLASSIFIER
    from pyspark.ml.classification import RandomForestClassifier

    #Initialize model
    rf = RandomForestClassifier(numTrees=10)
    #Fit data into model
    rf_model = rf.fit(training)
    #Test model
    rf_predictions = rf_model.transform(testing)

    #Evaluate model
    rf_evaluator = MulticlassClassificationEvaluator(metricName='accuracy')
    rf_accuracy = rf_evaluator.evaluate(rf_predictions)
    return rf_accuracy

def nb_classifier(training, testing):
    #MODEL 1: DECISION TREE CLASSIFIER
    from pyspark.ml.classification import NaiveBayes

    #Initialize model
    nb = NaiveBayes(modelType='multinomial')
    #Fit data into model
    nb_model = nb.fit(training)
    #Test model
    nb_predictions = nb_model.transform(testing)

    #Evaluate model
    nb_evaluator = MulticlassClassificationEvaluator(metricName='accuracy')
    nb_accuracy = nb_evaluator.evaluate(nb_predictions)
    return nb_accuracy

def ovr_classifier(training, testing):
    from pyspark.ml.classification import LogisticRegression, OneVsRest

    #Instantiate the base classifier.
    lr = LogisticRegression(maxIter=10, tol=1E-6, fitIntercept=True)
    #Instantiate the One Vs Rest Classifier.
    ovr = OneVsRest(classifier=lr)
    # train the multiclass model.
    ovr_model = ovr.fit(training)

    #Test model
    ovr_predictions = ovr_model.transform(testing)

    #Evaluate model
    ovr_evaluator = MulticlassClassificationEvaluator(metricName='accuracy')
    ovr_accuracy = ovr_evaluator.evaluate(ovr_predictions)
    return ovr_accuracy

def gbt_classifier(training, testing):
    from pyspark.ml.classification import GBTClassifier

    # Train a GBT model.
    gbt = GBTClassifier(maxIter=10)
    # Train model.  This also runs the indexers.
    gbt_model = gbt.fit(training)

    # Make predictions.
    gbt_predictions = gbt_model.transform(testing)

    #Evaluate model
    gbt_evaluator = MulticlassClassificationEvaluator(metricName='accuracy')
    gbt_accuracy = gbt_evaluator.evaluate(gbt_predictions)
    return gbt_accuracy



