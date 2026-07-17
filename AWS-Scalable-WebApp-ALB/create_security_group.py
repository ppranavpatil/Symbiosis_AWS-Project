import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.create_security_group(
    GroupName="Pranav-ALB-SG",
    Description="Security Group for ALB Project",
    VpcId="vpc-0cb0eb05dd55437cc"
)

sg_id = response["GroupId"]

print("Security Group Created Successfully!")
print("Security Group ID:", sg_id)

# Allow SSH (22)
ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }
    ]
)

# Allow HTTP (80)
ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }
    ]
)

# Allow HTTPS (443)
ec2.authorize_security_group_ingress(
    GroupId=sg_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 443,
            "ToPort": 443,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }
    ]
)

print("SSH, HTTP and HTTPS rules added successfully!")