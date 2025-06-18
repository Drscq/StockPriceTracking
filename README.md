# StockPriceTracking

## Tracking Tesla Stock Price

This repository provides a simple script to check the latest Tesla (TSLA) stock
price along with the maximum and minimum closing prices over the last five
years.

### Requirements

- Python 3
- `yfinance` (`pip install yfinance`)
- `twilio` (`pip install twilio`) if you want SMS notifications

### Usage

Run the script to print the stock update:

```bash
python track_tesla.py
```

To send the update via email, set the following environment variables and enable
email sending:

```bash
export STOCK_EMAIL_SENDER=your_email@example.com
export STOCK_EMAIL_RECEIVER=destination_email@example.com
export STOCK_EMAIL_PASSWORD=your_email_password
export STOCK_SEND_EMAIL=1  # accepts "1", "true", or "yes"
python track_tesla.py
```

To send the update via SMS using Twilio, set these variables:

```bash
export TWILIO_ACCOUNT_SID=your_account_sid
export TWILIO_AUTH_TOKEN=your_auth_token
export TWILIO_FROM_NUMBER=+1234567890
export TWILIO_TO_NUMBER=+1234567890
export STOCK_SEND_SMS=1  # accepts "1", "true", or "yes"
python track_tesla.py
```

You can schedule the script daily using `cron` or run it via GitHub Actions.

Create a workflow file at `.github/workflows/stock_update.yml` similar to the
one in this repo. The workflow installs dependencies and runs the script daily.
Add your email or Twilio credentials as repository secrets so they are not
exposed in the workflow file. Boolean secrets such as `STOCK_SEND_EMAIL` or
`STOCK_SEND_SMS` should be set to `1`, `true`, or `yes`.

Alternatively, schedule with `cron`:

```cron
0 9 * * * /usr/bin/python /path/to/track_tesla.py >> /path/to/tesla.log 2>&1
```

### Disclaimer

This script uses Yahoo Finance via `yfinance` and requires internet access.
Email and SMS credentials should be stored securely (for example in environment
variables or GitHub secrets) and never committed to the repository.
