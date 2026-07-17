import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

response = ec2.run_instances(
    ImageId="ami-01a18c38ece67e620",   # Change if your AMI is different
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="pranav-key-new",
    SecurityGroupIds=[
        "sg-093e2a72c4ac01aa9"
    ],
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Pranav-MultiTier-WebServer"
                }
            ]
        }
    ],
    UserData="""#!/bin/bash
yum update -y
yum install -y httpd php php-mysqlnd

systemctl start httpd
systemctl enable httpd

echo "<h1>Pranav Multi-Tier Web Application</h1>" > /var/www/html/index.html
"""
)

instance_id = response["Instances"][0]["InstanceId"]

print("✅ EC2 Instance Created Successfully!")
print("Instance ID:", instance_id)