import pandas as pd

# JSON files are used when storing or extracting large data sets.
# It's a plain text file that has the format of an object.
# We use .read_json to create a dataframe from a JSON file's content.

data = pd.read_json("1_Introduction\data.json")
print(data.to_string())

# If the JSON code is not in a file but in a Python Dictionary, you can directly load it in a DataFrame

dataDict = {
    "Subject" : {
        "0" : "English",
        "1" : "Hindi",
        "2" : "Mathematics",
        "3" : "SST",
        "4" : "Science",
        "5" : "CS"
    },
    "Total Marks" : {
        "0" : 80,
        "1" : 80,
        "2" : 80,
        "3" : 80,
        "4" : 80,
        "5" : 50
    },
    "Marks Obtained" : {
        "0" : 76,
        "1" : 68,
        "2" : 74,
        "3" : 59.5,
        "4" : 80,
        "5" : 48
    },
    "Percentage" : {
        "0" : 95,
        "1" : 85,
        "2" : 92.5,
        "3" : 74.4,
        "4" : 100,
        "5" : 96
    }
}

dfDict = pd.DataFrame(dataDict)
print(dfDict.to_string())