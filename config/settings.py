import os
from dotenv import load_dotenv
load_dotenv()
class settings():
    def __init__(self):
        self.project_name = self.get_required("PROJECT_NAME")
        self.environment = self.get_required("ENVIRONMENT")
        self.kafka_bootstrap_servers = self.get_required("KAFKA_BOOTSTRAP_SERVERS")
        self.postgres_host = self.get_required("POSTGRES_HOST")
        self.postgres_port = self.get_required("POSTGRES_PORT")
        self.postgres_database = self.get_required("POSTGRES_DATABASE")
        self.postgres_user = self.get_required("POSTGRES_USER")
        self.postgres_password = self.get_required("POSTGRES_PASSWORD")
    @property
    def postgres_url(self) -> str:

        return (
            f"postgresql://"
            f"{self.postgres_user}:"
            f"{self.postgres_password}@"
            f"{self.postgres_host}:"
            f"{self.postgres_port}/"
            f"{self.postgres_database}"
     )
    # @staticmethod
    def get_required(self, key):
        value = os.getenv(key)
        if not value:
            raise  ValueError(f"Missing required environment variable: {key}")
        return value
settings = settings()