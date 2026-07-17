import boto3

elbv2 = boto3.client("elbv2", region_name="ap-south-1")

response = elbv2.describe_load_balancers()

for lb in response["LoadBalancers"]:
    print("Name :", lb["LoadBalancerName"])
    print("ARN  :", lb["LoadBalancerArn"])
    print("DNS  :", lb["DNSName"])
    print("-" * 60)