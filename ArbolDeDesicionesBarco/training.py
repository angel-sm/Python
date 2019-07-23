import pandas as pd 
from sklearn import tree
import graphviz 
trainig = pd.read_csv('./titanic3/titanic-test.csv')

# Add media in empty spaces
trainig['Gender'] = trainig['Gender'].apply(lambda toLabel: 0 if toLabel == 'male' else 1)
trainig['Age'].fillna(trainig['Age'].mean(), inplace = True)
y_target = trainig['Survived'].values
columns = ['Fare','Pclass','Gender','Age','SibSp']
X_input = trainig[list(columns)].values

clf_train = tree.DecisionTreeClassifier(criterion="entropy",max_depth=3)
clf_train = clf_train.fit(X_input,y_target)

target_labels = clf_train.predict(X_input) 
target_labels = pd.DataFrame({'Est_Survival': target_labels, 'Name':trainig['Name']})

#Evaluar el modelo
dot_data = tree.export_graphviz(clf_train, out_file = None,
                                    feature_names=columns,
                                    class_names=columns,
                                    filled=True,
                                    rounded=True,
                                    special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('./img/SurvivorColor', format='png')

