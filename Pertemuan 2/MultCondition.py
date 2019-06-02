print("======= Menentukan keadaan air =======\n")
suhu = int(input("Masukan suhu air : "))
if(suhu>100):
	print("Dalam suhu ini air berwujud gas ")
elif(suhu > 0 and suhu <100):
	print("Dalam suhu ini air berwujud zat cair")
else:
	print("Dalam suhu ini air akan berwujud es")