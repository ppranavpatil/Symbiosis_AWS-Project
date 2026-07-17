import boto3

rds = boto3.client("rds", region_name="ap-south-1")

response = rds.describe_db_instances()

for db in response["DBInstances"]:
    print("DB Identifier :", db["DBInstanceIdentifier"])
    print("Status        :", db["DBInstanceStatus"])
    print("Engine        :", db["Engine"])
    print("Endpoint      :", db.get("Endpoint", {}).get("Address", "Not Available Yet"))
    print("-" * 40)