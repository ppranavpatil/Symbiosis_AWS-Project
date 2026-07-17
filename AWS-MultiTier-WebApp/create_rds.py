import boto3

rds = boto3.client("rds", region_name="ap-south-1")

response = rds.create_db_instance(
    DBInstanceIdentifier="pranav-mysql-db",
    AllocatedStorage=20,
    DBName="pranavdb",
    Engine="mysql",
    EngineVersion="8.0",
    DBInstanceClass="db.t3.micro",
    MasterUsername="admin",
    MasterUserPassword="Pranav12345",
    VpcSecurityGroupIds=[
        "sg-043e6c8e76a3df376"
    ],
    PubliclyAccessible=False,
    BackupRetentionPeriod=0,
    MultiAZ=False,
    StorageType="gp2"
)

print("✅ RDS MySQL Instance Creation Started!")
print("DB Identifier:", response["DBInstance"]["DBInstanceIdentifier"])