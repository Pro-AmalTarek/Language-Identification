import re
from nltk.tokenize import TweetTokenizer
#convert input to list of word
class PreProcessing :

    text = ""

    def __init__(self, dataText):
        self.text = dataText

    def remove_webLinks(self):
        ''' Get rid of web links(http or https) '''
        self.text = re.sub(r"http\S+", '', self.text)

    def remove_retweet(self):
        ''' Get rid of re-tweet "RT" '''
        self.text = re.sub(r"RT @", '', self.text)

    def remove_digits(self):
        ''' Get rid of all digits in text '''
        self.text = re.sub(r"\d", '', self.text)

    def remove_newLine(self):
        ''' Get rid of new Line or tab charachter '''
        self.text = self.text.replace("\t|\n|\r", "")

    def remove_punctuation(self):
        ''' Get rid of punctuation except apostrophes '''
        self.text = re.sub(r"[^\w\d\s']+", '', self.text)

    def remove_spaces(self):
        ''' Get rid of Additional Spaces '''
        self.text = re.sub(' +',' ', self.text)

    def convert_lowercase(self):
        ''' Convert text to lower case Characters '''
        self.text = self.text.lower()

    def tokenize_text(self):
        ''' Tokenize tweet text using TweetTokenizer '''
        tknzr = TweetTokenizer()
        return tknzr.tokenize(self.text)

    def dataPreprocess(self):
        ''' Preprocess data return tokenized words '''
        self.remove_webLinks()
        self.remove_retweet()
        self.remove_digits()
        self.remove_newLine()
        self.remove_punctuation()
        self.remove_spaces()
        self.convert_lowercase()
        return self.tokenize_text()

if __name__ == "__main__":
    """
    line = "Le match2 de   RT @#####  @@  n12345 Ligue RT @1 Bordeaux-Rennes, ce week-end, a été le théâtre' "
    """
    #process = PreProcessing(line)
    #print(process.dataPreprocess())
