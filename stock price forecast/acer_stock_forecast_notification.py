import yfinance as yf
import tensorflow as tf
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

stock_code = "2353.TW"

#獲取20天歷史股價
def get_stock(stock_code):
    df = yf.Ticker(stock_code)
    df = df.history(period="3mo",interval="1d")
    df = df[-20:]
    return df["Close"].values

#預測股價
def predict_nextday_price(data):
    ann_model = tf.keras.models.load_model(r'C:\Users\tyhoo\Documents\python project\PROJECT\Time Series performance forecast\stock price forecast\ANN_time_forecast_model')
    data = np.array(data)
    data = data.reshape((1,20,1))
    predicted_price = ann_model.predict(data)
    predicted_price = round(predicted_price.item(),3)
    return predicted_price

# 發送郵件通知
def send_email(predicted_price):
    sender_email = "u109075201@cmu.edu.tw"
    receiver_email = "tyhood17@gmail.com"
    password = "cgjq vhcg aqpe gkmz"

    message = MIMEMultipart("alternative")
    message["Subject"] = "每日股價預測"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"預測的下一次交易日宏碁股價為: {predicted_price}"
    part = MIMEText(text, "plain")
    message.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
         server.login(sender_email, password)
         server.sendmail(sender_email, receiver_email, message.as_string())

# 主函數
def main():
    data = get_stock(stock_code)
    predicted_price = predict_nextday_price(data)
    send_email(predicted_price)
    print(f"預測的下一次交易日股價為: {predicted_price}")

if __name__ == "__main__":
    main()