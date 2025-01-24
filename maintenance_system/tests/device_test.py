import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from maintenance_system import db, app
from maintenance_system.models import Department, Device
import unittest
from flask_testing import TestCase

class TestDevice(TestCase):
	def create_app(self):
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		return app

	def setUp(self):
		db.create_all()

	def tearDown(self):
		db.session.remove()
		os.remove('instance/test.db')

	def test_device(self):
		device = Device(name='X-Ray Machine', department_id=1)
		db.session.add(device)
		db.session.commit()
		devices = Device.query.all()
		self.assertEqual(len(devices), 1)
		self.assertEqual(devices[0].name, 'X-Ray Machine')

	def test_device_repr(self):
		device = Device(name='X-Ray Machine', department_id=1)
		self.assertEqual(str(device), '<Device: X-Ray Machine>')

	def test_device_delete(self):
		device = Device(name='X-Ray Machine', department_id=1)
		db.session.add(device)
		db.session.commit()
		devices = Device.query.all()
		self.assertEqual(len(devices), 1)
		db.session.delete(device)
		db.session.commit()
		devices = Device.query.all()
		self.assertEqual(len(devices), 0)

	def test_device_update(self):
		device = Device(name='X-Ray Machine', department_id=1)
		db.session.add(device)
		db.session.commit()
		devices = Device.query.all()
		self.assertEqual(len(devices), 1)
		device.name = 'MRI Machine'
		db.session.commit()
		devices = Device.query.all()
		self.assertEqual(len(devices), 1)
		self.assertEqual(devices[0].name, 'MRI Machine')

if __name__ == '__main__':
	unittest.main()