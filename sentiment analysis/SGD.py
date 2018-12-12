import numpy as np

class SGD():
    def __init__(self, max_iter=500, tol=0.00001, eta=0.1):
        self.n_epochs = max_iter
        self.tol = tol # loss > previous_loss - tol
        self.eta = eta # learning rate
        
    def fit(self, X, y):
     
        theta = np.ones((X.shape[1], 1)) # x.sharpe[0] : n_points, X.shape[1]: n_attributes
        
        for k in range(self.n_epochs):
            for i in range(X.shape[0]):
                grad = (np.dot(X[i], theta)-y[i])*X[i]
                theta = theta - self.eta*grad.reshape(X.shape[1], 1)
                
                if np.linalg.norm(grad) < self.tol:
                    break
            # shuffle X, Y
            indices = np.random.permutation(X.shape[0])
            X = X[indices]
            y = y[indices]
        self.theta = theta
    
    def predict(self, test):
        y = np.dot(test, self.theta)
#        print(y)
        y_pred = []
        for item in y:
            if abs(item - 1) > abs(item + 1):
                y_pred.append(-1)
            else:
                y_pred.append(1)
        return y_pred
       
if __name__ == "__main__":
    X = np.array([[0, 0], [0, 0.1], [1, 1], [1, 0.9]])
    Y = np.array([-1, -1, 1, 1])
    sgd = SGD()
    sgd.fit(X, Y)
    test = np.array([[0.8, 0.8], [0.8, 1], [0, 0.2]])
    print(sgd.predict(test))
    
                
            
        