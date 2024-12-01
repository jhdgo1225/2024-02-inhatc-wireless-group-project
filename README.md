# 2024년 2학기 무선네트워크 1조

### 사업아이템: 이미지 분석을 이용한 미세 플라스틱 검출기

#### 조원: 류경록, 박종호, 유준선, 장동건, 정지민

---

## 0. 사업계획서

## 1. 사업아이템 설명<br/>

### 1.1. 사업아이템 소개<br/>

-   미세 플라스틱 검출기: 정수기 물 속 미세 플라스틱을 이미지 처리 AI로 분석하고 미세 플라스틱이 검출되면 검출 여부를 소비자에게 전달<br/>

### 1.2. 사업아이템 개발 배경<br/>

-   미세 플라스틱 입자 크기는 1nm ~ 5mm이다.<br/>
-   미세 플라스틱은 플라스틱 제품 생산 과정이나 플라스틱 쓰레기의 풍화작용에 의해 발생<br/>
-   플라스틱 쓰레기가 매년 증가하는 추세인 만큼, 미세 플라스틱도 함께 증가하고 있음<br/>
-   해양 속 미세 플라스틱이 해양 생물 내부를 침투하고 미세 플라스틱이 축적된 해양 생물을 우리가 먹게 되면서 체내 미세 플라스틱이 쌓이고 있음<br/>
-   대기 중에도 미세 플라스틱이 포함되어 있어서 일상생활 속에서도 피할 수 없게 됨<br/>
-   미세 플라스틱 검출 대상이 될 수 있는 범위가 넓기 때문에 정수기 물을 대상으로 사업아이템을 개발하기로 결정. 시중에 필터기를 거친 정수기 물이 안전한지 아닌지 소비자에게 알릴 수 있는 제품이 존재하지 않음<br/>
-   기존 미세 플라스틱 검출 기술(분광분석법, 열분석법)이 아닌 이미지 처리 AI와 전자 현미경만으로 빠른 검출을 할 수 있는 기술을 개발하고 이를 제품에 적용해서 소비자에게 정수기 제품의 안전성과 신뢰성을 높이도록 함<br/>

## 2. 미세 플라스틱 검출기 작업 흐름도<br/>

### 2.1. 작업 흐름도 설명<br/>

<img src="https://github.com/user-attachments/assets/43b8f99e-9d7e-4060-98b5-e554e5e3a4aa" width="550" height="400" />

① 현미경 관찰 및 데이터 수집<br/>

-   USB 디지털 현미경으로 물 속 입자들을 실시간으로 관찰하고 영상 데이터 수집<br/>
-   사용 USB 디지털 현미경 정보<br/>
    -   제품명: 스마트폰 USB 디지털 전자 현미경<br/>
    -   제품기업: DASO<br/>
    -   배율 범위: 50x - 1000x<br/>
    -   관찰 입자 크기: 1 - 10µm(1000배율)<br/>
    -   LED 여부: 있음<br/>
    -   촬영: 가능<br/>

② AI 기반 영상 처리<br/>

-   YOLOv8 기반 AI 모델로 관찰된 영상에서 미세 플라스틱 탐지<br/>
-   미세 플라스틱 탐지 결과(크기, 개수, 위치 등) 추출<br/>

③ 결과 데이터 분석<br/>

-   검출된 미세 플라스틱 데이터의 개수에 따라 미세 플라스틱 "유/무" 판별<br/>

④ 실시간 알림 전송<br/>

-   미세 플라스틱 검출 여부를 Telegram 챗봇을 통해 사용자에게 알림 전송<br/>

⑤ 사용자 조치<br/>

-   검출된 미세 플라스틱 데이터를 기반으로 정수기 필터 교체 필요성 또는 경고 알림 제공<br/>
-   사용자가 Telegram 챗봇의 알림 메시지에서 세부 데이터 확인<br/>

## 3. 기술 개발 과정<br/>

### 3.1. 기술 개발에 적용한 AI 모델 설명<br/>

#### 3.1.1 YOLOv8n 모델<br/>

-   YOLOv8 모델: 실시간 객체 탐지를 수행하는 딥러닝 기반 알고리즘<br/>
-   이미지나 동영상에서 다양한 객체를 한 번에 빠르게 탐지하는 데 사용<br/>
-   YOLOv8n 모델: YOLOv8 모델의 경량화 버전의 모델.<br/>
    -   추론 속도 빠름.<br/>
    -   정확도 떨어짐.<br/>
    -   메모리 소모 적음<br/>
-   사용 이유: USB 전자 현미경을 라즈베리파이 5세대와 연결해서 측정하기 때문에 모델의 정확도보다 경량화와 속도에 집중해야 함.<br/>

