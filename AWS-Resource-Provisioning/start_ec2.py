import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

instance_id = "i-0756b29056f519d1b"

print("Starting EC2 Instance...")

response = ec2.start_instances(
    InstanceIds=[instance_id]
)

print(response)