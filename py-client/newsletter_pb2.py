# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: newsletter.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='newsletter.proto',
  package='newsletter',
  syntax='proto3',
  serialized_options=b'\n\027com.olliekrk.newsletterB\017NewsletterProtoP\001',
  serialized_pb=b'\n\x10newsletter.proto\x12\nnewsletter\"~\n\x04News\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.newsletter.NewsType\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\r\n\x05views\x18\x03 \x01(\x03\x12\x32\n\x0e\x63ommentSection\x18\x04 \x01(\x0b\x32\x1a.newsletter.CommentSection\"N\n\x0e\x43ommentSection\x12\x15\n\radministrated\x18\x01 \x01(\x08\x12%\n\x08\x63omments\x18\x02 \x03(\x0b\x32\x13.newsletter.Comment\")\n\x07\x43omment\x12\x0e\n\x06\x61uthor\x18\x01 \x01(\t\x12\x0e\n\x06rating\x18\x02 \x01(\x03\"G\n\x0bNewsRequest\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.newsletter.NewsType\x12\x14\n\x0csearchPhrase\x18\x02 \x01(\t*6\n\x08NewsType\x12\x0c\n\x08\x46ORECAST\x10\x00\x12\x0b\n\x07\x41RTICLE\x10\x01\x12\x0f\n\x0b\x44OCUMENTARY\x10\x02\x32\x91\x01\n\x11NewsletterService\x12:\n\tfetchNews\x12\x17.newsletter.NewsRequest\x1a\x10.newsletter.News\"\x00\x30\x01\x12@\n\rfetchManyNews\x12\x17.newsletter.NewsRequest\x1a\x10.newsletter.News\"\x00(\x01\x30\x01\x42,\n\x17\x63om.olliekrk.newsletterB\x0fNewsletterProtoP\x01\x62\x06proto3'
)

_NEWSTYPE = _descriptor.EnumDescriptor(
  name='NewsType',
  full_name='newsletter.NewsType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORECAST', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTICLE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOCUMENTARY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=356,
  serialized_end=410,
)
_sym_db.RegisterEnumDescriptor(_NEWSTYPE)

NewsType = enum_type_wrapper.EnumTypeWrapper(_NEWSTYPE)
FORECAST = 0
ARTICLE = 1
DOCUMENTARY = 2



_NEWS = _descriptor.Descriptor(
  name='News',
  full_name='newsletter.News',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='newsletter.News.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='newsletter.News.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='views', full_name='newsletter.News.views', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commentSection', full_name='newsletter.News.commentSection', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=32,
  serialized_end=158,
)


_COMMENTSECTION = _descriptor.Descriptor(
  name='CommentSection',
  full_name='newsletter.CommentSection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='administrated', full_name='newsletter.CommentSection.administrated', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comments', full_name='newsletter.CommentSection.comments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=160,
  serialized_end=238,
)


_COMMENT = _descriptor.Descriptor(
  name='Comment',
  full_name='newsletter.Comment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='author', full_name='newsletter.Comment.author', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rating', full_name='newsletter.Comment.rating', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=240,
  serialized_end=281,
)


_NEWSREQUEST = _descriptor.Descriptor(
  name='NewsRequest',
  full_name='newsletter.NewsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='newsletter.NewsRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='searchPhrase', full_name='newsletter.NewsRequest.searchPhrase', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=283,
  serialized_end=354,
)

_NEWS.fields_by_name['type'].enum_type = _NEWSTYPE
_NEWS.fields_by_name['commentSection'].message_type = _COMMENTSECTION
_COMMENTSECTION.fields_by_name['comments'].message_type = _COMMENT
_NEWSREQUEST.fields_by_name['type'].enum_type = _NEWSTYPE
DESCRIPTOR.message_types_by_name['News'] = _NEWS
DESCRIPTOR.message_types_by_name['CommentSection'] = _COMMENTSECTION
DESCRIPTOR.message_types_by_name['Comment'] = _COMMENT
DESCRIPTOR.message_types_by_name['NewsRequest'] = _NEWSREQUEST
DESCRIPTOR.enum_types_by_name['NewsType'] = _NEWSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

News = _reflection.GeneratedProtocolMessageType('News', (_message.Message,), {
  'DESCRIPTOR' : _NEWS,
  '__module__' : 'newsletter_pb2'
  # @@protoc_insertion_point(class_scope:newsletter.News)
  })
_sym_db.RegisterMessage(News)

CommentSection = _reflection.GeneratedProtocolMessageType('CommentSection', (_message.Message,), {
  'DESCRIPTOR' : _COMMENTSECTION,
  '__module__' : 'newsletter_pb2'
  # @@protoc_insertion_point(class_scope:newsletter.CommentSection)
  })
_sym_db.RegisterMessage(CommentSection)

Comment = _reflection.GeneratedProtocolMessageType('Comment', (_message.Message,), {
  'DESCRIPTOR' : _COMMENT,
  '__module__' : 'newsletter_pb2'
  # @@protoc_insertion_point(class_scope:newsletter.Comment)
  })
_sym_db.RegisterMessage(Comment)

NewsRequest = _reflection.GeneratedProtocolMessageType('NewsRequest', (_message.Message,), {
  'DESCRIPTOR' : _NEWSREQUEST,
  '__module__' : 'newsletter_pb2'
  # @@protoc_insertion_point(class_scope:newsletter.NewsRequest)
  })
_sym_db.RegisterMessage(NewsRequest)


DESCRIPTOR._options = None

_NEWSLETTERSERVICE = _descriptor.ServiceDescriptor(
  name='NewsletterService',
  full_name='newsletter.NewsletterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=413,
  serialized_end=558,
  methods=[
  _descriptor.MethodDescriptor(
    name='fetchNews',
    full_name='newsletter.NewsletterService.fetchNews',
    index=0,
    containing_service=None,
    input_type=_NEWSREQUEST,
    output_type=_NEWS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='fetchManyNews',
    full_name='newsletter.NewsletterService.fetchManyNews',
    index=1,
    containing_service=None,
    input_type=_NEWSREQUEST,
    output_type=_NEWS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_NEWSLETTERSERVICE)

DESCRIPTOR.services_by_name['NewsletterService'] = _NEWSLETTERSERVICE

# @@protoc_insertion_point(module_scope)
