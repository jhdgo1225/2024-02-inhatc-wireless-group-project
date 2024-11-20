import cv2
from ultralytics import YOLO

# 학습된 모델 로드
model = YOLO('./runs/detect/train/weights/best.pt')

# 예측할 이미지 경로
image_path = "./image3.jpg"

# 이미지 읽기
image = cv2.imread(image_path)

# 예측 수행
results = model(image)
print(results)

if len(results[0].boxes) == 0:
    print("탐지된 객체가 없습니다.")
    exit(1)

boxes = results[0].boxes.xyxy.cpu().numpy()  # 경계 상자 좌표
scores = results[0].boxes.conf.cpu().numpy()  # 신뢰도 점수
class_ids = results[0].boxes.cls.cpu().numpy().astype(int)  # 클래스 ID
class_names = results[0].names  # 클래스 이름

# 각 객체에 대해 정보 출력
for box, score, class_id in zip(boxes, scores, class_ids):
    x1, y1, x2, y2 = map(int, box)
    label = class_names[class_id]
    print(f"클래스: {label}, 신뢰도: {score:.2f}, 좌표: ({x1}, {y1}), ({x2}, {y2})")


# 각 객체에 대해 경계 상자, 레이블, 신뢰도 점수 그리기
for box, score, class_id in zip(boxes, scores, class_ids):
    x1, y1, x2, y2 = map(int, box)
    label = f"{class_names[class_id]}: {score:.2f}"
    print(f"탐지된 객체: {label}, 위치: ({x1}, {y1}), ({x2}, {y2})")
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 결과 이미지 표시
cv2.imshow("Detection Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
