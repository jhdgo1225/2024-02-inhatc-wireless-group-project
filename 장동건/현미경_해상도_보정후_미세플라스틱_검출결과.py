# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gNkP8lIquPrBO81MtGnkXVYyIJDXBQ4O
"""

import cv2
import numpy as np
from skimage.feature import local_binary_pattern
import imageio  # imageio로 이미지를 읽습니다
import matplotlib.pyplot as plt
from google.colab import files
import io

# LBP 히스토그램 계산 함수
def calculate_lbp_histogram(image, radius=1, n_points=8):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp_image = local_binary_pattern(gray_image, n_points, radius, method="uniform")
    lbp_hist, _ = np.histogram(lbp_image.ravel(), bins=np.arange(0, n_points + 3), range=(0, n_points + 2))
    lbp_hist = lbp_hist.astype('float')
    lbp_hist /= lbp_hist.sum()
    return lbp_hist, lbp_image

# 이미지 전처리 및 에지 감지
def preprocess_image(image_path):
    image = imageio.imread(image_path)  # imageio로 이미지 읽기

    # 이미지 크기 출력
    height, width, channels = image.shape
    print(f"이미지 크기: {width}x{height}, 채널 수: {channels}")

    # Gaussian Blur로 노이즈 제거
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Canny 에지 감지: 임계값을 낮추어 더 세밀한 에지 추출
    edges = cv2.Canny(blurred_image, 50, 150)

    return image, edges

# 미세플라스틱 검출 예시
def detect_microplastics(image_path):
    original_image, edges = preprocess_image(image_path)
    lbp_hist, lbp_image = calculate_lbp_histogram(original_image)

    # LBP 히스토그램 분석
    threshold = 0.05
    if np.any(lbp_hist > threshold):
        print(f"이미지 {image_path}에서 미세플라스틱을 검출했습니다.")
    else:
        print(f"이미지 {image_path}에서 미세플라스틱을 검출하지 못했습니다.")

    # 에지 감지된 이미지에서 윤곽선 찾기
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 미세플라스틱의 개수와 사이즈 출력
    num_microplastics = len(contours)
    print(f"검출된 미세플라스틱의 개수: {num_microplastics}")

    # 각 미세플라스틱의 크기(면적) 계산
    areas = [cv2.contourArea(cnt) for cnt in contours]
    print(f"각 미세플라스틱의 크기 (면적): {areas}")

    # 미세플라스틱 검출 위치에 파란색 테두리 그리기
    result_image = original_image.copy()
    for idx, contour in enumerate(contours):
        # 윤곽선의 면적이 일정 크기 이상인 경우만 테두리 표시
        area = cv2.contourArea(contour)
        print(f"Contour {idx+1} - 면적: {area}px")
        if area > 5:  # 면적 기준을 5로 설정하여 더 작은 물체도 검출
            cv2.drawContours(result_image, [contour], -1, (255, 0, 0), 2)  # 파란색 테두리
            # 각 미세플라스틱 번호 표시
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(result_image, str(idx+1), (cX-10, cY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # 원본 이미지와 에지 감지된 이미지를 나란히 출력
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))  # 1행 2열로 배치
    axes[0].imshow(result_image)
    axes[0].set_title(f"Original Image with Contours: {image_path}")
    axes[0].axis('off')  # 축 숨기기

    axes[1].imshow(edges, cmap='gray')
    axes[1].set_title(f"Edge Detection: {image_path}")
    axes[1].axis('off')  # 축 숨기기

    plt.tight_layout()  # 레이아웃 조정
    plt.show()

# 로컬 파일 업로드
uploaded = files.upload()

# 업로드된 이미지 파일 이름
image_path = next(iter(uploaded))

# 미세플라스틱 검출
detect_microplastics(image_path)