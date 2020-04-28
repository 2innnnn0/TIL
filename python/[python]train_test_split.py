# train_test split
random_seed = 50
np.random.seed(random_seed)
msk = np.random.rand(len(train_df)) <= 0.8 # 80% 학습

_train = train_df[msk]
_test = train_df[~msk]

print(_train.shape)
print(_test.shape)
