import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.describe_images(
    Owners=["amazon"],
    Filters=[
        {
            "Name": "architecture",
            "Values": ["x86_64"]
        },
        {
            "Name": "state",
            "Values": ["available"]
        }
    ]
)

images = sorted(response["Images"], key=lambda x: x["CreationDate"], reverse=True)

for image in images[:20]:
    name = image.get("Name", "")
    if "al2023" in name.lower():
        print("AMI ID:", image["ImageId"])
        print("AMI Name:", name)
        break