# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spelling_bee.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spelling_bee.proto',
  package='app',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12spelling_bee.proto\x12\x03\x61pp\"1\n\x0bGameRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x10\n\x08gameType\x18\x02 \x01(\t\"T\n\x0cGameResponse\x12\x0e\n\x06gameID\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\x12\x0f\n\x07letters\x18\x03 \x01(\t\x12\x14\n\x0cmiddleLetter\x18\x04 \x01(\t\"0\n\x10\x43heckWordRequest\x12\x0e\n\x06gameID\x18\x01 \x01(\t\x12\x0c\n\x04word\x18\x02 \x01(\t\"C\n\x11\x43heckWordResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\x32\x7f\n\x0bSpellingBee\x12\x32\n\tStartGame\x12\x10.app.GameRequest\x1a\x11.app.GameResponse\"\x00\x12<\n\tCheckWord\x12\x15.app.CheckWordRequest\x1a\x16.app.CheckWordResponse\"\x00\x62\x06proto3'
)




_GAMEREQUEST = _descriptor.Descriptor(
  name='GameRequest',
  full_name='app.GameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='app.GameRequest.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gameType', full_name='app.GameRequest.gameType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=76,
)


_GAMERESPONSE = _descriptor.Descriptor(
  name='GameResponse',
  full_name='app.GameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameID', full_name='app.GameResponse.gameID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='app.GameResponse.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='letters', full_name='app.GameResponse.letters', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='middleLetter', full_name='app.GameResponse.middleLetter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=162,
)


_CHECKWORDREQUEST = _descriptor.Descriptor(
  name='CheckWordRequest',
  full_name='app.CheckWordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='gameID', full_name='app.CheckWordRequest.gameID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='word', full_name='app.CheckWordRequest.word', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=212,
)


_CHECKWORDRESPONSE = _descriptor.Descriptor(
  name='CheckWordResponse',
  full_name='app.CheckWordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='app.CheckWordResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='app.CheckWordResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='app.CheckWordResponse.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=214,
  serialized_end=281,
)

DESCRIPTOR.message_types_by_name['GameRequest'] = _GAMEREQUEST
DESCRIPTOR.message_types_by_name['GameResponse'] = _GAMERESPONSE
DESCRIPTOR.message_types_by_name['CheckWordRequest'] = _CHECKWORDREQUEST
DESCRIPTOR.message_types_by_name['CheckWordResponse'] = _CHECKWORDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameRequest = _reflection.GeneratedProtocolMessageType('GameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEREQUEST,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.GameRequest)
  })
_sym_db.RegisterMessage(GameRequest)

GameResponse = _reflection.GeneratedProtocolMessageType('GameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.GameResponse)
  })
_sym_db.RegisterMessage(GameResponse)

CheckWordRequest = _reflection.GeneratedProtocolMessageType('CheckWordRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHECKWORDREQUEST,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.CheckWordRequest)
  })
_sym_db.RegisterMessage(CheckWordRequest)

CheckWordResponse = _reflection.GeneratedProtocolMessageType('CheckWordResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHECKWORDRESPONSE,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.CheckWordResponse)
  })
_sym_db.RegisterMessage(CheckWordResponse)



_SPELLINGBEE = _descriptor.ServiceDescriptor(
  name='SpellingBee',
  full_name='app.SpellingBee',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=283,
  serialized_end=410,
  methods=[
  _descriptor.MethodDescriptor(
    name='StartGame',
    full_name='app.SpellingBee.StartGame',
    index=0,
    containing_service=None,
    input_type=_GAMEREQUEST,
    output_type=_GAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckWord',
    full_name='app.SpellingBee.CheckWord',
    index=1,
    containing_service=None,
    input_type=_CHECKWORDREQUEST,
    output_type=_CHECKWORDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPELLINGBEE)

DESCRIPTOR.services_by_name['SpellingBee'] = _SPELLINGBEE

# @@protoc_insertion_point(module_scope)
