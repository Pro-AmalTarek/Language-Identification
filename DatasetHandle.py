import string
import io
import re
from nltk.collocations import BigramCollocationFinder
import numpy as np
from nltk.classify import NaiveBayesClassifier


class DatasetHandle:
    datasets = {}
    rootDir = "..\\Datasets\\"

    def createDatasetsDic(self):
        self.datasets["Arabic"] = self.rootDir + "Arabic.txt"
        self.datasets["English"] = self.rootDir + "English.txt"
        self.datasets["German"] = self.rootDir + "German.txt"
        self.datasets["French"] = self.rootDir + "French.txt"
        # self.datasets["EgyptionArabic"] = self.rootDir + "EgyptionArabic.txt"

    def read_datasets(self, file):
        text = open(file, 'r', encoding='utf-8').read()
        return text