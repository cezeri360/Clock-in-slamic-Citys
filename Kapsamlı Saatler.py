import datetime
import pytz
import tkinter as tk
trablus_zaman = pytz.timezone('Africa/Tripoli')
trablus_saat = datetime.datetime.now(trablus_zaman)
kahire_zaman = pytz.timezone('Africa/Cairo')
kahire_saat = datetime.datetime.now(kahire_zaman)
ceza_zaman = pytz.timezone('Africa/Algiers')
cezayir_saat = datetime.datetime.now(ceza_zaman)
ist_zaman = pytz.timezone('Europe/Istanbul')
istanbul_saat = datetime.datetime.now(ist_zaman)
fil_zaman = pytz.timezone('Asia/Gaza')
ramallah_saat = datetime.datetime.now(fil_zaman)
ur_zaman = pytz.timezone('Etc/GMT-8')
dog_saat = datetime.datetime.now(ur_zaman)
urit_zaman = pytz.timezone('Asia/Baku')
doggg_saat = datetime.datetime.now(urit_zaman)
uritiye_zaman = pytz.timezone('Europe/Tirane')
doggguke_saat = datetime.datetime.now(uritiye_zaman)
uritiyeuke_zaman = pytz.timezone('Asia/Kuala_Lumpur')
dogggukeiye_saat = datetime.datetime.now(uritiyeuke_zaman)
uritiyeukemm_zaman = pytz.timezone('Asia/Nicosia')
dogggukeiyemm_saat = datetime.datetime.now(uritiyeukemm_zaman)
uritiyecc_zaman = pytz.timezone('Asia/Kabul')
dogggukecv_saat = datetime.datetime.now(uritiyecc_zaman)
uritiyeukewq_zaman = pytz.timezone('Etc/GMT-5')
dogggukeiyeww_saat = datetime.datetime.now(uritiyeukewq_zaman)
uritiyeukemmll_zaman = pytz.timezone('Etc/GMT-5')
dogggukeiyemmqr_saat = datetime.datetime.now(uritiyeukemmll_zaman)
uritiyeukemmllşş_zaman = pytz.timezone('Etc/GMT-7')
dogggukeiyemmqrwert_saat = datetime.datetime.now(uritiyeukemmllşş_zaman)
uritiyeukemmllşşuvyz_zaman = pytz.timezone('Asia/Baghdad')
dogggukeiyemmqrwertcimcim_saat = datetime.datetime.now(uritiyeukemmllşşuvyz_zaman)
print("Trablus saati:", trablus_saat.strftime('%H:%M:%S'))
print("Kahire saati:", kahire_saat.strftime('%H:%M:%S'))
print("Cezayir saati:", cezayir_saat.strftime('%H:%M:%S'))
print("İstanbul saati:", istanbul_saat.strftime('%H:%M:%S'))
print("Ramallah saati:", ramallah_saat.strftime('%H:%M:%S'))
print("Urumçi saati:", dog_saat.strftime('%H:%M:%S'))
print("Bakü saati:", doggg_saat.strftime('%H:%M:%S'))
print("Tiran saati:", doggguke_saat.strftime('%H:%M:%S'))
print("Kuala-Lumpur saati:", dogggukeiye_saat.strftime('%H:%M:%S'))
print("Lefkoşa saati:", dogggukeiyemm_saat.strftime('%H:%M:%S'))
print("Kabil saati:", dogggukecv_saat.strftime('%H:%M:%S'))
print("İslamabad saati:", dogggukeiyeww_saat.strftime('%H:%M:%S'))
print("Nur Sultan saati:", dogggukeiyemmqr_saat.strftime('%H:%M:%S'))
print("Cakarta saati:", dogggukeiyemmqrwert_saat.strftime('%H:%M:%S'))
print("Bağdat saati:", dogggukeiyemmqrwertcimcim_saat.strftime('%H:%M:%S'))
r= tk.Tk()
r.title("ساعات المدن الإسلامية")
r.geometry("500x500+300+100")
r.configure(background="black")
yazi=tk.Label(
    text="İslam Şehirlerinde Saatler",
    fg="red",
    bg="black",
    width=30,
    height=3,
    font="Elephant"
)
yazi.pack()
def listeye_tikla(event):
    secilen = liste.get(liste.curselection())
    if secilen == "Trablus":
        sonuc_label.config(text=trablus_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Kahire":
        sonuc_label.config(text=kahire_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Cezayir":
        sonuc_label.config(text=cezayir_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "İstanbul":
        sonuc_label.config(text=istanbul_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Ramallah":
        sonuc_label.config(text=ramallah_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Urumçi":
        sonuc_label.config(text=dog_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Bakü":
        sonuc_label.config(text=doggg_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Tiran":
        sonuc_label.config(text=doggguke_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Kuala-Lumpur":
        sonuc_label.config(text=dogggukeiye_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Lefkoşa":
        sonuc_label.config(text=dogggukeiyemm_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Kabil":
        sonuc_label.config(text=dogggukecv_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "İslamabad":
        sonuc_label.config(text=dogggukeiyeww_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Nur Sultan":
        sonuc_label.config(text=dogggukeiyemmqr_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Cakarta":
        sonuc_label.config(text=dogggukeiyemmqrwert_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")
    elif secilen == "Bağdat":
        sonuc_label.config(text=dogggukeiyemmqrwertcimcim_saat.strftime('%H:%M:%S'),fg="orange",bg="black",font="Tahoma")       
liste=tk.Listbox(r)
liste.pack()
liste.insert(tk.END,"Trablus")
liste.insert(tk.END,"Kahire")
liste.insert(tk.END,"Cezayir")
liste.insert(tk.END,"İstanbul")
liste.insert(tk.END,"Ramallah")
liste.insert(tk.END,"Urumçi")
liste.insert(tk.END,"Bakü")
liste.insert(tk.END,"Tiran")
liste.insert(tk.END,"Kuala-Lumpur")
liste.insert(tk.END,"Lefkoşa")
liste.insert(tk.END,"Kabil")
liste.insert(tk.END,"İslamabad")
liste.insert(tk.END,"Nur Sultan")
liste.insert(tk.END,"Cakarta")
liste.insert(tk.END,"Bağdat")
liste.insert(tk.END,"")
liste.insert(tk.END,"")
liste.insert(tk.END,"")
liste.insert(tk.END,"")
liste.insert(tk.END,"")
sonuc_label = tk.Label(r, text="",fg="green",bg="orange",font="Impact")
sonuc_label.pack()
liste.bind("<ButtonRelease-1>", listeye_tikla)
r.mainloop()
###Dünya Saatimiz###
#التوقيت العالمي#
############



































