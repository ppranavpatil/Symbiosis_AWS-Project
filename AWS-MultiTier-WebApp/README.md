# AWS Multi-Tier Web Application using Amazon EC2 & Amazon RDS

## 📌 Project Overview

This project demonstrates how to build a simple multi-tier web application on AWS.

The frontend is hosted on an Amazon EC2 instance using Apache and PHP, while the backend uses Amazon RDS (MySQL). Python (Boto3) is used to automate the creation of AWS resources.

---

## 🚀 AWS Services Used

- Amazon EC2
- Amazon RDS (MySQL)
- Amazon VPC
- Security Groups
- AWS IAM
- Python (Boto3)
- AWS CLI
- Apache HTTP Server
- PHP

---

## ✨ Features

- Create EC2 Instance using Python
- Create Amazon RDS MySQL Database
- Create RDS Security Group
- Configure Network Security
- Install Apache and PHP
- Connect PHP Application with Amazon RDS
- Verify Database Connectivity

---

## 📂 Project Structure

```text
AWS-MultiTier-WebApp/
│── create_ec2.py
│── create_rds.py
│── create_rds_security_group.py
│── get_public_ip.py
│── get_vpc.py
│── list_rds.py
│── db.php
│── requirements.txt
│── README.md
└── images/
    ├── Screenshot 2026-07-17 001235.png
    └── Screenshot 2026-07-17 010325.png
```

---

## ⚙️ Prerequisites

- AWS Account
- Python 3.x
- AWS CLI
- Boto3

Install Boto3

```bash
pip install boto3
```

Configure AWS CLI

```bash
aws configure
```

---

## ▶️ Project Workflow

### Step 1

Create RDS Security Group

```bash
python create_rds_security_group.py
```

### Step 2

Create Amazon RDS Database

```bash
python create_rds.py
```

### Step 3

Check RDS Status

```bash
python list_rds.py
```

### Step 4

Create EC2 Instance

```bash
python create_ec2.py
```

### Step 5

Get Public IP

```bash
python get_public_ip.py
```

### Step 6

Connect to EC2

```bash
ssh -i "your-key.pem" ec2-user@<Public-IP>
```

### Step 7

Install Apache and PHP

```bash
sudo dnf install -y httpd php php-mysqli
sudo systemctl enable httpd
sudo systemctl start httpd
```

### Step 8

Configure Database Connection

Edit the `db.php` file and enter your RDS endpoint, username, and password.

---

## 🏗️ Architecture

```text
              User
                │
                ▼
      Amazon EC2 (Apache + PHP)
                │
                ▼
      Amazon RDS (MySQL Database)
```

---

## 📸 Screenshots

### Amazon RDS Database

![Amazon RDS](images/Screenshot%202026-07-17%20001235.png)

---

### Successful Database Connection

![Database Connection](images/Screenshot%202026-07-17%20010325.png)

---

## ✅ Output

The application successfully connected to the Amazon RDS MySQL database.

Browser Output:

```text
✅ Connected to Amazon RDS Successfully!
```

---

## 🎯 Learning Outcomes

- Amazon EC2
- Amazon RDS
- Security Groups
- Apache Web Server
- PHP & MySQL Integration
- SSH Access
- AWS SDK (Boto3)
- Multi-Tier Architecture
- Cloud Deployment

---

## 👨‍💻 Author

**Pranav Patil**

B.Tech – Artificial Intelligence & Machine Learning

---

## ⭐ Project Status

✅ Completed Successfully