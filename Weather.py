from tkinter import*
from PIL import ImageTk,ImageTk
import json
import requests
root = Tk()
root.title("Dropdown Menus")
root.geometry("600x100")

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=F03B615A-5E46-4609-82AF-54D4A1D31F1D
def lookup():
	try:
		api_req = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zipc.get()+"&distance=25&API_KEY=F03B615A-5E46-4609-82AF-54D4A1D31F1D")
		api = json.loads(api_req.content)
		city=api[0]["ReportingArea"]
		aqi = api[0]["AQI"]
		category=api[0]["Category"]["Name"]

		if category=="Good":
			w_color="green"
		elif category=="Moderate":
			w_color="#FFF00"
		elif category=="Unhealthy for Sensitive Groups":
			w_color="#ff9900"
		elif category=="Unhealthy":
			w_color="#FF0000"
		elif category=="Very Unhealthy":
			w_color="#990066"
		elif category=="Hazardous":
			w_color="#660000"
		

		root.configure(bg=w_color)
		mylabel = Label(root,text=city + " Air Quality " + str(aqi) + " " + category,font=("Helvetica",20),bg=w_color)
		mylabel.grid(row=1,column=0,columnspan=2,sticky=W+E+N+S)
	except:
		api= "Error..."


zipc = Entry(root)
zipc.grid(row=0,column=0,sticky=W+E+N+S)

zipbtn = Button(root,text="Lookup ZipCode",command=lookup)
zipbtn.grid(row=0,column=1,sticky=W+E+N+S)

root.mainloop()