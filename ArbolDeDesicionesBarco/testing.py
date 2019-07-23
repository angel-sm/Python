import pandas as pd 
from sklearn import tree
import graphviz 
testing = pd.read_csv('./titanic3/titanic-test.csv')
all_data = pd.read_csv('./titanic3/titanic_all.csv')

# Add media in empty spaces
testing['Gender'] = testing['Gender'].apply(lambda toLabel: 0 if toLabel == 'male' else 1)
testing['Age'].fillna(testing['Age'].mean(), inplace = True)
y_target = testing['Survived'].values
columns = ['Fare','Pclass','Gender','Age','SibSp']
X_input = testing[list(columns)].values

clf_train = tree.DecisionTreeClassifier(criterion="entropy",max_depth=3)
clf_train = clf_train.fit(X_input,y_target)

target_labels = clf_train.predict(X_input) 
target_labels = pd.DataFrame({'Est_Survival': target_labels, 'Name':testing['Name']})

ts = pd.merge(target_labels,all_data[['Name','Survived']], on=['Name'])

print(ts)

