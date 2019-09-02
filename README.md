# CSV Analysis

Run `csv_gen.sh` in `./csv` directory to generate 5 csv files with various rows of entries.

- Run `python3 tracking.py` to analyse csv files from an OS directory, i.e. `./csv`
- `csv_lambda_test.py` is a lambda code that analyses csv files uploaded in S3 bucket
- Run `python3 tracking.py` is a lambda code that analyses csv files uploaded in S3 bucket, and scheduled with a canary event
