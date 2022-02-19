import os,sys
import json
img=sys.argv[1]
name=os.path.splitext(img)[0]
anser=0
one=0
five=0
ten=0
fifty=0
os.system("cd darknet && ./darknet detector test data/obj.data cfg/yolov4.cfg backup/yolov4_5000.weights ../media/image/"+img+" -thresh 0.5 -dont_show -out results/"+name+".json && mv predictions.jpg "+img)
#os.system("cd darknet && ./darknet detector test data/obj.data cfg/yolov4.cfg backup/yolov4_5000.weights ../media/image/"+img+" -thresh 0.5 -dont_show -out results/"+name+".json")
def money_dict(type):
	types={0:'1',1:'5',2:'10',3:'50'}
	return types.get(type,'0')
files="./darknet/results/"+name+".json"
with open(files,'r') as obj:
	data=json.load(obj)
for i in data:
	for j in i.get("objects"):
		anser+=int(money_dict(j.get("class_id")))
		if j.get("class_id")==3:
			fifty+=1
		if j.get("class_id")==2:
			ten+=1
		if j.get("class_id")==1:
			five+=1
		if j.get("class_id")==0:
			one+=1
	i["money"]= anser
	i["fifty"]=fifty
	i["ten"]=ten
	i["five"]=five
	i["one"]=one
with open(files,'w') as obj:
	json.dump(data,obj)
#print(img, name)