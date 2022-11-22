import tkinter as tk
import requests
from bs4 import BeautifulSoup

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        tempe = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)

    except:
        final_str = 'There was a problem retrieving that information'
        return final_str


USER_AGENT={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}


def fetch_data(city):
    google_url='https://www.google.com/search?q={}&h1={}'.format("weather", "en")
    response=requests.get(google_url, headers=USER_AGENT)
    response.raise_for_status()
    weather = response.text
    label['text'] = format_response(weather)
    #text1= fetch_data()
    soup=BeautifulSoup(weather, 'html.parser')
    city=soup.find_all('div', attrs={'class': 'vk_h'})
    time=soup.find_all('div', attrs={'class': 'vk_sh'})
    condition=soup.find_all('div', attrs={'id' : 'wob_dcp'})
    temp=soup.find_all('span', attrs={'class' :'wob_t'})
#print('Current Location: '+city[0].get_text())
#print('Day and Time: '+time[0].get_text())
#print('Weather Condition: '+condition[0].get_text())
#print('Temperature: '+temp[0].get_text())

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=40, command=lambda: fetch_data(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()