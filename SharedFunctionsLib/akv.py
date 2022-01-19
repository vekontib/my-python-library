

# ===========================================
# Let's define a class for handling secrets
# in Azure Key Vault, using a secret scope
# in Databricks
# ===========================================

class akv:
    
  def getSecret(self, secretName):
    try:
      return dbutils.secrets.get(scope = self.secretScope, key = secretName)
    except:
      return None
    
  def setSecretScope(self, secretScope):
    self.secretScope = secretScope
    
  def __init__(self, secretScope):
    self.setSecretScope(secretScope = secretScope)
    
# ===========================================