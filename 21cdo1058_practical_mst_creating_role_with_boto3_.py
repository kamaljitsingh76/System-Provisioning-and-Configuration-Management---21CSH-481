import boto3
import json

iam_client = boto3.client('iam')

assume_role_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"  
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

iam_client.create_role(
    RoleName='my_instance_role',
    AssumeRolePolicyDocument=json.dumps(assume_role_policy_document),
    Description="Role for EC2 instances to access resources",
)

policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
iam_client.attach_role_policy(
    RoleName='my_instance_role',
    PolicyArn=policy_arn
)

print("Role created suceessfully and Policy attached.")