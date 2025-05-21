from app.models.user import User
from app.utils.logger import logger


from app.utils.common import generate_random_password, hash_password

from app.config.env import ENVSettings

DEFAULT_ADMINS = [
    {"login": "crmManagerAcc", "bitrix_id": ENVSettings.BX_CRM_MANAGER_ID},
    {"login": "rootDevAcc", "bitrix_id": ENVSettings.BX_DEV_ACC_ID},
]


async def seed_admins():
    """
    Seed default admin users into the database.
    # ! "Root should only be granted via DB injection to prevent root rights from being spread"
    """
    try:
        seeded_users = []
        for admin_data in DEFAULT_ADMINS:
            existing_admin = await User.find_one(User.login == admin_data["login"])
            if not existing_admin:
                password = generate_random_password()
                hashed_password = hash_password(password)
                new_admin = User(
                    login=admin_data["login"],
                    password=hashed_password,
                    bitrix_id=admin_data["bitrix_id"],
                    role="root",
                )
                await User.insert_one(new_admin)
                seeded_users.append(
                    {
                        "login": admin_data["login"],
                        "password": password,
                        "bitrix_id": admin_data["bitrix_id"],
                        "role": "root",
                    }
                )

        if seeded_users:
            logger.success(f"\n\n\nSeeded admins: {seeded_users}\n\n\n")
        else:
            logger.info("No admins were seeded")

    except Exception as e:
        logger.error(f"Failed to seed admins: {e}")
        raise
