
class DatasetHandle:
    datasets = {}
    rootDir = "..\\Datasets\\"

    def createDatasetsDic(self):
        self.datasets["Arabic"] = self.rootDir + "Arabic.txt"
        self.datasets["English"] = self.rootDir + "English.txt"
        self.datasets["German"] = self.rootDir + "German.txt"
        self.datasets["French"] = self.rootDir + "French.txt"
        self.datasets["Italian"] = self.rootDir + "Italian.txt"
        self.datasets["Japanese"] = self.rootDir + "Japanese.txt"
        self.datasets["Dutch"] = self.rootDir + "Dutch.txt"
        self.datasets["Hindi"] = self.rootDir + "Hindi.txt"
        self.datasets["Spanish"] = self.rootDir + "Spanish.txt"
        self.datasets["EgyptionArabic"] = self.rootDir + "EgyptionArabic.txt"

    def read_datasets(self, file):
        text = open(file, 'r', encoding='utf-8').read()
        return text
