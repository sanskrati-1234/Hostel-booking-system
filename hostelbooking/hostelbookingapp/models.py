from django.db import models

# Create your models here.
class State(models.Model):
	stateName=models.CharField(max_length=120)
	def __str__(self):
		return self.stateName

class City(models.Model):
	cityName=models.CharField(max_length=120)
	stateName=models.ForeignKey(State,on_delete=models.CASCADE)
	def __str__(self):
		return self.cityName





class Hostel(models.Model):
	hostelName=models.CharField(max_length=120)
	TYPE=(
			('Girls Hostel','Girls Hostel'),
			('Boys Hostel','Boys Hostel'),
		)
	type=models.CharField(max_length=20,choices=TYPE)
	AVALIABILITY=(('avaliable','avaliable'),
		('unavaliable','unavaliable'),

		)
	avaliable=models.CharField(max_length=20,choices=AVALIABILITY)
	images=models.FileField(upload_to='upload/hostel')
	description=models.CharField(max_length=2000)
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	location=models.CharField(max_length=120)
	owner=models.CharField(max_length=50)
	price=models.IntegerField()
	contact=models.CharField(max_length=10,default="90909")	
	def __str__(self):
		return f'{self.hostelName}';
	

class Room(models.Model):
	seat=models.IntegerField()
	roomImg=models.FileField(upload_to='upload/hostel/room')
	avaliable=models.BooleanField(default=False)
	hostel=models.ForeignKey(Hostel,on_delete=models.CASCADE)
	def __str__(self):
		return f'{"room with"+str(self.seat)+"seaters"}-{self.roomImg}';
class Tefin:
		pass		
class Tenant(models.Model):
	name=models.CharField(max_length=120)
	fatherName=models.CharField(max_length=120)
	address=models.CharField(max_length=500)
	phone=models.CharField(max_length=10)
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	qualification=models.CharField(max_length=10)	
	TEFIN=(
			('Interested','Interested'),
			('NotInterested','NotInterested'),
		)
	tefin=models.CharField(max_length=20,choices=TEFIN)
	photo=models.FileField(upload_to='upload/tenant')
	room=models.ForeignKey(Room,on_delete=models.CASCADE)		