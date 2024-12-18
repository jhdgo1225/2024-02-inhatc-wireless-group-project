# 머신러닝 학습 모델 추천

## 추천 모델

| **모델**               | **설명**                                                                 | **추천 사용 사례**                                      |
|----------------------|-------------------------------------------------------------------------|-----------------------------------------------------|
| **선형 회귀 (Linear Regression)**  | - 가장 기본적인 회귀 모델로, 변수 간의 선형 관계를 모델링합니다.                             | - 주택 가격 예측, 학생 성적 예측                        |
| **로지스틱 회귀 (Logistic Regression)** | - 이진 분류 문제에 사용되며, 확률 기반의 분류 모델입니다.                                   | - 이메일 스팸 분류, 질병 여부 예측                     |
| **결정 트리 (Decision Tree)**      | - 데이터를 트리 구조로 분할하여 예측하는 모델입니다. 직관적이고, 해석이 용이합니다.             | - 고객 이탈 예측, 신용카드 사기 탐지                    |
| **K-최근접 이웃 (K-Nearest Neighbors, KNN)** | - 새로운 데이터 포인트를 가장 가까운 K개의 데이터와 비교하여 분류하는 모델입니다.             | - 손글씨 숫자 인식 (MNIST 데이터셋), 추천 시스템         |
| **서포트 벡터 머신 (Support Vector Machine, SVM)** | - 분류 문제에서 두 클래스 간의 경계를 최대화하는 모델입니다. 선형과 비선형 분류에 모두 적용 가능.  | - 얼굴 인식, 텍스트 분류                                |
| **랜덤 포레스트 (Random Forest)**  | - 여러 개의 결정 트리를 결합한 앙상블 모델로, 성능이 뛰어나고 과적합을 방지할 수 있습니다.       | - 고객 예측, 질병 진단, 금융 예측                       |
| **K-평균 군집화 (K-Means Clustering)** | - 군집화 알고리즘으로, 데이터를 K개의 군집으로 나누는 비지도 학습 모델입니다.                 | - 시장 세분화, 고객 클러스터링                         |
| **신경망 (Neural Networks)**       | - 여러 층의 뉴런을 사용하여 복잡한 패턴을 학습하는 모델입니다. 다층 퍼셉트론(MLP)을 사용할 수 있습니다. | - 이미지 분류, 자연어 처리, 추천 시스템                |
| **나이브 베이즈 (Naive Bayes)**    | - 조건부 확률을 이용한 분류 모델로, 간단하면서도 강력한 성능을 보입니다.                      | - 텍스트 분류, 스팸 필터링, 감정 분석                    |
| **XGBoost**                      | - 강력한 앙상블 모델로, Gradient Boosting을 기반으로 합니다. 높은 정확도와 성능을 제공합니다.     | - Kaggle 대회, 예측 모델링, 회귀 및 분류 문제 해결      |

## 모델 선택 시 고려할 사항

- **문제의 유형**: 분류(Classification) 문제인지, 회귀(Regression) 문제인지에 따라 선택할 모델이 달라짐.
- **데이터의 크기**: 작은 데이터셋에는 간단한 모델이, 큰 데이터셋에는 복잡한 모델이나 앙상블 모델이 적합.
- **해석 가능성**: 모델을 해석해야 하는 경우, 결정 트리나 로지스틱 회귀가 더 적합할 수 있다.

