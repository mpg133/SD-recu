# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import todo_pb2 as todo__pb2


class TodoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registrarVisitante = channel.unary_unary(
                '/todoPackage.Todo/registrarVisitante',
                request_serializer=todo__pb2.RegVis.SerializeToString,
                response_deserializer=todo__pb2.RegReturns.FromString,
                )
        self.editarVisitante = channel.unary_unary(
                '/todoPackage.Todo/editarVisitante',
                request_serializer=todo__pb2.EditVis.SerializeToString,
                response_deserializer=todo__pb2.RegReturns.FromString,
                )


class TodoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registrarVisitante(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def editarVisitante(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registrarVisitante': grpc.unary_unary_rpc_method_handler(
                    servicer.registrarVisitante,
                    request_deserializer=todo__pb2.RegVis.FromString,
                    response_serializer=todo__pb2.RegReturns.SerializeToString,
            ),
            'editarVisitante': grpc.unary_unary_rpc_method_handler(
                    servicer.editarVisitante,
                    request_deserializer=todo__pb2.EditVis.FromString,
                    response_serializer=todo__pb2.RegReturns.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todoPackage.Todo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Todo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registrarVisitante(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todoPackage.Todo/registrarVisitante',
            todo__pb2.RegVis.SerializeToString,
            todo__pb2.RegReturns.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def editarVisitante(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/todoPackage.Todo/editarVisitante',
            todo__pb2.EditVis.SerializeToString,
            todo__pb2.RegReturns.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
