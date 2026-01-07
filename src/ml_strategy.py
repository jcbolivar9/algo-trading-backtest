import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split

def train_xgb_strategy(df: pd.DataFrame, features_cols: list):
    X = df[features_cols]
    y = df["label"] + 1 # Convert -1,0,1 to 0,1,2 for XGBoost

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=0.2
    )

    model = xgb.XGBClassifier(
        objective='multi:softmax',
        num_class=3,
        n_estimators=200,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )

    model.fit(X_train, y_train)

    df.loc[X_test.index, "signal"] = model.predict(X_test) - 1

    return df, model