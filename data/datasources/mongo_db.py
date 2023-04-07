from data.datasources.remote_datasource import RemoteDatasource
from domain.entities.todo import Todo
from core.error import Error


class MongoDB(RemoteDatasource):
    def __init__(self, connection_url: str) -> None:
        self.__connection_url = connection_url

    def get_todo(self, id: int) -> Todo | None:
        pass

    def change_todo_status(self, id: int, new_status: bool) -> Todo | Error:
        return Error("not implemented")
