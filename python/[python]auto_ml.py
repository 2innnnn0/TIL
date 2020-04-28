# 작성 환경 콜랩 기준.

# automl 설치
# !pip3 install automl
# !pip3 install gcsfs dask

# auto_ml : lightgbm
from auto_ml import Predictor

column_descriptions = {
    'date' : 'ignore',
    'region': 'categorical',
    'weekday': 'categorical',
    'hour': 'categorical',
    'peak': 'ignore',
    'call_count': 'output'
}
# 모델 학습 및 성능검사
ml_predictor = Predictor(type_of_estimator='regressor', column_descriptions=column_descriptions)
ml_predictor.train( _train , model_names=['LGBMRegressor'])
ml_predictor.score( _test, _test.call_count )


# 학습된 모델 저장
filename = ".dill"
p = ml_predictor.save(filename)

# predict
dist_test['predict'] =  ml_predictor.predict(_dist_test)


# 저장한 ml model 불러오기
from auto_ml.utils_models import load_ml_model

def get_est_time_model() :
  trained_model = load_ml_model(".dill")
  return trained_model

trained_model = get_est_time_model()
