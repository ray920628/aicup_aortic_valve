# AICUP 影像檢視與 YOLO 訓練專案

本專案包含兩個主要用途：

1. **模型訓練（train.ipynb）**：用於整理資料並訓練 YOLO（You Only Look Once）模型。  
2. **推論結果人工檢視（test_image_check.py）**：把 submission 文字檔中的 Bounding Box（邊界框）畫回測試圖片，並把「同一張圖有多個框」的案例另外輸出，方便人工快速檢查。

---

## 1) 環境需求

- Python 3.8+（建議 3.10）
- OpenCV（Open Source Computer Vision Library）
- NumPy（Numerical Python）

安裝（建議使用虛擬環境 Virtual Environment）：

```bash
pip install opencv-python numpy
```

> 若你會跑 `train.ipynb`，通常還會需要 PyTorch（Python Torch）、CUDA（Compute Unified Device Architecture，若使用 NVIDIA GPU）、以及 YOLO 相關套件（依你的 Notebook 內容為準）。

---

## 2) 專案檔案說明

- `train.ipynb`  
  訓練與前處理的 Jupyter Notebook（Jupyter Notebook：互動式 Python 筆記本）。

- `test_image_check.py`  
  讀取 `submission_sorted.txt`（或你指定的 txt），將每筆偵測框畫回對應圖片，並輸出：
  - **全部圖片（含框）** 到 `ALL_DIR`
  - **重複框圖片（同一張圖框數 > 1）** 到 `OUT_DIR`

---

## 3) 推論結果檢視：test_image_check.py

### 3.1 輸入資料格式（TXT）

程式預期每一行有 **7 個欄位**（以空白分隔）：

```
img_name cls score x1 y1 x2 y2
```

- `img_name`：圖片檔名（**不含副檔名**），程式會自動加上 `.png`
- `cls`：類別編號（class id）
- `score`：信心分數（confidence score）
- `(x1, y1, x2, y2)`：左上與右下座標（像素座標）

> 如果你的影像副檔名不是 `.png`（例如 `.jpg`），請到程式中把 `.png` 改掉。

### 3.2 路徑設定

在 `test_image_check.py` 最上面這段修改成你的路徑（Windows / Linux 都可）：

- `TXT_PATH`：submission txt 檔路徑  
- `IMG_DIR`：測試圖片資料夾  
- `OUT_DIR`：輸出「需要檢查（重複框）」的資料夾  
- `ALL_DIR`：輸出「所有圖片都畫框」的資料夾  

### 3.3 執行方式

```bash
python test_image_check.py
```

### 3.4 輸出結果

- `ALL_DIR/xxx.png`：每張圖都會輸出一張「已畫框」版本（即使只有一個框）
- `OUT_DIR/xxx.png`：只有當同一張圖有 **多於 1 個框** 才會輸出到這裡

---

## 4) 訓練：train.ipynb（簡要）

Notebook 主要流程通常會包含：

1. 前處理（整理資料、產生 train/val 清單、更新 data.yaml 等）
2. 訓練 YOLO（You Only Look Once）
3. 產生權重（weights）與評估結果

> 如果你希望我把 `train.ipynb` 的「執行步驟」整理成更完整的教學（例如：每個 cell 在做什麼、需要哪些檔案、資料夾結構怎麼放），你把你目前的資料夾結構貼上來，我可以直接幫你補一段「可照做」的 README 教學段落。

---

## 5) 常見問題（FAQ）

### Q1：為什麼程式會跳過某些行？
程式會檢查每行是否剛好 7 欄；不是 7 欄就會略過。

### Q2：為什麼找不到圖片？
程式預設把 `img_name` 加上 `.png` 才去找檔案；如果你的檔案副檔名不同，請修改副檔名。

### Q3：每張圖的框顏色為什麼都不一樣？
程式使用隨機顏色來區分不同框。如果你希望「同一類別固定顏色」或「可重現顏色（固定 random seed）」也可以再改。

---

## License

如無特別聲明，預設為你自用腳本用途。若你需要放到 GitHub（GitHub：原始碼代管平台）公開，建議加上 MIT License（Massachusetts Institute of Technology License）或你偏好的授權條款。
