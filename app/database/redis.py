import sys

from redis.asyncio import Redis
from redis.exceptions import AuthenticationError, TimeoutError


class RedisClientDB(Redis):
    def __init__(self) -> None:
        super(RedisClientDB, self).__init__()

    async def open(self) -> None:
        try:
            await self.ping()
        except TimeoutError:
            sys.exit()
        except AuthenticationError:
            sys.exit()
        except Exception as e:
            sys.exit()




redis_client_db: RedisClientDB = RedisClientDB()
