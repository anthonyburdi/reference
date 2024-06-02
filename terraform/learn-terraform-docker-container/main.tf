# Docker provider docs:
# https://registry.terraform.io/providers/kreuzwerker/docker/latest/docs

terraform {
# Providers for terraform to download:
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

# Provider options:
provider "docker" {}

# Pulls the image
resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

# Create a container
resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "tutorial"

  ports {
    internal = 80
    external = 8000
  }
}
