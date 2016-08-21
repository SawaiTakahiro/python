# -*- coding: utf-8 -*-

import numpy as np

from sklearn import tree

hoge = np.array([[1,2,3],[200,300,400],[5,6,8]])
fuga = np.array([[0,1,2],[2,3,4],[5,6,7]])


clf = tree.DecisionTreeClassifier()
clf = clf.fit(hoge, fuga)

test_data = ([[200,300,400]])

result = clf.predict(test_data)
print(result)
