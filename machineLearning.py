# -*- coding: utf-8 -*-
"""実力テスト提出用.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z97R7ycV3e7yar4sYOhj3VCxZCPppye9

# データの前処理
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# データの読み込み
df_train = pd.read_csv('/content/bank_train.csv')
df_train.head(3)

df_test = pd.read_csv('/content/bank_test02.csv')
df_test.head(3)

# データの形を確認
df_train.shape

df_test.shape

"""**データを加工**

## 重複行を確認
"""

df_train.duplicated(keep=False)

df_train.duplicated(keep=False).value_counts()

df_test.duplicated(keep=False).value_counts()

df_train.drop_duplicates(inplace=True)

df_test.drop_duplicates(inplace=True)

df_train.duplicated(keep=False).value_counts()

df_test.duplicated(keep=False).value_counts()

"""## 欠損値処理"""

# 欠損値の確認
df_train.isnull()[:5]

# 欠損値の数を確認
df_train.isnull().sum()

# 欠損値の数を確認
df_test.isnull().sum()

# データ統計量の確認
df_train.describe()

"""### 数値の欠損値補完

#### age
"""

plt.hist(df_train['age'])

plt.hist(df_test['age'])

# ageの平均値の確認
df_train['age'].mean()

# ageの平均値の確認
df_test['age'].mean()

# 欠損値を平均値で補完
df_train = df_train.fillna({'age':df_train['age'].mean()})

# 欠損値を平均値で補完
df_test = df_test.fillna({'age':df_test['age'].mean()})

"""#### pdays"""

plt.hist(df_train['pdays'])

plt.hist(df_test['pdays'])

# pdaysの中央値の確認
df_train['pdays'].median()

# pdaysの中央値の確認
df_test['pdays'].median()

# 欠損値を中央値で補完
df_train = df_train.fillna({'pdays':df_train['pdays'].median()})

# 欠損値を中央値で補完
df_test = df_test.fillna({'pdays':df_test['pdays'].median()})

# 欠損値の数を確認
df_train.isnull().sum()

# 欠損値の数を確認
df_test.isnull().sum()

"""### 文字列型の欠損値補完

#### job
"""

df_train['job'].unique()

df_test['job'].unique()

df_train['job'].mode()

df_test['job'].mode()

df_train['job'].mode()[0]

df_test['job'].mode()[0]

# 最頻値を使用して欠損値を補完
df_train = df_train.fillna({'job':df_train['job'].mode()[0]})

# 最頻値を使用して欠損値を補完
df_test = df_test.fillna({'job':df_test['job'].mode()[0]})

"""#### marital"""

df_train['marital'].unique()

df_test['marital'].unique()

df_train['marital'].mode()

df_test['marital'].mode()

df_train['marital'].mode()[0]

df_test['marital'].mode()[0]

# 最頻値を使用して欠損値を補完
df_train = df_train.fillna({'marital':df_train['marital'].mode()[0]})

# 最頻値を使用して欠損値を補完
df_test = df_test.fillna({'marital':df_test['marital'].mode()[0]})

"""#### default"""

df_train['default'].unique()

df_test['default'].unique()

df_train['default'].mode()

df_test['default'].mode()

df_train['default'].mode()[0]

df_test['default'].mode()[0]

# 最頻値を使用して欠損値を補完
df_train = df_train.fillna({'default':df_train['default'].mode()[0]})

# 最頻値を使用して欠損値を補完
df_test = df_test.fillna({'default':df_test['default'].mode()[0]})

"""#### housing"""

df_train['housing'].unique()

df_test['housing'].unique()

df_train['housing'].mode()

df_test['housing'].mode()

df_train['housing'].mode()[0]

df_test['housing'].mode()[0]

# 最頻値を使用して欠損値を補完
df_train = df_train.fillna({'housing':df_train['housing'].mode()[0]})

# 最頻値を使用して欠損値を補完
df_test = df_test.fillna({'housing':df_test['housing'].mode()[0]})

"""#### loan"""

df_train['loan'].unique()

df_test['loan'].unique()

df_train['loan'].mode()

df_test['loan'].mode()

df_train['loan'].mode()[0]

df_test['loan'].mode()[0]

# 最頻値を使用して欠損値を補完
df_train = df_train.fillna({'loan':df_train['loan'].mode()[0]})

