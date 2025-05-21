import os

from dotenv import load_dotenv

load_dotenv()


# TODO: Add validation for the environment variables, need to throw an error if the required environment variables are not set
class ENVSettings:
    # ? GENERAL SETTINGS
    MONGODB_URL: str = os.environ.get("MONGODB_URL", "mongodb://localhost:27017")
    JWT_KEY: str = os.environ.get("JWT_KEY", "your_secret_key")
    DEFAULT_DB_NAME: str = os.environ.get("DEFAULT_DB_NAME", "default_db")

    # ? For object encryption and decryption
    OBJECT_CRYPTO_KEY: str = os.environ.get("OBJECT_CRYPTO_KEY", "default_secret_key")

    # ? Bitrix accounts which are allowed to access the admin panel
    BX_CRM_MANAGER_ID: str = os.environ.get("BX_CRM_MANAGER_ID", "")
    BX_DEV_ACC_ID: str = os.environ.get("BX_DEV_ACC_ID", "")
    BX_ROOT_ADMIN_IDS: list = [
        os.environ.get("BX_CRM_MANAGER_ID", ""),
        os.environ.get("BX_DEV_ACC_ID", ""),
    ]

    # ? Bitrix webhook settings
    BITRIX_WEBHOOK: str = os.environ.get("BITRIX_WEBHOOK", "")
    BITRIX_WEBHOOK_ID: str = os.environ.get("BITRIX_WEBHOOK_ID", "")
    BITRIX_DOMAIN: str = os.environ.get("BITRIX_DOMAIN", "")

    # ? CRYPTS
    CRYPT_APP_BITRIX_DATA_SECRET = (
        os.getenv("CRYPT_APP_BITRIX_DATA_SECRET") or "jhdsbfjhgdsfjhbdf"
    )

    PHONE_NUMBER_CRYPT_PUBLIC_KEY = (
        os.getenv("PHONE_NUMBER_CRYPT_PUBLIC_KEY") or "PHONE_NUMBER_CRYPT_PUBLIC_KEY"
    )

    PHONE_NUMBER_CRYPT_PRIVATE_KEY = (
        os.getenv("PHONE_NUMBER_CRYPT_PRIVATE_KEY") or "PHONE_NUMBER_CRYPT_PRIVATE_KEY"
    )

    IS_AUTO_CRYPT = os.getenv("IS_AUTO_CRYPT") or False

    # ? Helper constants
    BITRIX_BASIC_WEBHOOK_URL: str = (
        f"https://{BITRIX_DOMAIN}/rest/{BITRIX_WEBHOOK_ID}/{BITRIX_WEBHOOK}"
    )

    # ? SERVER SETTINGS
    SERVER_PORT: str = os.getenv("SERVER_PORT") or "8000"
    SERVER_HOST: str = os.getenv("SERVER_HOST") or "127.0.0.1"

    # ? DOCS SWAGGER
    DOCS_URL: str = os.getenv("DOCS_URL") or "/docs"
    DOCS_TITLE: str = os.getenv("TITLE") or "Decryptor API"
    DOCS_DESCRIPTION: str = "Project for decrypting and encrypting objects"
    SERVER_APP_DOMAIN: str = os.getenv("SERVER_APP_DOMAIN")

    @staticmethod
    def get_db_url():
        return os.environ.get("MONGODB_URL", "mongodb://localhost:27017")
