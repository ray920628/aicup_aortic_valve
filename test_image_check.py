import os
import cv2
import numpy as np
from collections import defaultdict

# =================== 可調整路徑 ===================
TXT_PATH = r"C:\Users\307\Desktop\aicup\submissions\submission_sorted.txt"
IMG_DIR = r"C:\Users\307\Desktop\aicup\test\images"
OUT_DIR = r"C:\Users\307\Desktop\aicup\test_image_review\need_check"
ALL_DIR = r"C:\Users\307\Desktop\aicup\test_image_review\all_label"  # ✅ 新增：全部的圖片
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(ALL_DIR, exist_ok=True)


# =================== 讀取檔案 ===================
records = defaultdict(list)
with open(TXT_PATH, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) != 7:
            continue
        img_name, cls, score, x1, y1, x2, y2 = parts
        records[img_name].append({
            "cls": int(cls),
            "score": float(score),
            "bbox": (int(x1), int(y1), int(x2), int(y2))
        })

# =================== 處理每張圖片 ===================
for img_name, boxes in records.items():
    png_name = img_name + ".png"
    img_path = os.path.join(IMG_DIR, png_name)
    if not os.path.exists(img_path):
        print(f"[WARN] 找不到圖片：{img_path}")
        continue

    img = cv2.imread(img_path)
    if img is None:
        print(f"[ERROR] 無法讀取圖片：{img_path}")
        continue

    # === 所有圖片都畫框（不論重複與否） ===
    all_img = img.copy()
    for i, box_data in enumerate(boxes):
        x1, y1, x2, y2 = box_data["bbox"]
        score = box_data["score"]
        color = tuple(np.random.randint(0, 255, size=3).tolist())
        cv2.rectangle(all_img, (x1, y1), (x2, y2), color, 2)
        label = f"{score:.4f}"
        cv2.putText(all_img, label, (x1, max(15, y1 - 5)), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, color, 1, cv2.LINE_AA)

    # ✅ 儲存全部都有框的版本
    save_all_path = os.path.join(ALL_DIR, png_name)
    cv2.imwrite(save_all_path, all_img)

    # === 額外處理重複框的版本 ===
    if len(boxes) > 1:
        save_check_path = os.path.join(OUT_DIR, png_name)
        cv2.imwrite(save_check_path, all_img)
        print(f"[OK] 重複框: {img_name} -> {save_check_path}")
    else:
        print(f"[INFO] 單框: {img_name}")

print("✅ 完成！所有圖片(含框)已輸出到 test_image，重複框圖片已輸出到 test_image_check。")