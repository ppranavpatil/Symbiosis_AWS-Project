import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.describe_instances()

print("EC2 Instances:\n")

found = False

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        found = True
        print("Instance ID :", instance["InstanceId"])
        print("State       :", instance["State"]["Name"])
        print("Type        :", instance["InstanceType"])
        print("----------------------------")

if not found:
    print("No EC2 instances found.")