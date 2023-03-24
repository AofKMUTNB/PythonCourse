from sklearn import tree
features = [[120,5] , [110,5] , [180,12] , [163,12]]
labels = ["ECO Car / B-Segment" , "ECO Car / B-Segment" , "VAN" , "VAN"]
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features,labels)
print(classifier.predict([[150 , 12]]))