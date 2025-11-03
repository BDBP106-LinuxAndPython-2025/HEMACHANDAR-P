import pandas as pd

class CDataProcessor:
    def __init__(self, df):
        self.samples = df.shape[0]  # Number of rows
        self.features = df.shape[1]  # Number of columns

    def PrintDatasetInfo(self):
        print(f"Number of samples: {self.samples}")
        print(f"Number of features: {self.features}")

class CCSVProcessor(CDataProcessor):
    def __init__(self, filename):
        self.filename = filename
        self.dfData = pd.DataFrame()  # empty initially

    def LoadData(self):
        self.dfData = pd.read_csv(self.filename)
        super().__init__(self.dfData)  # initialize base class with dataframe

    def ConvertToJSON(self):
        json_filename = self.filename.rsplit('.', 1)[0] + ".json"
        self.dfData.to_json(json_filename, orient='records', lines=True)
        print(f"JSON file created: {json_filename}")

class CJSONProcessor(CDataProcessor):
    def __init__(self, filename):
        self.filename = filename
        self.dfData = pd.DataFrame()

    def LoadData(self):
        self.dfData = pd.read_json(self.filename, lines=True)
        super().__init__(self.dfData)

# ---------------------------
# Testing the classes as per tasks
# ---------------------------

def main():
    print("Task (a): Load titanic.csv using CCSVProcessor")
    titanic_processor = CCSVProcessor("titanic.csv")
    titanic_processor.LoadData()
    titanic_processor.PrintDatasetInfo()

    print("\nTask (b): Load ODI-Batting_Cricket_Analytics.csv and convert to JSON")
    cricket_processor = CCSVProcessor("ODI-Batting_Cricket_Analytics.csv")
    cricket_processor.LoadData()
    cricket_processor.ConvertToJSON()

    print("\nTask (c): Load the JSON file and print dataset info using CJSONProcessor")
    json_processor = CJSONProcessor("ODI-Batting_Cricket_Analytics.json")
    json_processor.LoadData()
    json_processor.PrintDatasetInfo()

if __name__ == "__main__":
    main()
