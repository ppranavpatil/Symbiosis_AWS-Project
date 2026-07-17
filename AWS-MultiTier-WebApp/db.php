<?php

$host = "pranav-mysql-db.cl0wo8qyeob3.ap-south-1.rds.amazonaws.com";
$user = "admin";
$password = "Pranav12345";
$database = "mydatabase";

$conn = new mysqli($host, $user, $password);

if ($conn->connect_error) {
    die("Connection Failed: " . $conn->connect_error);
}

echo "<h2>✅ Connected to RDS MySQL Successfully!</h2>";

