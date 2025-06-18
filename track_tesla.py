import os
import yfinance as yf
import smtplib
from email.mime.text import MIMEText

def _env_flag(name: str) -> bool:
    """Return True if the environment variable is set to a truthy value."""
    val = os.environ.get(name, "").lower()
    return val in {"1", "true", "yes"}

# Fetch last 5 years of Tesla (TSLA) data
# Use period='5y' for last 5 years

def get_stock_data():
    # auto_adjust=False ensures the columns are simple floats with the usual
    # Open/High/Low/Close/Volume structure
    data = yf.download(
        'TSLA', period='5y', auto_adjust=False, multi_level_index=False
    )
    if data.empty:
        raise ValueError('No data fetched for TSLA')
    close_series = data['Close']
    latest_close = float(close_series.iloc[-1])
    latest_date = data.index[-1].strftime('%Y-%m-%d')
    max_price = float(close_series.max())
    min_price = float(close_series.min())
    return latest_date, latest_close, max_price, min_price


def compose_message(latest_date, latest_close, max_price, min_price):
    message = (
        f"Tesla Stock Price Update for {latest_date}\n"
        f"Latest Close Price: ${latest_close:.2f}\n"
        f"5-Year Max Price: ${max_price:.2f}\n"
        f"5-Year Min Price: ${min_price:.2f}\n"
    )
    return message


def send_email(subject, body):
    sender = os.environ.get('STOCK_EMAIL_SENDER')
    receiver = os.environ.get('STOCK_EMAIL_RECEIVER')
    password = os.environ.get('STOCK_EMAIL_PASSWORD')
    if not all([sender, receiver, password]):
        print('Email credentials not fully set; skipping email.')
        return False

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)
    return True


if __name__ == '__main__':
    send_mail = _env_flag('STOCK_SEND_EMAIL')
    main(send_mail)