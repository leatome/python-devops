import os
from app.db import init_db, add_user, get_user

def test_add_and_get_user(tmp_path):
    os.environ["APP_DB_PATH"] = str(tmp_path / "test.db")
    init_db()
    user_id = add_user("bob")
    user = get_user(user_id)
    assert user.name == "bob"
