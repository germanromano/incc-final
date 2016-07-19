import numpy as np
from sklearn import cross_validation
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

#Levanto features del dataset
dataset = open('dataset.txt', 'r')

features = []
etiquetas = []

for line in dataset:
	if line[0] != '#':
		split = line.split(',')
		features.append(map(float,split[:-1]))
		etiquetas.append(int((split[-1])[0]))

#for i in features:
#	print i
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
clf = RandomForestClassifier(n_estimators=10)
# Entrenar
clf.fit(X_train, y_train)
# Predicho por el clasificador
y_pred = clf.predict(X_test)

columns = ["numberOfSentences","numOfWords","avgWordLength","wwrl","wordsWithRepeatingLetters","questions","exclamations","avgTokensPerSentence","avgPunctuationMarksPerSentence","femPronouns","malePronouns","femToMalePronounRatio","childrenMentions"]
print zip(columns, clf.feature_importances_)

# Comparacion entre el predicho y el de etiquetas
print metrics.accuracy_score(y_test, y_pred)
print metrics.confusion_matrix(y_test, y_pred)
