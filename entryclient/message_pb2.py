# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='message',
  syntax='proto3',
  serialized_pb=_b('\n\rmessage.proto\x12\x07message\"|\n\x0eRequestMessage\x12\x34\n\x07msgType\x18\x01 \x01(\x0e\x32#.message.RequestMessage.RequestType\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"#\n\x0bRequestType\x12\t\n\x05PLAIN\x10\x00\x12\t\n\x05WINCH\x10\x01\"\x8d\x01\n\x0fResponseMessage\x12\x36\n\x07msgType\x18\x01 \x01(\x0e\x32%.message.ResponseMessage.ResponseType\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"1\n\x0cResponseType\x12\n\n\x06STDOUT\x10\x00\x12\n\n\x06STDERR\x10\x01\x12\t\n\x05\x43LOSE\x10\x02\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_REQUESTMESSAGE_REQUESTTYPE = _descriptor.EnumDescriptor(
  name='RequestType',
  full_name='message.RequestMessage.RequestType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAIN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WINCH', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=115,
  serialized_end=150,
)
_sym_db.RegisterEnumDescriptor(_REQUESTMESSAGE_REQUESTTYPE)

_RESPONSEMESSAGE_RESPONSETYPE = _descriptor.EnumDescriptor(
  name='ResponseType',
  full_name='message.ResponseMessage.ResponseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STDOUT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STDERR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=245,
  serialized_end=294,
)
_sym_db.RegisterEnumDescriptor(_RESPONSEMESSAGE_RESPONSETYPE)


_REQUESTMESSAGE = _descriptor.Descriptor(
  name='RequestMessage',
  full_name='message.RequestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgType', full_name='message.RequestMessage.msgType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='message.RequestMessage.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTMESSAGE_REQUESTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=150,
)


_RESPONSEMESSAGE = _descriptor.Descriptor(
  name='ResponseMessage',
  full_name='message.ResponseMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msgType', full_name='message.ResponseMessage.msgType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='message.ResponseMessage.content', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESPONSEMESSAGE_RESPONSETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=153,
  serialized_end=294,
)

_REQUESTMESSAGE.fields_by_name['msgType'].enum_type = _REQUESTMESSAGE_REQUESTTYPE
_REQUESTMESSAGE_REQUESTTYPE.containing_type = _REQUESTMESSAGE
_RESPONSEMESSAGE.fields_by_name['msgType'].enum_type = _RESPONSEMESSAGE_RESPONSETYPE
_RESPONSEMESSAGE_RESPONSETYPE.containing_type = _RESPONSEMESSAGE
DESCRIPTOR.message_types_by_name['RequestMessage'] = _REQUESTMESSAGE
DESCRIPTOR.message_types_by_name['ResponseMessage'] = _RESPONSEMESSAGE

RequestMessage = _reflection.GeneratedProtocolMessageType('RequestMessage', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTMESSAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.RequestMessage)
  ))
_sym_db.RegisterMessage(RequestMessage)

ResponseMessage = _reflection.GeneratedProtocolMessageType('ResponseMessage', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSEMESSAGE,
  __module__ = 'message_pb2'
  # @@protoc_insertion_point(class_scope:message.ResponseMessage)
  ))
_sym_db.RegisterMessage(ResponseMessage)


# @@protoc_insertion_point(module_scope)
