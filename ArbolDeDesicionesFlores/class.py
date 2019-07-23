import matplotlib
import graphviz
from sklearn.datasets import load_iris
from sklearn import tree
from IPython.display import Image
import os
os.environ['PATH'] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# Cargar la libreria de irirs
iris = load_iris()
# print(iris)
# Crear el arbol de deciciones
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
tree.plot_tree(clf)

# Generar imagen del arbol de decicion 
dot_data = tree.export_graphviz(clf, out_file = None,
                                    feature_names=iris.feature_names,
                                    class_names=iris.target_names,
                                    filled=True,
                                    rounded=True,
                                    special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('./img/irisColor', format='png')

# 
img = Image(filename=('irisColor.png'))


