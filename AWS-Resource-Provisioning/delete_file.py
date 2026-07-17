import boto3

# Create S3 client
s3 = boto3.client("s3")

bucket_name = "pranav-resource-provisioning-2026-01"
file_name = "sample.txt"

try:
    s3.delete_object(
        Bucket=bucket_name,
        Key=file_name
    )

    print(f"✅ '{file_name}' deleted successfully from '{bucket_name}'.")

except Exception as e:
    print("❌ Error:", e)