# 最頻値を使用して欠損値を補完
df_test = df_test.fillna({'loan':df_test['loan'].mode()[0]})

"""#### poutcome

"""

df_train['poutcome'].unique()

df_test['poutcome'].unique()

df_train['poutcome'].mode()

df_test['poutcome'].mode()

df_train['poutcome'].mode()[0]

df_test['poutcome'].mode()[0]

# 最頻値を使用して欠損値を補完
df_train = df_train.fillna({'poutcome':df_train['poutcome'].mode()[0]})

# 最頻値を使用して欠損値を補完
df_test = df_test.fillna({'poutcome':df_test['poutcome'].mode()[0]})



# 欠損値の数を確認
df_train.isnull().sum()

# 欠損値の数を確認
df_test.isnull().sum()

"""## ユニークな値を数値に変換

### Label Encording
"""

# モデルの宣言
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

"""#### default"""

le.fit(df_train['default'])

le.fit(df_test['default'])

# 適用
le.transform(df_train['default'])

# 適用
le.transform(df_test['default'])

df_train['default'] = le.transform(df_train['default'])

le.classes_

df_test['default'] = le.transform(df_test['default'])

le.classes_

"""**default = 'no' →0**

**default = 'yes' →1**

#### housing
"""

le.fit(df_train['housing'])

le.fit(df_test['housing'])

# 適用
le.transform(df_train['housing'])

# 適用
le.transform(df_test['housing'])

df_train['housing'] = le.transform(df_train['housing'])

le.classes_

le.classes_

df_test['housing'] = le.transform(df_test['housing'])

"""**housing = 'no' →0**

**housing = 'yes' →1**

#### loan
"""

le.fit(df_train['loan'])

le.fit(df_test['loan'])

# 適用
le.transform(df_train['loan'])

# 適用
le.transform(df_test['loan'])

df_train['loan'] = le.transform(df_train['loan'])

le.classes_

df_test['loan'] = le.transform(df_test['loan'])

le.classes_

"""**loan = 'no' →0**

**loan = 'yes' →1**

#### result
"""

le.fit(df_train['result'])

le.fit(df_test['result'])

# 適用
le.transform(df_train['result'])

# 適用
le.transform(df_test['result'])

df_train['result'] = le.transform(df_train['result'])

le.classes_

df_test['result'] = le.transform(df_test['result'])

le.classes_

"""**result = 'fail' →0　(不成約)**

**result = 'success' →1　(成約)**

### One-Hot Encording
"""

# カテゴリカル変数を含んだデータのみを抽出
df_train_obj = df_train.select_dtypes(include='object')
df_train_obj.head(3)

# カテゴリカル変数を含んだデータのみを抽出
df_test_obj = df_test.select_dtypes(include='object')
df_test_obj.head(3)

df_train_uni = df_train_obj.nunique()
df_train_uni

df_test_uni = df_test_obj.nunique()
df_test_uni

for uni in df_train_obj.columns:
    print(uni)
    print(df_train_obj[uni].unique())

for uni in df_test_obj.columns:
    print(uni)
    print(df_test_obj[uni].unique())

df_train.shape

df_test.shape

df_train = pd.get_dummies(df_train, drop_first=False)

df_test = pd.get_dummies(df_test, drop_first=False)

df_train.head(3)

df_test.head(3)

df_train.shape

df_test.shape

"""# 重回帰分析の実装"""

from sklearn.linear_model import LinearRegression

# 入力変数と出力変数の切り分け
x_train = df_train.drop('result', axis=1).values
t_train = df_train['result'].values

# インスタンス化
model = LinearRegression()

# モデルの学習
model.fit(x_train, t_train)

# 入力変数と出力変数の切り分け
x_test = df_test.drop('result', axis=1).values
t_test = df_test['result'].values

# インスタンス化
model = LinearRegression()

# モデルの学習
model.fit(x_test, t_test)

# モデルの検証
print('train score : ', model.score(x_train, t_train))
print('test score : ', model.score(x_test, t_test))

y_pred = model.predict(x_test)

"""# モデルの学習

"""

# モデルの定義
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier(random_state=0)

# モデルの学習
dtree.fit(x_train, t_train)

# モデルの検証
print('train score : ', dtree.score(x_train, t_train))
print('test score : ', dtree.score(x_test, t_test))

