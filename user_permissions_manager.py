from collections.abc import Collection
from typing import Any, Dict, Optional, Tuple

from synapse.module_api import ModuleApi
from synapse.spam_checker_api import RegistrationBehaviour

class UserPermissionsManager:
    def __init__(self, config: Dict[str, Any], api: ModuleApi):
        self.config = config
        self.api = api
        self.api.register_spam_checker_callbacks(user_may_create_room=self.user_may_create_room)

    async def user_may_create_room(self, user_id: str) -> bool:
        return user_id in (await self.api._store.get_local_users_in_room("!DfdVjzZpVpcKZQuxPy:chat.warmupboston.org"))
