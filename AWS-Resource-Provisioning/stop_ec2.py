import boto3

INSTANCE_ID = "i-0756b29056f519d1b"

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.stop_instances(
    InstanceIds=[INSTANCE_ID]
)

print("Stopping EC2 Instance...")
print(response)