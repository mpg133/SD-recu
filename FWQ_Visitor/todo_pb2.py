# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x0btodoPackage\"?\n\nRegReturns\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02ok\x18\x03 \x01(\x08\x12\x0b\n\x03msg\x18\x04 \x01(\t\"(\n\x06RegVis\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"O\n\x07\x45\x64itVis\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0f\n\x07newName\x18\x03 \x01(\t\x12\x13\n\x0bnewPassword\x18\x04 \x01(\t2\xd2\x01\n\x04Todo\x12\x44\n\x12registrarVisitante\x12\x13.todoPackage.RegVis\x1a\x17.todoPackage.RegReturns\"\x00\x12@\n\x0eloginVisitante\x12\x13.todoPackage.RegVis\x1a\x17.todoPackage.RegReturns\"\x00\x12\x42\n\x0f\x65\x64itarVisitante\x12\x14.todoPackage.EditVis\x1a\x17.todoPackage.RegReturns\"\x00\x62\x06proto3')



_REGRETURNS = DESCRIPTOR.message_types_by_name['RegReturns']
_REGVIS = DESCRIPTOR.message_types_by_name['RegVis']
_EDITVIS = DESCRIPTOR.message_types_by_name['EditVis']
RegReturns = _reflection.GeneratedProtocolMessageType('RegReturns', (_message.Message,), {
  'DESCRIPTOR' : _REGRETURNS,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todoPackage.RegReturns)
  })
_sym_db.RegisterMessage(RegReturns)

RegVis = _reflection.GeneratedProtocolMessageType('RegVis', (_message.Message,), {
  'DESCRIPTOR' : _REGVIS,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todoPackage.RegVis)
  })
_sym_db.RegisterMessage(RegVis)

EditVis = _reflection.GeneratedProtocolMessageType('EditVis', (_message.Message,), {
  'DESCRIPTOR' : _EDITVIS,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:todoPackage.EditVis)
  })
_sym_db.RegisterMessage(EditVis)

_TODO = DESCRIPTOR.services_by_name['Todo']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGRETURNS._serialized_start=27
  _REGRETURNS._serialized_end=90
  _REGVIS._serialized_start=92
  _REGVIS._serialized_end=132
  _EDITVIS._serialized_start=134
  _EDITVIS._serialized_end=213
  _TODO._serialized_start=216
  _TODO._serialized_end=426
# @@protoc_insertion_point(module_scope)
