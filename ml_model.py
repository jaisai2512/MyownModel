import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv('framingham.csv')
df.dropna(axis=0, inplace=True)
new_feature = df[['male', 'age', 'cigsPerDay', 'totChol', 'sysBP', 'glucose', 'TenYearCHD']]
titanic_array = new_feature.to_numpy()
X_train, X_test, y_train, y_test = train_test_split([item[0:-1] for item in titanic_array],
                                                    [item[-1] for item in titanic_array], test_size=0.5,
                                                    random_state=42)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Save the model using joblib
joblib.dump(logreg, 'logreg.joblib')
