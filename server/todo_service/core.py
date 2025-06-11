from generated import todo_pb2
from generated import todo_pb2_grpc

class TodoServicer(todo_pb2_grpc.TodoServicer):
    def __init__(self):
        self.todos = []


    async def createTodo(self, request, context) -> todo_pb2.TodoItem:
        print(f"Received reqeuest for createTodo: {request}")

        try:
            new_todo = todo_pb2.TodoItem(
                id=len(self.todos),
                text=request.text
            )

        except Exception as e:
            print(f"Error new_todo for createTodo: {e}")
            raise ValueError

        self.todos.append(new_todo)
        return new_todo


    async def readTodos(self, request, context) -> todo_pb2.TodoItems:
        return todo_pb2.TodoItems(
            items=self.todos
        )