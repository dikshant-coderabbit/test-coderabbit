from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient

# Set your Azure subscr
# List all container registries in the subscription
registries = acr_client.registries.list()

for registry in registries:
    print("Registry Name:", registry.name)
    print("Location:", registry.location)
    print("SKU:", registry.sku.name)
    print("Login Server:", registry.login_server)
    print("Admin User Enabled:", registry.admin_user_enabled)
    print("-" * 40)
