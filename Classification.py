from nltk.classify import NaiveBayesClassifier
from Core.PreProcess import *
from Core.TrainLanguage import *
import os
import pickle
MyClassifier = r'D:\university\four year\second term\nlp\NLP_Project-my.pickle.pickle'
class Classifier:
    def __init__(self,inputText):
        if not os.path.exists(MyClassifier):
            trainLg=TrainLanguage()
            self.trainSet=trainLg.trainDataset()
            self.Myclassifier()
        else:
            self.classifier = pickle.load(open(MyClassifier, "rb"))

        self.inputText=inputText

    def prepareInputToClassifier(self,words):
        return dict([(word, True) for word in words])


    def detectLanguage(self):
        preprocessor = PreProcessing(self.inputText)
        textTOClassifier =self.prepareInputToClassifier(preprocessor.dataPreprocess())
        language = self.classifier.classify(textTOClassifier)
        return language

    def Myclassifier(self):
        self.classifier = NaiveBayesClassifier.train(self.trainSet)
        print( self.classifier,"kkkkkk")
        pickle.dump(self.classifier, open(MyClassifier, 'wb'))




