import pandas as pd;

data = pd.read_csv('fake_data.csv');
# print(data);



# Problem is the Purchased value is Yes Or No Form but sklearn is not understand string form data that is understood by only integer form data.
# So we have to convert this string form data into integer form data.
# For this we use OneHotEncoding.

from sklearn.preprocessing import LabelEncoder, OneHotEncoder;

# We Are Using LabelEncoder for convert string form data into integer form data.
y = data['Purchased'];     # For Accessing Purchased column from data.
print(y);
label_enc = LabelEncoder();
y_enc = label_enc.fit_transform(y);
print(y_enc);       #   Now we have converted string form data into integer form data.

# So why yes or no convert into 0 and 1 that are converts 2,3 forms why 0 or 1 form.   because in label encoding are data start from 0 if here 3 values like yes, no or maybe then yes=1, no=2, maybe=3.


# OneHotEncoder

# OneHotEncodeing is so confusing LabelEncoding is Easy. 

