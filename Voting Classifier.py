import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier
import lightgbm as lgb
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import GradientBoostingClassifier
X=pd.read_excel('after_selection.xlsx',header=None)
Y=pd.read_csv('lab.txt',header=None)
dataset=np.column_stack((X,Y))


clf1 =  lgb.LGBMClassifier()
clf2 = MLPClassifier()
clf3 = GradientBoostingClassifier()


eclf = VotingClassifier(
    estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)],
    voting='hard')

for clf, label in zip([clf1, clf2, clf3,eclf], ['LGBM', 'MLPC', 'GBDT','Ensemble']):
    scores = cross_val_score(clf, X, Y, scoring='accuracy', cv=5)
    print("Accuracy: %0.6f (+/- %0.6f) [%s]" % (scores.mean(), scores.std(), label))