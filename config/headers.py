import os
from dotenv import load_dotenv

load_dotenv()

class Headers:

    # basic = {
    #     "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
    # }
    def headers(self, x_task_id):
        return {
            "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
            "X-Task-Id": x_task_id
        }

