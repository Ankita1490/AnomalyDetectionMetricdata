import pandas as pd
import numpy as np

from sklearn.metrics import classification_report



class ModelEvaluator:
    def __init__(self):
        pass

    def evalute(self, model, X_val:pd.DataFrame, val_true:pd.Series):
        X_val_noisy =X_val.copy()
        moise_level = 0.1
        for col in X_val_noisy.select_dtypes(include=['float','int']).columns:
            X_val_noisy[col] += np.random.normal(0, moise_level, size = X_val_noisy.shape[0])

        val_pred = model.predict(X_val_noisy)
        #val_pred = np.where(-1,1,0)
        return classification_report(val_true, val_pred)





