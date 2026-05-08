output "public_ip_address" {
  description = "Public IP of the demo VM"
  value       = azurerm_public_ip.main.ip_address
}

output "app_url" {
  description = "Demo app URL"
  value       = "http://${azurerm_public_ip.main.ip_address}:${var.app_port}"
}
