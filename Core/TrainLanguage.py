from Core.DatasetHandle import DatasetHandle
from Core.PreProcess import *
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

class TrainLanguage :

    #trainDataset = []

    def trainDataset(self):
        self.trainDataset = []
        handler = DatasetHandle()
        handler.createDatasetsDic()
        for langName, datasetPath in handler.datasets.items():
            Text = handler.read_datasets(datasetPath)
            preprocessor = PreProcessing(Text)
            tokens = preprocessor.dataPreprocess()
            bigramModel = self.BigramModel(tokens)
            self.trainDataset = self.trainDataset + [(self.prepareDataToClassifier(token), langName) for token in bigramModel]
        return self.trainDataset


    def BigramModel(self, tokens):
        tokens=set(tokens)
        finder = BigramCollocationFinder.from_words(tokens)
        bestBigrams = finder.nbest(BigramAssocMeasures.chi_sq, 500)
        for tuple in bestBigrams:
            formatTuple = "%s %s" % tuple
            tokens.add(formatTuple)
        return tokens

    def prepareDataToClassifier(self , token):
        return dict([(token, True)])
