from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import City,State,Hostel,Room,Tenant
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

state1=State()
# Create your views here.
def index(request):
	'''for k,v in state.items():
		print(k)
		print(v)
		global state1
		for li in v:
			print(li)
			for k1,v1 in li.items():
				
				
				print(k1)
				if k1=="state":

					state1=State(stateName=v1)
					state1.save()

				print(v1)
				if k1=="districts":
					for districts in v1:
						city=City(stateName=state1,cityName=districts)
						city.save()
						print(districts)

					print("yes")'''



			

		


	return render(request,"hostelbookingapp/index.html")

def hostel(request):
	return render(request,"hostelbookingapp/hostel.html")

def registerhostel(request):
	context={}
	context['city']=City.objects.all()
	return render(request,"hostelbookingapp/registerhostel.html",context)

def collecthostel(request):
	context={}
	context['hostels']=Hostel.objects.filter(avaliable__exact="avaliable")
	print(context['hostels'])
	return render(request,"hostelbookingapp/hostel.html",context)

def registeryourhostel(request):
	if request.method=='POST':
		hostelName=request.POST['hostelname']
		type=request.POST['type']
		avaliable=request.POST['status']
		images=request.FILES['image']
		fs=FileSystemStorage()
		fs.save(images.name,images)
		description=request.POST['description']
		city=request.POST['city']
		city1=City.objects.get(cityName__exact=city)
		location=request.POST['location1']
		owner=request.POST['owner']
		price=request.POST['price']
		contact=request.POST['contact']
		print(Hostel.objects.filter(contact__exact=contact))
		print(Hostel.objects.filter(contact__exact=contact).exists())
		
		if Hostel.objects.filter(contact__exact=contact).exists():
			city=City.objects.all()
			context={}
			context['city']=city
			return render(request,"hostelbookingapp/registerhostel.html",context)
			
		else:
			
			hostel=Hostel(hostelName=hostelName,type=type,avaliable=avaliable,images=images,description=description,city=city1,location=location,owner=owner,contact=contact,price=price)
			context={}
			context['hostel']=hostel
			hostel.save()
			return render(request,"hostelbookingapp/addroom.html",context)		

		
	else:
		context={}
		city=City.objects.all()
		context['city']=city
		return render(request,"hostelbookingapp/registerhostel.html",context)

def login(request):
	
	#context={}
	#context['hostel']=Hostel.objects.all()
	return render(request,"hostelbookingapp/hostellogin.html")

def loginyourself(request):
	if request.method=='POST':
		name=request.POST['username']
		contact=request.POST['contact']
		try:
			hostel=Hostel.objects.get(contact__exact=contact,owner__exact=name)
			context={}
			if hostel:
					context['hostel']=hostel
					print(hostel)
					return render(request,"hostelbookingapp/addroom.html",context)
		except:
				try:
					tenant=Tenant.objects.get(name__exact=name,phone__exact=contact)
					if tenant:
							context={}
							context['tenant']=tenant
							return render(request,"hostelbookingapp/detailofroom.html",context)
				except:
					return render(request,"hostelbookingapp/addroom.html")
					



		
	else:	
		return render(request,"hostelbookingapp/addroom.html")

def addroom(request):
	if request.method=='POST':

		image=request.FILES['image']
		hostel=request.POST['hostel']
		hostelObj=Hostel.objects.get(hostelName__exact=hostel)
		seat=request.POST['seat']
		avaliableval=request.POST['avaliable']
		avaliable=False
		if avaliableval=='on':
			avaliable=True
		
			
		room=Room(roomImg=image,hostel=hostelObj,seat=seat,avaliable=avaliable)
		print(str(room)+"--------------")
		print(avaliable)
		fs=FileSystemStorage()
		fs.save(image.name,image)

		context={}
		context['hostel']=hostelObj
	 
		print(context['hostel'])
		room.save()
		print(str(hostelObj.id)+"-----")



		return render(request,"hostelbookingapp/addroom.html",context)
	else:	
		return render(request,"hostelbookingapp/addroom.html",context)

def showDetail(request,hostel_id):
	hostel1=Hostel.objects.get(pk=hostel_id)
	print(hostel_id)
	room=Room.objects.filter(hostel__exact=hostel1)
	context={}
	context['rooms']=room
	print(room)
	#context2={'ABC':123}
	#context2['hostel']=hostels

	return render(request,"hostelbookingapp/showDetails.html",context)

def showRooms(request,hostel_id):
	hostel=Hostel.objects.get(pk=hostel_id)
	room=Room.objects.filter(hostel=hostel)
	print(room)

	context={}
	context['rooms']=room
	return render(request,"hostelbookingapp/showRooms.html",context)
def tenantPage(request,room_id):
	room=Room.objects.get(pk=room_id)
	city=City.objects.all()
	context={}
	context['room1']=room
	context['city']=city
	return render(request,"hostelbookingapp/registertenant.html",context)	

def registerTenant(request,room_id):
	if request.method=='POST':
		name=request.POST['name']
		fatherName=request.POST['fatherName']
		address=request.POST['address']
		phone=request.POST['phone']
		city=request.POST['city']
		city1=City.objects.get(cityName__exact=city)
		qualification=request.POST['qualification']
		tefin=request.POST['tefin']
		photo=request.FILES['photo']
		fs=FileSystemStorage()
		fs.save(photo.name,photo)
		room=Room.objects.get(pk=room_id)
		tenant=Tenant(name=name,fatherName=fatherName,address=address,phone=phone,city=city1,qualification=qualification,tefin=tefin,photo=photo,room=room)
		tenant.save()
		return HttpResponse("success")
	else:
		return HttpResponse("something wrong")
def abouttenentroom(request):
		pass
def abouttefin(request):
		pass
def orderTefin(request,tenant_id):
	tenant=Tenant.objects.get(pk=tenant_id)
	context['tenant']=tenant
	return render(request,"hostelbookingapp/tefindetail.html",context)




		
