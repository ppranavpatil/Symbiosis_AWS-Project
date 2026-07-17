import boto3

# Create S3 client
s3 = boto3.client("s3")

# Bucket name
bucket_name = "pranav-resource-provisioning-2026-01"

# File names
file_name = "sample.txt"

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print(f"✅ '{file_name}' uploaded successfully to '{bucket_name}'.")

except Exception as e:
    print("❌ Error:", e)