import os, sys, grpc, asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from generated import todo_pb2, todo_pb2_grpc


async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = todo_pb2_grpc.TodoStub(channel)

        response = await stub.createTodo(todo_pb2.TodoItem(text="Do hometask"))
        print("Created:", response)

        response = await stub.createTodo(todo_pb2.TodoItem(text="Cook dinner"))
        print("Created:", response)

        todo_list = await stub.readTodos(todo_pb2.void())
        for todo in todo_list.items:
            print(f"{todo.id}: {todo.text}")

if __name__ == '__main__':
    asyncio.run(run())