provider "aws" {
  access_key = "${var.aws_access_key_id}"
  secret_key = "${var.aws_secret_access_key}"
  region = "${var.region_name}"
}

resource "aws_key_pair" "key" {
  key_name   = "${var.aws_key_name}"
  public_key = "${var.aws_public_key}"
}

resource "aws_security_group" "web-node" {
  name = "web-node"
  description = "Web Security Group"
  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "instance" {
  ami                    = "${var.aws_ami}"
  instance_type          = "${var.aws_instance_type}"
  key_name               = "${var.aws_key_name}"
  availability_zone      = "${var.availability_zone}"
  tags {
    Name = "${var.aws_instance_name}"
  }
  security_groups = ["${aws_security_group.web-node.name}"]
  depends_on = ["aws_key_pair.key", "aws_security_group.web-node"]
}

