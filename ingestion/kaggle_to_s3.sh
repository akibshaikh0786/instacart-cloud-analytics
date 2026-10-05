#!/bin/bash
# Kaggle -> AWS CloudShell -> S3 ingestion for Instacart dataset
# NOTE: Set the Kaggle token separately in ~/.kaggle/access_token (never commit it)

pip install kaggle -q

kaggle datasets download -d psparks/instacart-market-basket-analysis

# Stream each CSV from the zip straight into S3 (no unzip on disk)
for f in aisles departments products orders order_products__train order_products__prior; do
  echo "uploading $f ..."
  unzip -p instacart-market-basket-analysis.zip $f.csv | aws s3 cp - s3://instacart-project-akib-2026/raw/$f.csv
done

aws s3 ls s3://instacart-project-akib-2026/raw/ --human-readable
