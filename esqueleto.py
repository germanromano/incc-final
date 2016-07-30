import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
# Igual al RandomForest (hasta que agregue features)
# from sklearn.ensemble import ExtraTreesClassifier
# Un poco peor. ~85%
# from sklearn.tree import DecisionTreeClassifier


#Levanto features del dataset
# dataset = open('dataset.txt', 'r')
dataset = open('joined2.txt', 'r')

features = []
etiquetas = []

for line in dataset:
  if line[0] != '#':
    split = line.split(',')
    # features.append(map(float,split[:-1]))
    # etiquetas.append(int((split[-1])[0]))
    features.append(map(float,split[1:]))
    etiquetas.append(int((split[0])[0]))

#for i in features:
# print i
#print etiquetas

dataset.close()


# Vectores de features
#X = np.array([[1,0,0,0],[1,0,0,2],[1,0,0,10],[1,0,1,1],[1,0,0,1],[1,1,0,0],[1,0,0,1]])
X = np.array(features)

# Vector de etiquetas
#y = np.array([1, 0, 0, 1, 0, 1, 0])
y = np.array(etiquetas)

# Separacion en datos de desarrollo y validacion
X_dev, X_dev, y_verif, y_verif = cross_validation.train_test_split(X, y, test_size=0.1, random_state=1234)

# Separacion en datos de training y testing
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=1234)

#print X_train.shape, y_train.shape, X_test.shape, y_test.shape

# Hacer el clasificador
clf = RandomForestClassifier(n_estimators=15, random_state=1234)
# Entrenar
clf.fit(X_train, y_train)
# Predicho por el clasificador
y_pred = clf.predict(X_test)

# columns = ["numberOfSentences","numOfWords","avgWordLength","wwrl","wordsWithRepeatingLetters","questions","exclamations","avgTokensPerSentence","avgPunctuationMarksPerSentence","femPronouns","malePronouns","femToMalePronounRatio","childrenMentions","happiness","sadness","relationships","colors","affection","dreams"]
columns = ["numberOfSentences","numOfWords","avgWordLength","wwrl","wordsWithRepeatingLetters","questions","exclamations","avgTokensPerSentence","avgPunctuationMarksPerSentence","femPronouns","malePronouns","femToMalePronounRatio","childrenMentions","happiness","sadness","relationships","colors","affection","dreams","adjectives","adverbs","nouns","cardinals"]
importances = clf.feature_importances_
print zip(columns, clf.feature_importances_)

# Comparacion entre el predicho y el de etiquetas
print metrics.accuracy_score(y_test, y_pred)
print metrics.confusion_matrix(y_test, y_pred)

std = np.std([tree.feature_importances_ for tree in clf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances[indices],
       color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()
