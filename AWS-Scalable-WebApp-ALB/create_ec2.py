import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

UserData = """#!/bin/bash
dnf update -y
dnf install -y httpd
systemctl enable httpd
systemctl start httpd
echo "<h1>Hello AWS from Pranav!</h1>" > /var/www/html/index.html
"""

print("Creating EC2 Instance...")

response = ec2.run_instances(
    ImageId='ami-01a18c38ece67e620',
    InstanceType='t3.micro',
    KeyName='Pranav-ALB-Key',
    SecurityGroupIds=['sg-0d87c2181f1d33159'],
    UserData=UserData,
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Pranav-Web-Server'
                }
            ]
        }
    ]
)

instance_id = response['Instances'][0]['InstanceId']

print("EC2 Instance Created Successfully!")
print("Instance ID:", instance_id)