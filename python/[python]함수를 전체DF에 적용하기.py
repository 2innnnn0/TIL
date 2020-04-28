# Z 스코어로 변경할떄,
def z_score(X):
    Z = (X-X.mean(axis=0)) / X.std(axis=0)
    return Z

X_train = X_train.apply(lambda x : z_score(x))
X_train.describe()