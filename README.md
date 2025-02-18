# 📈 Acer Stock Price Forecast & Email Notification

## 📖 專案介紹
本專案使用 **TensorFlow、yFinance** 來 **預測宏碁 (2353.TW) 的股價**，並透過 **Email 通知** 預測結果。該系統每天自動獲取最新的 **20 天歷史股價**，使用 **人工神經網路（ANN）** 進行股價預測，然後發送 Email 告知用戶預測結果。

---

## 🚀 **使用技術**
### 📊 **股價數據獲取**
- **yFinance**：從 Yahoo Finance 獲取 Acer (2353.TW) **最近 20 天的股價數據**。

### 🤖 **深度學習模型**
- **TensorFlow + Keras**：
  - 採用 **人工神經網路（ANN）** 進行時間序列預測。
  - **輸入**：最近 20 天的股價。
  - **輸出**：預測 **下一個交易日的股價**。

### 📡 **Email 通知**
- **smtplib**：透過 **Gmail SMTP** 伺服器發送 Email，將預測結果通知用戶。

---

## 📦 **環境與依賴**
請確保你的環境具備以下軟體：
- Python 3.9+
- TensorFlow 2.x
- yFinance（獲取股價數據）
- smtplib（發送 Email）

📌 **安裝 Python 依賴**
```bash
pip install tensorflow yfinance numpy
