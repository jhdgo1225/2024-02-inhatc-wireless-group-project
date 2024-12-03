import pandas as pd
import os

# CSV 파일 경로
csv_file = './dataset/images/valid/_annotations.csv'

# 이미지와 라벨 파일이 저장될 디렉토리
image_dir = './dataset/images/valid'
label_dir = './dataset/labels/valid'

# 클래스 이름과 해당 번호 매핑
class_name_to_id = {'Microplastic': 0}

# 라벨 디렉토리가 없으면 생성
os.makedirs(label_dir, exist_ok=True)

# CSV 파일 읽기
df = pd.read_csv(csv_file)

# 각 이미지에 대해 라벨 파일 생성
for filename, group in df.groupby('filename'):
    # 이미지 크기
    image_width = group.iloc[0]['width']
    image_height = group.iloc[0]['height']
    
    # YOLO 형식의 라벨 내용
    yolo_labels = []
    for _, row in group.iterrows():
        class_name = row['class']
        class_id = class_name_to_id[class_name]
        
        # 바운딩 박스 좌표
        xmin = row['xmin']
        ymin = row['ymin']
        xmax = row['xmax']
        ymax = row['ymax']
        
        # 중심 좌표와 너비, 높이 계산 및 정규화
        x_center = (xmin + xmax) / 2.0 / image_width
        y_center = (ymin + ymax) / 2.0 / image_height
        width = (xmax - xmin) / image_width
        height = (ymax - ymin) / image_height
        
        # YOLO 형식: 클래스 번호, x_center, y_center, width, height
        yolo_labels.append(f"{class_id} {x_center} {y_center} {width} {height}")
    
    # 라벨 파일 경로
    label_file = os.path.join(label_dir, os.path.splitext(filename)[0] + '.txt')
    
    # 라벨 파일 저장
    with open(label_file, 'w') as f:
        f.write('\n'.join(yolo_labels))
