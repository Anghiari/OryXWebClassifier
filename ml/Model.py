import Orange, cPickle

data = Orange.data.Table("dataset2.csv")
bayes = Orange.classification.bayes.NaiveLearner()
classifier = bayes(data)
cPickle.dump(classifier, open("oryx2_1.pck", "wb"))

knnLearner = Orange.classification.knn.kNNLearner()
knnLearner.k = 10
knnClassifier = knnLearner(data)
cPickle.dump(knnClassifier, open("oryx2_2.pck", "wb"))


tree_classifier = Orange.classification.tree.TreeLearner(data)
cPickle.dump(tree_classifier, open("oryx2_3.pck", "wb"))

print "done"