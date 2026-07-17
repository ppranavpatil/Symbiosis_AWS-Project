import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

key_name = "Pranav-ALB-Key"

try:
    response = ec2.create_key_pair(KeyName=key_name)

    with open(f"{key_name}.pem", "w") as file:
        file.write(response["KeyMaterial"])

    print("✅ Key Pair Created Successfully!")
    print("Key Pair Name:", key_name)
    print(f"Private Key saved as: {key_name}.pem")

except Exception as e:
    print("❌ Error:", e)