#!/bin/bash

yum update -y
yum install -y httpd

systemctl start httpd
systemctl enable httpd

echo "<h1>Welcome to Pranav's ALB Project</h1>" > /var/www/html/index.html
echo "<h2>Server is Running Successfully!</h2>" >> /var/www/html/index.html