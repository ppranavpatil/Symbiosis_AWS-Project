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

vpc = response["Vpcs"][0]

print("Default VPC ID:", vpc["VpcId"])