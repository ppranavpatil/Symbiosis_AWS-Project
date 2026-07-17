import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.describe_vpcs(
    Filters=[
        {
            "Name": "isDefault",
            "Values": ["true"]
        }
    ]
)

print("Default VPC ID:")
print(response["Vpcs"][0]["VpcId"])