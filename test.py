from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient

# Set your Azure subscription ID
subscription_id = "<your-subscription-id>"

# Initialize credentials and ACR client
credential = DefaultAzureCredential()
acr_client = ContainerRegistryManagementClient(credential, subscription_id)

# List all container registries in the subscription
registries = acr_client.registries.list()

for registry in registries:
    print("Registry Name:", registry.name)
    print("Location:", registry.location)
    print("SKU:", registry.sku.name)
    print("Login Server:", registry.login_server)
    print("Admin User Enabled:", registry.admin_user_enabled)
    print("-" * 40)
