from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    
    # Switch to production mode
    ENV: str = "prod"

    # These will be pulled from .env, but defaults are set to EC2 IP
    KEYCLOAK_CLIENT_ID: str = "Front-End-Client"
    KEYCLOAK_CLIENT_SECRET: str = "W2q3rEyF2GFoRvS6nCpBts4vpBDqlKdi"
    KEYCLOAK_REALM: str = "auth-realm"
    
    # CRITICAL: Point these to your EC2 Public IP
    KEYCLOAK_SERVER_URL: str = "http://18.214.226.2:8080"
    FRONTEND_URL: str = "http://18.214.226.2:3000"
    GATEWAY_URL: str = "http://18.214.226.2"

    KEYCLOAK_ADMIN_CLIENT_ID: str = "fast-api-admin-client"
    KEYCLOAK_ADMIN_CLIENT_SECRET: str = "JemMoYxTqjNK3c5zlKM26KFhnaPYg59z"

    @property
    def metadata_url(self) -> str:
        return (
            f"{self.KEYCLOAK_SERVER_URL}/realms/"
            f"{self.KEYCLOAK_REALM}/.well-known/openid-configuration"
        )

settings = Settings()