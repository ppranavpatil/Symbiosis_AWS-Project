import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.describe_security_groups()

print("All Security Groups:\n")

for sg in response["SecurityGroups"]:
    print("Name :", sg["GroupName"])
    print("ID   :", sg["GroupId"])
    print("VPC  :", sg["VpcId"])
    print("-" * 40)