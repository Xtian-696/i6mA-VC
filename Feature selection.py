import pandas as pd
import warnings
warnings.filterwarnings("ignore")


dataset=pd.read_excel('kmer_binary.xlsx',header=None)
# dataset=pd.read_csv('rice_RFHCP2.txt',header=None)
X=dataset
label=pd.read_csv('lab.txt',header=None)
Y=label



def GBDT():
    from sklearn.feature_selection import SelectFromModel
    from sklearn.ensemble import GradientBoostingClassifier
    clf=GradientBoostingClassifier().fit(X,label)
    model=SelectFromModel(clf,prefit=True)
    newMat=model.transform(X)
    pd.DataFrame(newMat).to_csv('GBDT.csv',header=False,index=False)

def ET():
    from sklearn.feature_selection import SelectFromModel
    from sklearn.ensemble import ExtraTreesClassifier
    clf = ExtraTreesClassifier()
    clf.fit(X,label)
    importance=clf.feature_importances_
    model=SelectFromModel(clf,prefit=True)
    new_data = model.transform(X)
    pd.DataFrame(new_data).to_csv('ET.csv',header=False,index=False)

if __name__ == '__main__':
    GBDT()
    ET()