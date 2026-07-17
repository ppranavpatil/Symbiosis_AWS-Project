import boto3

print("Program Started")

s3 = boto3.client("s3", region_name="ap-south-1")

bucket_name = "pranav-resource-provisioning-2026-01"

try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": "ap-south-1"
        }
    )

    print("Bucket created successfully!")
    print(response)

except Exception as e:
    print("Error:", e)

print("Program Finished")