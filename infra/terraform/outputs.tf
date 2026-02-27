output "alb_dns" {
  value = aws_lb.main.dns_name
}

output "ecr_repo" {
  value = aws_ecr_repository.backend.repository_url
}

output "frontend_url" {
  value = aws_s3_bucket_website_configuration.frontend.website_endpoint
}