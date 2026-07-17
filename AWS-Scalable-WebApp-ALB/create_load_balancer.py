import boto3

elbv2 = boto3.client("elbv2", region_name="ap-south-1")

response = elbv2.create_load_balancer(
    Name="Pranav-ALB",
    Subnets=[
        "subnet-059a9fb7f016a1936",
        "subnet-0c147a65c1061a4ab"
    ],
    SecurityGroups=[
        "sg-0d87c2181f1d33159"
    ],
    Scheme="internet-facing",
    Type="application",
    IpAddressType="ipv4"
)

print("✅ Load Balancer Created Successfully!")
print("DNS Name:", response["LoadBalancers"][0]["DNSName"])
print("Load Balancer ARN:")
print(response["LoadBalancers"][0]["LoadBalancerArn"])