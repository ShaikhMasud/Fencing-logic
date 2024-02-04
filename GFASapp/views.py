from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request,"home.html")
    else:
        return redirect('/signin')

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return redirect('/signin')
        else:
            return render(request,"login.html")



def signout(request):
    logout(request)
    return redirect('/signin')



def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        confpassword=request.POST['confirmpassword']
        if password==confpassword:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            login(request,user)
            return redirect('/')
        else:
            return redirect('/signup')
    else:
        return render(request,"signup.html")
    
# # barcode_scanner/views.py
# from django.shortcuts import render
# import cv2
# from pyzbar.pyzbar import decode

# def scan_barcode(request):
#     cap = cv2.VideoCapture(0)

#     while cap.isOpened():
#         success, frame = cap.read()

#         frame = cv2.flip(frame, 1)

#         # QR Code detection
#         detect_qr_code = decode(frame)
#         if detect_qr_code:
#             for qr_code in detect_qr_code:
#                 if qr_code.data != "":
#                     barcode_data = qr_code.data.decode('utf-8')
#                     cap.release()
#                     cv2.destroyAllWindows()
#                     return render(request, 'barcode_scanner/result.html', {'barcode_data': barcode_data})

#         cv2.imshow('Code Scanner', frame)

#         key = cv2.waitKey(1)
#         if key == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()

#     return render(request, 'barcode_scanner/scan_barcode.html')
    
    # barcode_scanner/views.py
from django.shortcuts import render

def scan_result(request):
    barcode_data = request.GET.get('data', '')
    return render(request, 'barcode_scanner/scan_result.html', {'barcode_data': barcode_data})

from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from geopy.distance import geodesic

from django.http import JsonResponse
from geopy.distance import geodesic

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from django.shortcuts import render
from django.http import JsonResponse
from geopy.distance import geodesic

def location(request):
    if request.method == 'POST':
        # Get geofence coordinates (replace with your actual values)
        geofence_latitude = 19.126130
        geofence_longitude = 73.034959
        geofence_coords = (geofence_latitude, geofence_longitude)

        # Get device coordinates from the request
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        device_coords = (float(latitude), float(longitude))

        # Calculate distance
        distance = geodesic(geofence_coords, device_coords).meters
        geofence_radius = 10000000  # meters (adjust according to your needs)

        # Check if the device is within the geofence
        if distance <= geofence_radius:
            # Save attendance record to the database (you can add your logic here)
            return JsonResponse({'message': 'Attendance recorded successfully.'})
        else:
            return JsonResponse({'message': 'Device is outside the geofence.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

def loc(request):
    return render(request ,"getlocation.html")

from getmac import get_mac_address

def mac(request):
    mac_address = get_mac_address()
    return render(request, 'mac.html', {'mac_address': mac_address})




