import cv2
from ultralytics import YOLO

# 학습된 모델 로드
model = YOLO('./runs/detect/train/weights/best.pt')

# 카메라 초기화
cap = cv2.VideoCapture(0)  # 0은 기본 카메라를 의미합니다.

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 가져올 수 없습니다.")
        break

    # 예측 수행
    results = model(frame)

    if len(results[0].boxes) == 0:
        print("탐지된 객체가 없습니다.")
        continue

    boxes = results[0].boxes.xyxy.cpu().numpy()  # 경계 상자 좌표
    scores = results[0].boxes.conf.cpu().numpy()  # 신뢰도 점수
    class_ids = results[0].boxes.cls.cpu().numpy().astype(int)  # 클래스 ID
    class_names = results[0].names  # 클래스 이름

    # 각 객체에 대해 경계 상자, 레이블, 신뢰도 점수 그리기
    for box, score, class_id in zip(boxes, scores, class_ids):
        x1, y1, x2, y2 = map(int, box)
        label = f"{class_names[class_id]}: {score:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 미세플라스틱의 갯수와 면적 비율 출력
    num_objects = len(boxes)
    total_area = sum((x2 - x1) * (y2 - y1) for x1, y1, x2, y2 in boxes)
    frame_area = frame.shape[0] * frame.shape[1]
    area_ratio = (total_area / frame_area) * 100
    print(f"탐지된 미세플라스틱의 갯수: {num_objects}")
    print(f"미세플라스틱이 차지한 면적 비율: {area_ratio:.2f}%")

    # 결과 이미지 표시
    cv2.imshow("Detection Result", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 카메라 및 윈도우 해제
cap.release()
cv2.destroyAllWindows()