### 3.2. 모델 학습을 위한 데이터셋<br/>

-   [Kaggle의 미세 플라스틱 이미지 데이터셋](https://www.kaggle.com/code/mathieuduverne/microplastic-detection-yolov8-map-50-76-2/notebook)<br/>
-   이미지<br/>
    ![이미지1](https://github.com/user-attachments/assets/06e32137-43e5-4546-bfce-2ccdeccdaea3)
    ![이미지2](https://github.com/user-attachments/assets/a0208f4a-d6ee-4732-bc15-0b664723fe08)

### 3.3. YOLOv8n 모델 구현 및 시각화 구현 과정<br/>

(참고 자료: 링크 삽입 바람)

#### 3.3.1 모델 학습 과정<br/>

#### 3.3.2 시각화 구현<br/>

### 3.4. AI 모델 예측 결과<br/>

### 3.5 LBP(Local Binary Pattern) 미세 플라스틱 검출 모듈과 YOLOv8n 모델 간의 차이점<br/>

#### 3.5.1 LBP(Local): 이미지의 텍스처(질감)을 분석하기 위한 기법. 픽셀 주변의 밝기 변화를 기반으로 국소적 특징을 추출하는 기술<br/>

-   **작동 원리**<br/>
    -   각 픽셀을 중심으로 주변 픽셀들과 밝기 값을 비교<br/>
        -   주변 픽셀 값이 중심 픽셀보다 크거나 같으면 1, 작으면 0으로 코딩<br/>
        -   결과적으로 이진 패턴(binary pattern)을 생성하여 텍스처 정보를 표현<br/>
-   **LBP 히스토그램**<br/>
    -   생성된 LBP 이미지에서 히스토그램을 계산하여 텍스처의 분포를 정량화<br/>
    -   히스토그램은 이미지에서 특정 텍스처를 검출하는 데 사용<br/>
-   **코드에서 역할**<br/>
    -   이미지의 LBP 히스토그램을 계산하여 특정 임계값(threshold)을 초과하면 미세 플라스틱으로 간주<br/>

#### 3.5.2 CV(Computer Vision) 기반 전처리<br/>

-   **Gaussian Blur**<br/>
    -   이미지 노이즈 제거
    -   에지 감지나 텍스처 분석의 정확도 상승에 도움을 줌
-   **Canny Edge 감지**<br/>
    -   이미지에서 물체 경계를 추출하는 알고리즘<br/>
    -   두 개의 임계값을 사용하여 강한 Edge와 약한 Edge 구분<br/>
    -   미세 플라스틱 검출에서 물체의 윤곽선을 파악하는 데 사용<br/>

#### 3.5.3 윤곽선(Contour) 분석<br/>

-   **cv2.findContours**<br/>
    -   Edge 감지로 얻은 이미지를 기반으로 미세 플라스틱의 윤곽선 추출<br/>
-   **윤곽선 면적 분석**<br/>
    -   추출된 윤곽선의 면적 계산 결과로 미세플라스틱의 크기 측정<br/>
    -   면적이 작은 윤곽선 -> 노이즈, 면적이 큰 윤곽선 -> 미세 플라스틱<br/>
-   **윤곽선에 테두리 및 번호 표시**<br/>
    -   검출된 미세 플라스틱에 테두리를 그리고, 각 물체의 위치에 번호를 표시<br/>

#### 3.5.4 이미지 시각화<br/>

-   Matplotlib 시각화 라이브러리 활용<br/>
-   원본 이미지, 에지 감지 이미지 나란히 출력<br/>
-   사용자가 검출 결과를 시각적으로 확인할 수 있도록 두 이미지를 함께 출력함<br/>
-   시각화 화면<br/>
    ![결과1](https://github.com/user-attachments/assets/477d486c-aab3-48dc-a148-2fb1c2b5f19f)
    ![결과2](https://github.com/user-attachments/assets/f9291cc9-b58e-4667-9761-8884ad72ef26)

#### 3.5.5 차이점<br/>

-   LBP 기반 모듈은 YOLOv8n 기반 모듈에 비해 성능과 정확도가 떨어진다.<br/>
-   LBP 기반 모듈은 딥러닝 없이 히스토그램과 임계값 설정에 의존하는 규칙 기반 검출 방식을 사용하는 반면 YOLOv8n은 딥러닝 기술을 사용하고 실시간 처리에 특화되었기 때문에 YOLOv8n 기반 모듈이 유리하다.<br/>

## 4. 미세 플라스틱 검출 여부 전송<br/>

### 4.1. 전송 과정<br/>

### 4.2. 전송 결과 확인<br/>

## 5. 미세 플라스틱 검출기 개발 결과<br/>

### 5.1. 개발 결과<br/>
