import boto3

elbv2 = boto3.client("elbv2", region_name="ap-south-1")

TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:ap-south-1:789738610714:targetgroup/PranavTargetGroup/e9233d7c2efe00d0"

INSTANCE_ID = "i-04eeffa41a061f0bd"

response = elbv2.register_targets(
    TargetGroupArn=TARGET_GROUP_ARN,
    Targets=[
        {
            "Id": INSTANCE_ID,
            "Port": 80
        }
    ]
)

print("✅ EC2 Instance Registered Successfully!")