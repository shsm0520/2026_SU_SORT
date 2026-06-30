import os
import csv

def read_default_list():
    """공용 폴더나 현재 폴더에서 외부 데이터 파일을 찾아 정수 리스트로 반환"""
    candidates = ['list.csv', 'list.md', 'list.txt']
    
    for file_name in candidates:
        if os.path.exists(file_name):
            try:
                # 1. CSV 파일 처리
                if file_name.endswith('.csv'):
                    with open(file_name, 'r', encoding='utf-8') as f:
                        reader = csv.reader(f)
                        for row in reader:
                            return [int(x) for x in row if x.strip().isdigit()]
                
                # 2. MD 또는 TXT 파일 처리 (공백, 줄바꿈 기준 쪼개기)
                else:
                    with open(file_name, 'r', encoding='utf-8') as f:
                        content = f.read()
                        return [int(x) for x in content.split() if x.strip().isdigit()]
            except Exception as e:
                print(f"⚠️ {file_name} 읽기 실패: {e}")
                
    # 3. 모든 파일이 없을 때 제공할 최후의 기본 배열
    return [1, 2, 3, 4, 5, 6, 7, 8, 11, 9, 10]