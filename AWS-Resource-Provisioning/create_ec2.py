import boto3

# Connect to EC2
ec2 = boto3.resource("ec2", region_name="ap-south-1")

print("Creating EC2 Instance...")

instances = ec2.create_instances(
    ImageId="ami-01a18c38ece67e620",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="pranav-key",
    SecurityGroupIds=["sg-093e2a72c4ac01aa9"],
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Pranav-Boto3-Instance"
                }
            ]
        }
    ]
)

instance = instances[0]

print("Instance is being created...")
print("Instance ID:", instance.id)