"""※決定係数ではなく、**正解率**"""

# 推論
dtree.predict(x_test)

"""# 木構造と Feature importance の確認"""

# 木構造の書き出し
import graphviz
from sklearn.tree import export_graphviz
dot_data = export_graphviz(dtree)

# 木構造の表示
graph_tree = graphviz.Source(dot_data)
graph_tree

#feature importance
feature_importance = dtree.feature_importances_
feature_importance

"""# サポートベクトルマシン (SVM)"""

# モデルの定義
from sklearn.svm import SVC
svc = SVC()

# モデルの学習
svc.fit(x_train, t_train)

# モデルの検証
print('train score : ', svc.score(x_train, t_train))
print('test score : ', svc.score(x_test, t_test))

"""# ロジスティック回帰でモデル構築

"""

# モデルの定義
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# モデルの学習
model.fit(x_train, t_train)

# モデルの検証
print(model.score(x_train, t_train))
print(model.score(x_test, t_test))

# 推論
y_pred = model.predict(x_test)

np.unique(y_pred)

np.unique(t_test, return_counts=True)

from sklearn import metrics

precision = metrics.precision_score(t_test, y_pred, average=None)
precision

recall = metrics.recall_score(t_test, y_pred, average=None)
recall

"""# 分類の閾値の調整"""

y_proba = model.predict_proba(x_test)
y_proba[0]

sns.distplot(y_proba[:, 1])
sns.distplot(y_proba[:, 0])
plt.xlabel('Probability')
plt.ylabel('Count')

sns.distplot(y_proba[:, 0])

y_pred = (y_proba[:,0] > 0.75).astype('i')

np.unique(y_pred, return_counts=True)

print('accuracy : ', metrics.accuracy_score(t_test, y_pred))
print('recall : ', metrics.recall_score(t_test, y_pred, average=None))

"""# 参考

### 重みの調整
"""

model = LogisticRegression(class_weight='balanced')

model.fit(x_train, t_train)

# 推論
y_pred = model.predict(x_test)

print('accuracy : ', metrics.accuracy_score(t_test, y_pred))
print('recall : ', metrics.recall_score(t_test, y_pred, average=None))

"""重みを調整したことで、正例が1の時のrecallは0.60になった

### DownSampling
"""

df_train = pd.DataFrame(x_train)
df_train['result'] = t_train
df_train.head()

# result=1のサンプルのインデックスを取得（少ない方のカテゴリ）
anomaly_indices = df_train[df_train['result'] == 1].index
num_records = len(anomaly_indices)

print(num_records)

# result=0 のサンプルのインデックスを取得（多い方のカテゴリ）
normal_indices = df_train[df_train['result'] == 0].index

sampled_indices = np.random.choice(normal_indices, num_records, replace=False)

len(sampled_indices)

total_indices = np.concatenate([anomaly_indices, sampled_indices])
print(len(total_indices))

df_undersampled = df_train.iloc[total_indices, :]

x_train_undersampled = df_undersampled.drop('result', axis=1).values
t_train_undersampled = df_undersampled['result'].values

sns.countplot(t_train_undersampled);

# モデルの宣言
model = LogisticRegression()
# モデルの学習
model.fit(x_train_undersampled, t_train_undersampled)

# 推論
y_pred = model.predict(x_test)

# AccuracyとRecallの確認
print('accuracy : ', metrics.accuracy_score(t_test, y_pred))
print('recall : ', metrics.recall_score(t_test, y_pred, average=None))

"""### SMOTE を用いての OverSampling"""

from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=0, k_neighbors=10)

x_train_oversampled, t_train_oversampled = smote.fit_resample(x_train, t_train)

sns.countplot(t_train_oversampled);

# モデルの宣言
model = LogisticRegression()
# モデルの学習
model.fit(x_train_oversampled, t_train_oversampled)

# 推論
y_pred = model.predict(x_test)

# Accuracy と Recall の確認
print('accuracy : ', metrics.accuracy_score(t_test, y_pred))
print('recall : ', metrics.recall_score(t_test, y_pred, average=None))

"""# まとめ

データが不均衡だったため、分類の閾値を調整したところ、recallは0.76380194になった。

参考として、accuracyとのバランスを考慮した他のモデルも添付する。
"""

