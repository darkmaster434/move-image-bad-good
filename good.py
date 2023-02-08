import os
import shutil
file_path='C:/Users/Corrupted/Desktop/New folder'#folder directory
good_path='C:/Users/Corrupted/Desktop/GOOD'#good path
bad_path='C:/Users/Corrupted/Desktop/BAD'#bad path

l=os.listdir(file_path)
new_l=list()
for i in l:
	t=i.split('.')
	new_l.append(int(t[0]))

l=sorted(new_l)
dec=''
f=0
for i in range(len(l)):
	
	os.system('cls')
	print('Image left: ',len(l))
	print('Image Name: ',l[i])
	print('Last Performed: ',dec)
	o=input('nothing for BAD.anything for good except "d" and "s" and "r".s -> switch\nd->delete\nr->refresh\n: ')
	
	if o=='r':
		dec='Refresh'
		l=os.listdir(file_path)
		new_l=list()
		for j in l:
			t=j.split('.')
			new_l.append(int(t[0]))
			l=sorted(new_l)
		i=0
	elif o=='d':
		dec='Delete'+str(l[i])
		os.remove(file_path+'/'+str(l[i])+'.jpg')
		i+=1
	elif o=='s':
		dec='Switch '
		if f==0:
			print('File still here')
		elif f==1:
			dec+='Good to Bad' 
			shutil.move(good_path+'/'+str(l[i-1])+'.jpg',bad_path+'/'+str(l[i-1])+'.jpg')
		elif f==2:
			dec+='Bad to Good' 
			shutil.move(bad_path+'/'+str(l[i-1])+'.jpg',good_path+'/'+str(l[i-1])+'.jpg')
		dec+=' '+str(l[i-1])
	elif o!='':
		dec='Good '+str(l[i])
		f=1
		shutil.move(file_path+'/'+str(l[i])+'.jpg',good_path+'/'+str(l[i])+'.jpg')
		i+=1
	else:
		dec='Bad '+str(l[i])
		f=2
		shutil.move(file_path+'/'+str(l[i])+'.jpg',bad_path+'/'+str(l[i])+'.jpg')
		i+=1


