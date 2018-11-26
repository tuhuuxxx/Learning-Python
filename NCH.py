import numpy as np
from scipy.optimize import minimize
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class NCHClassifier():
    def __init__(self, points, test, C):
        self.points = np.concatenate((points, test), axis=0)
        self.l = self.points.shape[0]
        self.y = np.asarray([1 for _ in range(self.l-1)] + [-1])
        self.bnds = [(0, C) for i in range(self.l-1)] + [(None, None)]
        
    def solve(self):
        def func(x):
            
            gt = 0
            for i in range(self.l):
                for j in range(self.l):
                    gt += x[i]*x[j]*self.y[i]*self.y[j]*(np.sum(self.points[i]*self.points[j]))
            return -(x[self.l-1] - gt/2)
            '''
            X = self.points
            y = self.y
            A = np.dot(X, X.T)
            B = np.dot(y, y.T)
            U = B*A
            return -(x[-1] - np.dot(np.dot(x.T, U), x)/2)
            '''
        xinit = [0.1 for _ in range(self.l)]
        bnds = self.bnds
        cons = [{"type": "eq", "fun": lambda x: np.sum(self.y*x)}]
        sol = minimize(func, x0=xinit, bounds=bnds, constraints=cons)
        
        return -sol.fun

def load_iris():
    samples = []
    labels = []
    with open('data/iris.data.txt', 'r') as f:
        lines = f.read()
        data = lines.split('\n')
        for item in data:
            x = item.split(',')
            samples.append(x[0:-1])
            labels.append(x[-1])
    label_set = list(set(labels))
    y = [label_set.index(i) for i in labels]
    samples = np.asarray(samples, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    return samples, y
'''
if __name__ == "__main__":
    points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    test = np.array([[0, -2]])
    C = 1
    nch_clf = NCHClassifier(points, test, C)
    print(nch_clf.solve())
'''
if __name__ == "__main__":
    samples, labels = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(samples, labels, test_size=0.2, random_state=42)    
    y_pred = []
    n_classes = len(set(labels))
    for test_point in X_test:
        distance = []
        for label in range(n_classes):
            points = X_train[np.where(y_train == label)]
            test_point = test_point.reshape(1, test_point.size)
            nch_clf = NCHClassifier(points, test_point, 1)
            distance.append(nch_clf.solve())
        y_pred.append(np.argmax(distance))
    print(accuracy_score(y_test, y_pred))
            
