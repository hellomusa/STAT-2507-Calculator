from statsapp import db

class Data(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nums = db.Column(db.Text) 

	def __repr__(self):
		return f"Data('{self.nums}')"