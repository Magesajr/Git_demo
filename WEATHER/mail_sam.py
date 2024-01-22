from itsdangerous import URLSafeTimedSerializer as serial

class Mail:

	def __init__(self,max_age,salt):
		self.max_age=max_age
		self.salt=salt

	def resets(self):
		s=serial(self.max_age,salt=self.salt)
		self.sam=s.dumps({'user_id':1})
		return  self.sam



	@staticmethod
	def verify(salt='reset',max_age=5):
		s=serial('secrets',salt=salt)
		sam=s.dumps({'user_id':90})
		#try:
			#user_id=s.loads(sam,max_age)
		#except:
			#return  user_id
		return s.loads(sam,30)

sk=Mail('secrets','reset')

tk=Mail.verify()

print(tk)

#print(tk,sk.resets(),sep='\n')

