# 測試影像檢視與重複框檢查工具

本專案用於 **快速檢視目標偵測（Object Detection，全名：Object Detection）提交結果**，
將預測框（Bounding Box，全名：Bounding Box）直接畫在測試影像上，
並 **自動分離出「有重複框的圖片」以利人工檢查**。

適合用於比賽（如 AICUP）或模型推論後的結果審查階段。

---

## 一、功能說明

此工具會完成以下工作流程：

1. 讀取模型輸出的 `submission_sorted.txt`
2. 依圖片名稱彙整所有預測框
3. 將 **所有圖片** 都畫上預測框並輸出
4. 若某張圖片 **預測框數量 > 1（重複框）**，則額外輸出到指定資料夾
5. 每個框會顯示其信心分數（Confidence Score，全名：Confidence Score）

---

## 二、資料格式需求

### 1️⃣ 預測結果文字檔（TXT）格式

`submission_sorted.txt` 每一行需為 **7 個欄位**：

```
image_name class_id score x1 y1 x2 y2
```

範例：

```
000123 0 0.8734 120 85 260 310
```

欄位說明：

| 欄位 | 說明 |
|----|----|
| image_name | 圖片檔名（不含副檔名） |
| class_id | 類別編號 |
| score | 預測信心分數 |
| x1, y1 | Bounding Box 左上角座標 |
| x2, y2 | Bounding Box 右下角座標 |

---

## 三、資料夾結構建議

```
project/
├─ submission_sorted.txt
├─ test/
│  └─ images/
│     ├─ 000001.png
│     ├─ 000002.png
│     └─ ...
├─ test_image_review/
│  ├─ all_label/        # 所有圖片（皆已畫框）
│  └─ need_check/       # 僅包含「重複框」圖片
└─ test_image_check.py
```

---

## 四、程式中可調整參數

在 `test_image_check.py` 開頭可直接修改路徑：

```python
TXT_PATH = r"...\submission_sorted.txt"
IMG_DIR = r"...\test\images"
OUT_DIR = r"...\test_image_review\need_check"
ALL_DIR = r"...\test_image_review\all_label"
```

⚠️ **圖片副檔名預設為 `.png`，如非 PNG 請自行修改程式。**

---

## 五、輸出結果說明

### ✅ all_label 資料夾
- **每一張圖片**
- 已畫上所有預測框
- 框上標示信心分數

### ⚠️ need_check 資料夾
- **僅包含有兩個（含）以上預測框的圖片**
- 用於人工檢查是否有誤檢、多檢問題

---

## 六、使用情境建議

- 比賽提交前的 **品質檢查（Quality Control，全名：Quality Control）**
- 分析模型是否在特定影像產生過多預測
- 快速定位後處理（Post-processing，全名：Post-processing）需優化的樣本

---

## 七、相依套件（Requirements）

```bash
pip install opencv-python numpy
```

Python 建議版本：**Python 3.8 以上**

---

## 八、注意事項

- 本工具 **不會做 Non-Maximum Suppression（非極大值抑制，Non-Maximum Suppression）**
- 若你希望只保留最佳框，需在模型端或後處理階段完成
- 框的顏色為隨機顏色，僅供視覺區分

---

## 九、作者備註

這是一個 **實務導向的檢視工具**，目的不是漂亮，而是讓你 **一眼看到模型哪裡出問題**。
如果你後面要加上：
- IoU（Intersection over Union，全名：Intersection over Union）分析
- 類別統計
- 自動標記可疑樣本

這份程式都很適合當基底擴充。

---

✅ 如果你需要 **Markdown + 圖例版 README**、或要改成 **CLI 參數形式**，我可以直接幫你升級。
