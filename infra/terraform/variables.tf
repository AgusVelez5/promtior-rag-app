variable "aws_region" {
  default = "us-east-1"
}

variable "project_name" {
  default = "promtior-app"
}

variable "container_port" {
  default = 8000
}

variable "ecs_desired_count" {
  default = 1
}

variable "vectorstore_dir" {
  default = "data/vectorstore"
}

variable "openai_api_key" {
  description = "OpenAI API Key"
  type        = string
  sensitive   = true
}