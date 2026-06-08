import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

class UserService:
    logger = logging.getLogger(__name__)

    def create_user(self, username):
        self.logger.info(f"Creating user: {username}")
        # business logic
        self.logger.info(f"User created: {username}")

service = UserService()
service.create_user("alice")
