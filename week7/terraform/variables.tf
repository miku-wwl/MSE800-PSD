variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastasia"
}

variable "resource_group_name" {
  description = "Resource group name"
  type        = string
  default     = "rg-week7-demo"
}

variable "name_prefix" {
  description = "Name prefix for Azure resources"
  type        = string
  default     = "week7-demo"
}

variable "vm_size" {
  description = "VM size"
  type        = string
  default     = "Standard_B1s"
}

variable "admin_username" {
  description = "Linux admin user"
  type        = string
  default     = "azureuser"
}

variable "ssh_public_key" {
  description = "SSH public key for the VM"
  type        = string
}

variable "repo_url" {
  description = "Git repository URL used by the VM bootstrap script"
  type        = string
}

variable "repo_branch" {
  description = "Branch to deploy"
  type        = string
  default     = "main"
}

variable "app_port" {
  description = "Port exposed by the demo app"
  type        = number
  default     = 5000
}
