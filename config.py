import os
from dotenv import load_dotenv

load_dotenv()


class SystemConfig:

    SECRET_KEY = os.getenv("SECRET_KEY")
    firebase_config = {
        'type': os.getenv("type"),

        'project_id': os.getenv("project_id"),
        'private_key_id': os.getenv("private_key_id"),
        'private_key': os.getenv("private_key"),
        'client_email': os.getenv("client_email"),
        'client_id': os.getenv("client_id"),
        'auth_uri': os.getenv("auth_uri"),
        'token_uri': os.getenv("token_uri"),
        'auth_provider_x509_cert_url': os.getenv("auth_provider_x509_cert_url"),
        'client_x509_cert_url': os.getenv("client_x509_cert_url"),

    }

system_config = SystemConfig()
