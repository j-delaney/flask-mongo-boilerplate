from app import db
from mongokit import Document

@db.register
class User(Document):
	__collection__ = 'users'
	__database__ = 'sample'

	structure = {
		'name': unicode,
		'visits': int
	}

	required_fields = ['name']
	default_values = {
		'visits': 0
	}
	use_dot_notation = True