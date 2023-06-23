import tkinter as tk
import requests
import time
import jdatetime
from bs4 import BeautifulSoup
def get_degree():
    url="https://forecast.weather.gov/MapClick.php?CityName=Los+Angeles&state=CA&site=LOX&textField1=34.0522&textField2=-118.243&e=0#.Y8bD-nZBy3A"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    p=soup.find_all('div',id='current_conditions-summary')
    p=list(p[0].children)
    print(p[2].get_text())
    return int(p[5].get_text()[:-2])
def get_temp_hum_press():
    url="https://weather.gc.ca/city/pages/qc-147_metric_e.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    p=soup.find_all('div',
                     class_='col-sm-4 brdr-rght-city')
    p0=list(p[0].children)
    p0=list(p0[0].children)
    press=p0[7].get_text()
    
    p1=list(p[1].children)
    p1=list(p1[0].children)
    temp=p1[3].get_text()
    hum=p1[-2].get_text()
    # print('temp = ',temp[:-1])
    # print('hum = ',hum)
    # print('press = ',press)
    return temp,hum,press
def write_degree2csv():    
    while True:
        with open('sanfransisco.csv','wt') as f:
             line=str(jdatetime.datetime.now())+" , "+\
                  str(get_degree())  
             print(line)
             f.write(line+"\n")
             time.sleep(2)
def publishonmqqr(temperprehum):
    import paho.mqtt.client as paho
    def on_publish(client,userdata,result):
        pass
    broker='broker.mqttdashboard.com'
    port=1883
    client1=paho.Client("controll")
    topic='arianganji'
    client1.connect(broker,port)  
    print(temperprehum)
    ret= client1.publish(topic,temperprehum)
def run():
    res=get_temp_hum_press()
    res=",".join(res)
    publishonmqqr(res)
    lb.config(text=res)      
top=tk.Tk()
fr0=tk.Frame(master=top)
fr0.pack()
fr1=tk.Frame(master=top)
fr1.pack()
lb=tk.Label(master=fr0,text='')
lb.pack()
bt=tk.Button(master=fr0,text='send',
             command=run)
bt.pack()
