import sklearn;
import pandas as pd;


print(sklearn.__version__);

"""
5 Steps of scikit-learn workflow:
1. Load The DataSet
2. Process The Data
3. Split into Train/Tests.
4. Train The Model
5. Evaulate and Predict.
"""

from sklearn.datasets import load_iris;        #   It's use on import iris dataset. This is famous dataset in sklearn.
iris = load_iris();
df = pd.DataFrame(data = iris.data, columns=iris.feature_names);
df['target'] = iris.target;         #   Add target column to dataframe.

print(df.head(10));         #   Print first 10 rows of dataframe.
print()
print("Tail")
print(df.tail(10));        #   Print last 10 rows of dataframe.

data = pd.read_csv('File_Name.csv');        # import data file of this line 
print(data);
