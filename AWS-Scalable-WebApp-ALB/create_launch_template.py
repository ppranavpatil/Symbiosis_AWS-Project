import boto3
import base64

ec2 = boto3.client("ec2", region_name="ap-south-1")

user_data_script = """#!/bin/bash
dnf update -y
dnf install -y httpd
systemctl enable httpd
systemctl start httpd
echo "<h1>Hello AWS from Auto Scaling!</h1>" > /var/www/html/index.html
"""

user_data = base64.b64encode(user_data_script.encode()).decode()

response = ec2.create_launch_template(
    LaunchTemplateName="PranavLaunchTemplate",
    LaunchTemplateData={
        "ImageId": "ami-01a18c38ece67e620",
        "InstanceType": "t3.micro",
        "KeyName": "Pranav-ALB-Key",
        "SecurityGroupIds": [
            "sg-0d87c2181f1d33159"
        ],
        "UserData": user_data
    }
)

print("✅ Launch Template Created Successfully!")
print("Launch Template ID:", response["LaunchTemplate"]["LaunchTemplateId"])