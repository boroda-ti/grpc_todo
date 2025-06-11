import os, sys, grpc, asyncio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from generated import todo_pb2_grpc
from server.todo_service.core import TodoServicer


async def serve():
    server = grpc.aio.server()
    todo_pb2_grpc.add_TodoServicer_to_server(TodoServicer(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    await server.start()
    print(f'Server started on {listen_addr}')
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())