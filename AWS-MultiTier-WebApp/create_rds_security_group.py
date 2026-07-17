import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.create_security_group(
    GroupName="pranav-rds-sg",
    Description="Security Group for RDS MySQL",
    VpcId="vpc-0cb0eb05dd55437cc"
)

rds_sg_id = response["GroupId"]

print("✅ RDS Security Group Created Successfully!")
print("RDS Security Group ID:", rds_sg_id)

ec2.authorize_security_group_ingress(
    GroupId=rds_sg_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 3306,
            "ToPort": 3306,
            "UserIdGroupPairs": [
                {
                    "GroupId": "sg-093e2a72c4ac01aa9"
                }
            ]
        }
    ]
)

print("✅ MySQL (3306) rule added successfully!")