# Quickstart

[Quickstart Link](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli#quick-start-tutorial)

`main.tf` contains a nginx configuration that is run via docker container.

Run the following after installing terraform and docker:

- `terraform init` - initialize i.e. download provider
- `terraform plan` (optional) - to show the steps terraform will take
- `terraform apply` - to start the container
- Visit [localhost:8000](http://localhost:8000/) to view the nginx welcome page.
- `terraform destroy` - to stop the container
