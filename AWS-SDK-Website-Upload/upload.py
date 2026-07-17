import boto3
import mimetypes

bucket_name = "aws-sdk-website-upload-pranav"

s3 = boto3.client("s3")

files = ["index.html", "style.css"]

for file in files:
    content_type = mimetypes.guess_type(file)[0]

    s3.upload_file(
        file,
        bucket_name,
        file,
        ExtraArgs={
            "ContentType": content_type
        }
    )

    print(f"Uploaded {file} ({content_type})")

print("Website uploaded successfully!")