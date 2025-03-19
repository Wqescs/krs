# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chat.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'chat.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\"0\n\x0bRoomRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"5\n\x0fRegisterRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1d\n\x0c\x41uthResponse\x12\r\n\x05token\x18\x01 \x01(\t\"1\n\x0b\x41uthRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"V\n\x11\x43reateRoomRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x11\n\talgorithm\x18\x02 \x01(\t\x12\x0c\n\x04mode\x18\x03 \x01(\t\x12\x0f\n\x07padding\x18\x04 \x01(\t\"4\n\x0fJoinRoomRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"(\n\x10JoinRoomResponse\x12\t\n\x01p\x18\x01 \x01(\x0c\x12\t\n\x01g\x18\x02 \x01(\x04\"M\n\x14SendPublicKeyRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\npublic_key\x18\x03 \x01(\x0c\"v\n\x0cRoomResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\ncount_user\x18\x02 \x01(\x05\x12\x0f\n\x07room_id\x18\x03 \x01(\t\x12\x11\n\talgorithm\x18\x04 \x01(\t\x12\x0c\n\x04mode\x18\x05 \x01(\t\x12\x0f\n\x07padding\x18\x06 \x01(\t\"7\n\x12GenerateKeyRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"/\n\x13GenerateKeyResponse\x12\x18\n\x10other_public_key\x18\x01 \x01(\x0c\"{\n\x0eMessageRequest\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x19\n\x11\x65ncrypted_message\x18\x03 \x01(\x0c\x12\x12\n\nimage_data\x18\x04 \x01(\x0c\x12\n\n\x02iv\x18\x05 \x01(\x0c\x12\r\n\x05nonce\x18\x06 \x01(\x0c\"|\n\x0fMessageResponse\x12\x0f\n\x07room_id\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x19\n\x11\x65ncrypted_message\x18\x03 \x01(\x0c\x12\x12\n\nimage_data\x18\x04 \x01(\x0c\x12\n\n\x02iv\x18\x05 \x01(\x0c\x12\r\n\x05nonce\x18\x06 \x01(\x0c\x32u\n\x0b\x41uthService\x12\x35\n\x08Register\x12\x15.chat.RegisterRequest\x1a\x12.chat.AuthResponse\x12/\n\x05Login\x12\x12.chat.LoginRequest\x1a\x12.chat.AuthResponse2\xc2\x03\n\x0b\x43hatService\x12\x39\n\nCreateRoom\x12\x17.chat.CreateRoomRequest\x1a\x12.chat.RoomResponse\x12\x39\n\x08JoinRoom\x12\x15.chat.JoinRoomRequest\x1a\x16.chat.JoinRoomResponse\x12>\n\x0bSendMessage\x12\x14.chat.MessageRequest\x1a\x15.chat.MessageResponse(\x01\x30\x01\x12=\n\x0fReceiveMessages\x12\x11.chat.RoomRequest\x1a\x15.chat.MessageResponse0\x01\x12\x32\n\tLeaveRoom\x12\x11.chat.RoomRequest\x1a\x12.chat.RoomResponse\x12?\n\rSendPublicKey\x12\x1a.chat.SendPublicKeyRequest\x1a\x12.chat.RoomResponse\x12I\n\x12GenerateSessionKey\x12\x18.chat.GenerateKeyRequest\x1a\x19.chat.GenerateKeyResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ROOMREQUEST']._serialized_start=20
  _globals['_ROOMREQUEST']._serialized_end=68
  _globals['_REGISTERREQUEST']._serialized_start=70
  _globals['_REGISTERREQUEST']._serialized_end=123
  _globals['_LOGINREQUEST']._serialized_start=125
  _globals['_LOGINREQUEST']._serialized_end=175
  _globals['_AUTHRESPONSE']._serialized_start=177
  _globals['_AUTHRESPONSE']._serialized_end=206
  _globals['_AUTHREQUEST']._serialized_start=208
  _globals['_AUTHREQUEST']._serialized_end=257
  _globals['_CREATEROOMREQUEST']._serialized_start=259
  _globals['_CREATEROOMREQUEST']._serialized_end=345
  _globals['_JOINROOMREQUEST']._serialized_start=347
  _globals['_JOINROOMREQUEST']._serialized_end=399
  _globals['_JOINROOMRESPONSE']._serialized_start=401
  _globals['_JOINROOMRESPONSE']._serialized_end=441
  _globals['_SENDPUBLICKEYREQUEST']._serialized_start=443
  _globals['_SENDPUBLICKEYREQUEST']._serialized_end=520
  _globals['_ROOMRESPONSE']._serialized_start=522
  _globals['_ROOMRESPONSE']._serialized_end=640
  _globals['_GENERATEKEYREQUEST']._serialized_start=642
  _globals['_GENERATEKEYREQUEST']._serialized_end=697
  _globals['_GENERATEKEYRESPONSE']._serialized_start=699
  _globals['_GENERATEKEYRESPONSE']._serialized_end=746
  _globals['_MESSAGEREQUEST']._serialized_start=748
  _globals['_MESSAGEREQUEST']._serialized_end=871
  _globals['_MESSAGERESPONSE']._serialized_start=873
  _globals['_MESSAGERESPONSE']._serialized_end=997
  _globals['_AUTHSERVICE']._serialized_start=999
  _globals['_AUTHSERVICE']._serialized_end=1116
  _globals['_CHATSERVICE']._serialized_start=1119
  _globals['_CHATSERVICE']._serialized_end=1569
# @@protoc_insertion_point(module_scope)