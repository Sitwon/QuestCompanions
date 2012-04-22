import random, re
from sms import sms
from handler import *
from model import *
from datetime import datetime
import markdown2

@handler('user/index')
def get_index(id, error=None):
	user = User.one(id=id)
	if not user: abort(404)

	return dict(user=user, error=error)

@handler
def post_feedback_create(id, helpful=None, body=None):
	with transact:
		Feedback.create(
				profile_id=id,
				helpful= helpful==u'on',
				date=datetime.now(),
				body=body,
				)
	redirect(get_index.url(id))

@handler
def post_index(id, phone_number=None, email=None):
	def normalize(phone_number):
		if phone_number == None:
			return user.phone_number
		phone_number = re.sub(r'[^0-9]', '', phone_number)
		if len(phone_number) == 11 and phone_number[0] == '1':
			return phone_number[1:]
		return phone_number

	user = User.one(id=id)
	if not user or user != session.user: abort(403)

	phone_number = normalize(phone_number)
	if len(phone_number) != 10:
		redirect(get_index.url(id, error='Invalid phone number'))
	elif False: # XXX add email validation
		redirect(get_index.url(id, error='Invalid email'))
	with transact:
		if phone_number != user.phone_number:
			user.update(
					phone_number=phone_number, 
					phone_verified=False
				)
		if email != user.email:
			user.update(
					email=email, 
					email_verified=True # XXX add email verification
				)

	redirect(get_index.url(id))

def generateVerification():
	with transact:
		session.user.update(
				verification_code=random.randrange(1, 1000000), 
				verification_tries=0
			)
	sms(session.user.phone_number, 'Quest Companions verification code: %06i' % session.user.verification_code)

@handler('user/verify')
def get_verify():
	if session.user.phone_verified:
		redirect(get_index.url(session.user.id))

	new = False
	if not session.user.verification_code:
		generateVerification()
		new=True
	return dict(new=new)

@handler('user/verify')
def post_verify(code):
	if session.user.phone_verified:
		redirect(get_index.url(session.user.id))

	if session.user.verification_code == int(code):
		with transact:
			session.user.update(phone_verified=True)
		redirect(get_index.url(session.user.id))
	elif session.user.verification_tries < 9:
		with transact:
			session.user.update(verification_tries=session.user.verification_tries+1)
		new = False
	else:
		generateVerification()
		new = True
	return dict(code=code, new=new)

@handler('user/verify')
def get_resend_code():
	if session.user.phone_verified:
		redirect(get_index.url(session.user.id))

	if not session.user.verification_code:
		generateVerification()
		new=True
	sms(session.user.phone_number, 'Quest Companions verification code: %06i' % session.user.verification_code)
	return dict(new=new)
