import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

VPC_ID = "vpc-0cb0eb05dd55437cc"

# Create EC2 Security Group
ec2_sg = ec2.create_security_group(
    GroupName="Pranav-EC2-SG",
    Description="Security Group for EC2 Web Server",
    VpcId=VPC_ID
)

EC2_SG_ID = ec2_sg["GroupId"]

print("✅ EC2 Security Group Created")
print("EC2 SG ID:", EC2_SG_ID)

# Allow SSH
ec2.authorize_security_group_ingress(
    GroupId=EC2_SG_ID,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }
    ]
)

# Allow HTTP
ec2.authorize_security_group_ingress(
    GroupId=EC2_SG_ID,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }
    ]
)

# Create RDS Security Group
rds_sg = ec2.create_security_group(
    GroupName="Pranav-RDS-SG",
    Description="Security Group for RDS Database",
    VpcId=VPC_ID
)

RDS_SG_ID = rds_sg["GroupId"]

print("\n✅ RDS Security Group Created")
print("RDS SG ID:", RDS_SG_ID)