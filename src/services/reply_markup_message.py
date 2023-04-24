from typing import Dict, List, Union
from uuid import uuid4

from models.redis.replymarkupmessage import ReplyMarkupMessage


def generate_imessage_id() -> str:
    return str(uuid4())


async def create_reply_markup_message(pk: str, message_id: int, language_code: str) -> ReplyMarkupMessage:
    obj = await ReplyMarkupMessage(pk=pk, message_id=message_id, language_code=language_code).save()
    await obj.expire(3600)
    return obj


async def bulk_create_reply_markup_message(objects_data: List[Dict[str, Union[str, int]]]) -> List[ReplyMarkupMessage]:
    for obj_data in objects_data:
        await create_reply_markup_message(**obj_data)


async def get_reply_markup_message(imessage_id: str) -> ReplyMarkupMessage:
    obj = await ReplyMarkupMessage.get(imessage_id)
    return obj
