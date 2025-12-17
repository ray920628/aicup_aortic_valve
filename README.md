
# Test Image Review Tool

## 用途說明
此工具用於將物件偵測（Object Detection）的 submission 結果畫回原始圖片，
並快速找出 **同一張圖片出現多個 bounding box** 的情況，方便人工檢查。

---

## 環境安裝

### Python 版本
- Python 3.8 以上

### 套件安裝
```bash
pip install opencv-python numpy
```

---

## 使用流程（流程圖）

```text
submission.txt
      │
      ▼
讀取每一行預測結果
      │
      ▼
依 image_name 分組 bounding box
      │
      ▼
讀取對應圖片 (.png)
      │
      ▼
在圖片上畫 bounding box + score
      │
      ├─► 存到 all_label/
      │
      ▼
若同一張圖有多個框
      │
      └─► 另外存到 need_check/
```

---

## 資料格式說明

### submission txt 格式（每行 7 欄）
```text
image_name class_id score x1 y1 x2 y2
```

範例：
```text
000001 0 0.8734 120 45 260 180
```

---

## 輸出資料夾

- `all_label/`  
  所有圖片都會輸出，並畫上預測框

- `need_check/`  
  只包含 **同一張圖片有兩個以上 bounding box** 的圖片

---

## 路徑設定（必改）

請在程式最上方修改：
```python
TXT_PATH = r"...submission_sorted.txt"
IMG_DIR  = r"...test/images"
OUT_DIR  = r"...need_check"
ALL_DIR  = r"...all_label"
```

---

## 備註
- 本工具 **不做 NMS（Non-Maximum Suppression，非極大值抑制）**
- 目的為協助人工檢查模型輸出是否異常
