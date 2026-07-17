import boto3

elbv2 = boto3.client("elbv2", region_name="ap-south-1")

LOAD_BALANCER_ARN = "arn:aws:elasticloadbalancing:ap-south-1:789738610714:loadbalancer/app/Pranav-ALB/0d194a32569b63e5"

TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:ap-south-1:789738610714:targetgroup/PranavTargetGroup/e9233d7c2efe00d0"

response = elbv2.create_listener(
    LoadBalancerArn=LOAD_BALANCER_ARN,
    Protocol="HTTP",
    Port=80,
    DefaultActions=[
        {
            "Type": "forward",
            "TargetGroupArn": TARGET_GROUP_ARN
        }
    ]
)

print("✅ Listener Created Successfully!")
print("Listener ARN:")
print(response["Listeners"][0]["ListenerArn"])