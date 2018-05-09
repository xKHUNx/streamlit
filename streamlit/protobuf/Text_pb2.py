# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Text.proto

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
  name='Text.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nText.proto\"\xb6\x01\n\x04Text\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12\x1c\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x0c.Text.Format\"\x81\x01\n\x06\x46ormat\x12\t\n\x05PLAIN\x10\x00\x12\x0c\n\x08MARKDOWN\x10\x01\x12\x08\n\x04JSON\x10\x02\x12\t\n\x05TITLE\x10\x03\x12\n\n\x06HEADER\x10\x04\x12\x0e\n\nSUB_HEADER\x10\x05\x12\t\n\x05\x45RROR\x10\x06\x12\x0b\n\x07WARNING\x10\x07\x12\x08\n\x04INFO\x10\x08\x12\x0b\n\x07SUCCESS\x10\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_TEXT_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='Text.Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLAIN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARKDOWN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JSON', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TITLE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEADER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUB_HEADER', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=68,
  serialized_end=197,
)
_sym_db.RegisterEnumDescriptor(_TEXT_FORMAT)


_TEXT = _descriptor.Descriptor(
  name='Text',
  full_name='Text',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='Text.body', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format', full_name='Text.format', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TEXT_FORMAT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=197,
)

_TEXT.fields_by_name['format'].enum_type = _TEXT_FORMAT
_TEXT_FORMAT.containing_type = _TEXT
DESCRIPTOR.message_types_by_name['Text'] = _TEXT

Text = _reflection.GeneratedProtocolMessageType('Text', (_message.Message,), dict(
  DESCRIPTOR = _TEXT,
  __module__ = 'Text_pb2'
  # @@protoc_insertion_point(class_scope:Text)
  ))
_sym_db.RegisterMessage(Text)


# @@protoc_insertion_point(module_scope)