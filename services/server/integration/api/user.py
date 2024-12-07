from aiohttp import ClientSession
from vsnder.dto.message import GetMessageDto
from vsnder.dto.user import GetShortUserDto, GetUserDto, PostUserDto

BASE_URL = "http://localhost:3000"


class User:
    session: ClientSession
    user_id: int

    def __init__(self, session: ClientSession, username: str, password: str):
        self.username = username
        self.password = password
        self.session = session

    async def login(self) -> int:
        async with self.session.post(
            "/api/user/login", json=dict(username=self.username, password=self.password)
        ) as resp:
            self.user_id = (await resp.json())["userId"]
            return self.user_id

    async def get(self, user_id: int) -> GetUserDto:
        async with self.session.get(f"/api/user/{user_id}") as resp:
            body = await resp.json()
            return GetUserDto.from_dict(body)

    async def edit(self, data: PostUserDto) -> int:
        async with self.session.post("/api/user/edit", json=data.to_dict()) as resp:
            body = await resp.json()
            return body

    async def logout(self) -> str:
        async with self.session.get("/api/user/logout") as resp:
            return await resp.text()

    async def get_page(
        self,
        page: int,
        limit: int,
        order_by: str = None,
        orientation: str = None,
        year_of_study: int = None,
        status: str = None,
        query: str = None,
    ) -> tuple[int, list[GetShortUserDto]]:
        params = dict(page=page, limit=limit)
        if order_by is not None:
            params["order_by"] = order_by
        if orientation is not None:
            params["orientation"] = orientation
        if year_of_study is not None:
            params["year_of_study"] = year_of_study
        if status is not None:
            params["status"] = status
        if query is not None:
            params["query"] = query

        async with self.session.get(
            "/api/users",
            params=params,
        ) as resp:
            body = await resp.json()
            return body["total"], list(map(GetShortUserDto.from_dict, body["users"]))

    async def get_random(self) -> GetUserDto:
        async with self.session.get("/api/user/random") as resp:
            body = await resp.json()
            return GetUserDto.from_dict(body)

    async def get_messages(self, user_id: int) -> list[GetMessageDto]:
        async with self.session.get(f"/api/user/{user_id}/messages") as resp:
            body = await resp.json()
            return list(map(GetMessageDto.from_dict, body))

    async def get_public_messages(self, user_id: int) -> list[GetMessageDto]:
        async with self.session.get(f"/api/user/{user_id}/messages/public") as resp:
            body = await resp.json()
            return list(map(GetMessageDto.from_dict, body))
