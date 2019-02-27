# export-spreadsheet

## before settings

- KMS
  - create KMS key
- Secret Manager
  - set googleapi service account credential json

## deploy

- upload source and layer to s3 bucket
- replace cfn.yml (S3Bucket/S3Key/CodeUri)
- run cfn.yml
