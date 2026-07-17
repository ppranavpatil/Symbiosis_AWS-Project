import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.describe_instances(
    InstanceIds=["i-00d7b0f10a1ebbba5"]
)

instance = response["Reservations"][0]["Instances"][0]

print("Instance ID :", instance["InstanceId"])
print("State       :", instance["State"]["Name"])

if "PublicIpAddress" in instance:
    print("Public IP   :", instance["PublicIpAddress"])
else:
    print("Public IP not assigned yet.")