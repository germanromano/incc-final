import numpy as np
from sklearn import cross_validation
import random

# Chance

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
X_dev, X_verif, y_dev, y_verif = cross_validation.train_test_split(X, y, test_size=0.1, random_state=1234)

# Separacion en datos de training y testing
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X_dev, y_dev, test_size=0.2, random_state=1234)

coin_weight = float(y_train.tolist().count(0)) / len(y_train)
print coin_weight

def flip():
  return 0 if random.random() < coin_weight else 1

# Chance classifier:
def classify():
  counter = 0
  for res in y_verif:
    if flip() == res:
      counter += 1
  return float(counter) / len(y_verif)

list = []
for classification in range(1,1000):
  list.append(classify())

print "Chance result: ", np.mean(list)
