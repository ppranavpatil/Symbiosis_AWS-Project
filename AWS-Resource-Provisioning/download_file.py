import boto3

# Create S3 client
s3 = boto3.client("s3")

bucket_name = "pranav-resource-provisioning-2026-01"

s3_file = "sample.txt"
local_file = "downloaded_sample.txt"

try:
    s3.download_file(bucket_name, s3_file, local_file)
    print(f"✅ '{s3_file}' downloaded successfully as '{local_file}'.")

except Exception as e:
    print("❌ Error:", e)