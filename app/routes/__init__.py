from .index import get_index, post_index
from .change_password import get_change_password, post_change_password
from .exhibition import get_exhibition
from .user import get_user
from .login import get_login, post_login
from .logout import post_logout

__all__ = [
    get_index,
    post_index,
    get_change_password,
    post_change_password,
    get_exhibition,
    get_user,
    get_login,
    post_login,
    post_logout,
]
