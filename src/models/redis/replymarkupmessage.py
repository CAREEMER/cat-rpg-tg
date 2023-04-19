from aredis_om import HashModel


class ReplyMarkupMessage(HashModel):
    message_id: int
    language_code: str
