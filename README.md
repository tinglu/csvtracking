# CSV Analysis

Run locally:

- Run `csv_gen.sh` in `./csv` directory to generate 5 csv files with various rows of entries.
- Run `python3 tracking.py` to analyse csv files from an OS directory, i.e. `./csv`

Lambda:

- `csv_lambda_test.py` is a lambda code that analyses csv files uploaded in S3 bucket
- `csv_lambda_canary_test.py` is similar to the above, and can be triggered by a scheduled canary event
