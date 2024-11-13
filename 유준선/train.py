from ultralytics import YOLO
import torch
import time

def main():
    # GPU 사용 가능 여부 확인
    if torch.cuda.is_available():
        device = '0'  # 첫 번째 GPU 사용
        print("GPU를 사용하여 학습을 진행합니다.")
    else:
        device = 'cpu'
        print("CPU를 사용하여 학습을 진행합니다.")

    # YOLOv8 모델 생성
    model = YOLO('yolov8n.pt')

    # 학습 시작 시간 기록
    start_time = time.time()

    # 모델 학습 (device 설정)
    model.train(data="microplastic.yaml", epochs=50, imgsz=640, device=device)

    # 학습 종료 시간 기록
    end_time = time.time()

    # 학습에 걸린 시간 계산 (초 단위)
    elapsed_time = end_time - start_time
    print(f"학습에 걸린 시간: {elapsed_time:.2f}초")

    # 시간을 시, 분, 초로 변환하여 출력
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print(f"학습에 걸린 시간: {int(hours)}시간 {int(minutes)}분 {int(seconds)}초")

if __name__ == '__main__':
    main()
