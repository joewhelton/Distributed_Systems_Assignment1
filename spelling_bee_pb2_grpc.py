# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import spelling_bee_pb2 as spelling__bee__pb2


class SpellingBeeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartGame = channel.unary_unary(
                '/app.SpellingBee/StartGame',
                request_serializer=spelling__bee__pb2.GameRequest.SerializeToString,
                response_deserializer=spelling__bee__pb2.GameResponse.FromString,
                )
        self.CheckWord = channel.unary_unary(
                '/app.SpellingBee/CheckWord',
                request_serializer=spelling__bee__pb2.CheckWordRequest.SerializeToString,
                response_deserializer=spelling__bee__pb2.CheckWordResponse.FromString,
                )
        self.NewMultiplayerGame = channel.unary_unary(
                '/app.SpellingBee/NewMultiplayerGame',
                request_serializer=spelling__bee__pb2.NewMultiplayerGameRequest.SerializeToString,
                response_deserializer=spelling__bee__pb2.NewMultiplayerGameResponse.FromString,
                )
        self.JoinMultiplayerGame = channel.unary_unary(
                '/app.SpellingBee/JoinMultiplayerGame',
                request_serializer=spelling__bee__pb2.JoinMultiplayerGameRequest.SerializeToString,
                response_deserializer=spelling__bee__pb2.JoinMultiplayerGameResponse.FromString,
                )
        self.CheckWordMultiplayer = channel.unary_unary(
                '/app.SpellingBee/CheckWordMultiplayer',
                request_serializer=spelling__bee__pb2.CheckWordMultiplayerRequest.SerializeToString,
                response_deserializer=spelling__bee__pb2.CheckWordMultiplayerResponse.FromString,
                )
        self.GetMultiplayerStatus = channel.unary_unary(
                '/app.SpellingBee/GetMultiplayerStatus',
                request_serializer=spelling__bee__pb2.GetMultiplayerStatusRequest.SerializeToString,
                response_deserializer=spelling__bee__pb2.GetMultiplayerStatusResponse.FromString,
                )


class SpellingBeeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckWord(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewMultiplayerGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinMultiplayerGame(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckWordMultiplayer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMultiplayerStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpellingBeeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartGame': grpc.unary_unary_rpc_method_handler(
                    servicer.StartGame,
                    request_deserializer=spelling__bee__pb2.GameRequest.FromString,
                    response_serializer=spelling__bee__pb2.GameResponse.SerializeToString,
            ),
            'CheckWord': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckWord,
                    request_deserializer=spelling__bee__pb2.CheckWordRequest.FromString,
                    response_serializer=spelling__bee__pb2.CheckWordResponse.SerializeToString,
            ),
            'NewMultiplayerGame': grpc.unary_unary_rpc_method_handler(
                    servicer.NewMultiplayerGame,
                    request_deserializer=spelling__bee__pb2.NewMultiplayerGameRequest.FromString,
                    response_serializer=spelling__bee__pb2.NewMultiplayerGameResponse.SerializeToString,
            ),
            'JoinMultiplayerGame': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinMultiplayerGame,
                    request_deserializer=spelling__bee__pb2.JoinMultiplayerGameRequest.FromString,
                    response_serializer=spelling__bee__pb2.JoinMultiplayerGameResponse.SerializeToString,
            ),
            'CheckWordMultiplayer': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckWordMultiplayer,
                    request_deserializer=spelling__bee__pb2.CheckWordMultiplayerRequest.FromString,
                    response_serializer=spelling__bee__pb2.CheckWordMultiplayerResponse.SerializeToString,
            ),
            'GetMultiplayerStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMultiplayerStatus,
                    request_deserializer=spelling__bee__pb2.GetMultiplayerStatusRequest.FromString,
                    response_serializer=spelling__bee__pb2.GetMultiplayerStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'app.SpellingBee', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpellingBee(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/StartGame',
            spelling__bee__pb2.GameRequest.SerializeToString,
            spelling__bee__pb2.GameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckWord(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/CheckWord',
            spelling__bee__pb2.CheckWordRequest.SerializeToString,
            spelling__bee__pb2.CheckWordResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NewMultiplayerGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/NewMultiplayerGame',
            spelling__bee__pb2.NewMultiplayerGameRequest.SerializeToString,
            spelling__bee__pb2.NewMultiplayerGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinMultiplayerGame(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/JoinMultiplayerGame',
            spelling__bee__pb2.JoinMultiplayerGameRequest.SerializeToString,
            spelling__bee__pb2.JoinMultiplayerGameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckWordMultiplayer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/CheckWordMultiplayer',
            spelling__bee__pb2.CheckWordMultiplayerRequest.SerializeToString,
            spelling__bee__pb2.CheckWordMultiplayerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMultiplayerStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/GetMultiplayerStatus',
            spelling__bee__pb2.GetMultiplayerStatusRequest.SerializeToString,
            spelling__bee__pb2.GetMultiplayerStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
