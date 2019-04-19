/*
AWS Access Keys Variables
*/
variable "aws_access_key_id" {}
variable "aws_secret_access_key" {}

/*
AWS Region Variables
*/
variable "region_name" {
    description = "EC2 Region for the VPC"
    default = "us-east-1"
}

variable "availability_zone" {
  default = "us-east-1a"
}

variable "aws_ami" {
    description = "AWS ami type"
    default = "ami-0de53d8956e8dcf80"
}

variable "aws_instance_type" {
    description = "AWS instance type"
    default = "t2.micro"
}

variable "aws_instance_name" {
    description = "AWS instance name"
    default = "terraform-instance"
}

variable "aws_key_name" {
    description = "AWS key name"
    default = "terraform-key"
}

variable "aws_public_key" {
    description = "AWS public key"
}
