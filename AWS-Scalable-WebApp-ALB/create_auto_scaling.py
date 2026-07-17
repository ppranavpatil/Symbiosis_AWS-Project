import boto3

autoscaling = boto3.client("autoscaling", region_name="ap-south-1")

response = autoscaling.create_auto_scaling_group(
    AutoScalingGroupName="PranavAutoScalingGroup",

    LaunchTemplate={
        "LaunchTemplateId": "lt-0837a265f7524f4c9",
        "Version": "$Latest"
    },

    MinSize=1,
    MaxSize=2,
    DesiredCapacity=1,

    VPCZoneIdentifier="subnet-059a9fb7f016a1936,subnet-0c147a65c1061a4ab",

    TargetGroupARNs=[
        "arn:aws:elasticloadbalancing:ap-south-1:789738610714:targetgroup/PranavTargetGroup/e9233d7c2efe00d0"
    ],

    HealthCheckType="ELB",
    HealthCheckGracePeriod=300
)

print("✅ Auto Scaling Group Created Successfully!")