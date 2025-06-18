# StockPriceTracking

## Tracking Tesla Stock Price

This repository provides a simple script to check the latest Tesla (TSLA) stock
price along with the maximum and minimum closing prices over the last five
years. It can optionally send the update via email.


### Requirements

- Python 3
- `yfinance` (`pip install yfinance`)

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

You can schedule the script daily using `cron` or run it via GitHub Actions.

Create a workflow file at `.github/workflows/stock_update.yml` similar to the
one in this repo. The workflow installs dependencies and runs the script daily.
Add your email credentials as repository secrets so they are not exposed in the
workflow file. The `STOCK_SEND_EMAIL` secret should be set to `1`, `true`, or
`yes`.


Alternatively, schedule with `cron`:

```cron
0 9 * * * /usr/bin/python /path/to/track_tesla.py >> /path/to/tesla.log 2>&1
```

### Disclaimer

This script uses Yahoo Finance via `yfinance` and requires internet access.
Email credentials should be stored securely (for example in environment
