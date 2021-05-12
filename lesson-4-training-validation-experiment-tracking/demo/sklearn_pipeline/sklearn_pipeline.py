from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, make_pipeline

pipe1 = Pipeline(
    steps=[
        ("imputer", SimpleImputer()),
        ("scaler", StandardScaler()),
        ("model", LogisticRegression)
    ]
)
# OR
pipe2 = make_pipeline(SimpleImputer(), StandardScaler(), LogisticRegression())
# Then use as usual:
# pipe.fit(X_train, y_train)
# pipe.predict(X_test)
# pipe.predict_proba(X_test)
