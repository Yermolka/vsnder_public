from random import choice

import pytest
import pytest_asyncio
from aiohttp import ClientSession

from ..api.user import User


@pytest_asyncio.fixture(scope="function")
async def user():
    async with ClientSession("http://localhost:3000") as session:
        u = User(session, "ЕрмошинА", "123456")
        await u.login()

        yield u

        await u.logout()


@pytest.mark.asyncio
@pytest.mark.user
async def test_user_get(user: User):
    data = await user.get(user.user_id)
    assert data.first_name == "Андрей"
    assert data.last_name == "Ермошин"


@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.parametrize("page", [0, 1, 4])
@pytest.mark.parametrize("limit", [0, 16, 100])
async def test_user_page(user: User, page: int, limit: int):
    order_by = choice(
        ["id", "first_name", "last_name", "age", "orientation", "year_of_study"]
    )
    orientation = choice(["Психология", "Социология", "Политология", "ГМУ"])
    status = choice(
        ["Замужем/Женат", "В отношениях", "Схожу на свидание", "Чиллю соло"]
    )
    query = choice(["Андрей", "абоба"])

    total, data = await user.get_page(
        page, limit, order_by, orientation, None, status, query
    )
    assert total is not None
    assert data is not None


@pytest.mark.asyncio
@pytest.mark.user
async def test_user_edit(user: User):
    data = await user.get(user.user_id)
    data.music = "Музыка"
    assert (await user.edit(data)) is not None


@pytest.mark.asyncio
@pytest.mark.user
async def test_user_get_random(user: User):
    data = await user.get_random()
    data_get = await user.get(data.id)

    assert data == data_get


@pytest.mark.asyncio
@pytest.mark.user
@pytest.mark.message
async def test_user_get_messages(user: User):
    data = await user.get_messages(user.user_id)
    assert data is not None

    with pytest.raises(Exception):
        await user.get_messages(user.user_id + 1)

    data = await user.get_public_messages(user.user_id + 1)
    assert data is not None
