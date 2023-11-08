import numpy as np
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from pandas import DataFrame
import matplotlib.pyplot as plt

def _tanh(x):
    return np.tanh(x)

class ELM(object):
    #num_input_nodes: number of columns
    def __init__(self, num_input_nodes, num_hidden_units, num_out_units):

        self._num_input_nodes = num_input_nodes
        self._num_hidden_units = num_hidden_units
        self._num_out_units = num_out_units

        self._activation = _tanh

        self._beta = np.random.uniform(-1., 1., size=(self._num_hidden_units, self._num_out_units))

        self._w = np.random.uniform(-1, 1, size=(self._num_input_nodes, self._num_hidden_units))

        self._bias = np.zeros(shape=(self._num_hidden_units,))

    def fit(self, X, Y, display_time=False):
        H = self._activation(X.dot(self._w) + self._bias)

        # Moore–Penrose pseudo inverse
        H_pinv = np.linalg.pinv(H)

        self._beta = H_pinv.dot(Y)

    def __call__(self, X):
        H = self._activation(X.dot(self._w) + self._bias)
        return H.dot(self._beta)

iris = datasets.load_iris()
X = iris.data
y = iris.target

lb = LabelBinarizer()
lb.fit(y)

y = lb.transform(y)

scaler_x = StandardScaler()
scaler_y = StandardScaler()

#Padronizacao valores
X = scaler_x.fit_transform(X)
y = scaler_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, shuffle=True)

mseTests = DataFrame(index=[i for i in range(0, 10)], columns=[i for i in range(5, 25, 5)])
perc_acertos = DataFrame(index=[i for i in range(0, 10)], columns=[i for i in range(5, 25, 5)])
#i = 0

for n_hidden in range(5, 25, 5):
    
    for test in range(0, 10):

        elm = ELM(X_train.shape[1], 100, 3)

        elm.fit(X_train, y_train)

        y_predicted_test = elm(X_test)

        #desfazer padronizacao valores
        X_original = scaler_x.inverse_transform(X_test)
        y_original = scaler_y.inverse_transform(y_test)

        predict = scaler_y.inverse_transform(y_predicted_test)

        y_original = lb.inverse_transform(y_original)

        predict = lb.inverse_transform(predict)

        mse = MSE(y_original, predict)

        mseTests.loc[test, n_hidden] = mse
        
        acertos = y_original - predict
        p_acertos = ((acertos==0).sum())/len(y_original)
        perc_acertos.loc[test, n_hidden] = p_acertos


print(perc_acertos)
print(mseTests)

fig, ax = plt.subplots()
ax.set_xlabel('Number of Neurons')
ax.boxplot(mseTests)
ax.set_title('Box plot')
ax.set_ylim([0,1])
plt.setp(ax, xticklabels=mseTests.columns)
plt.show()