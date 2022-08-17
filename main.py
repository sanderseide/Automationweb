from selenium import webdriver
import time
web = webdriver.Chrome()
web.get('https://unifa-edu.info/contenu/mon-unifa/portail-etudiant/formulaire-de-demande-dattestation-et-de-releve-de-notes/')

time.sleep(1)
Prenon= "Sander"
preno = web.find_element("xpath",'//*[@id="wpforms-15500-field_5"]')
preno.send_keys(Prenon)

Non_fanmi_ou = "Seide"
Non_fanmi = web.find_element("xpath", '//*[@id="wpforms-15500-field_5-last"]')
Non_fanmi.send_keys(Non_fanmi_ou)

Nimero_paspo_ou = "48957we6"
Nimero_pas = web.find_element("xpath", '//*[@id="wpforms-15500-field_6"]')
Nimero_pas.send_keys(Nimero_paspo_ou)

Konfime_paspo_ou = " re555677"
Konfime_pas = web.find_element("xpath", '//*[@id="wpforms-15500-field_7"]')
Konfime_pas.send_keys(Konfime_paspo_ou)

Adrese_electronik_ou = " mitelson070@gmail.com"
Adres_elektronik = web.find_element("xpath", '//*[@id="wpforms-15500-field_16"]')
Adres_elektronik.send_keys(Adrese_electronik_ou)


btn = web.find_element("xpath", '//*[@id="wpforms-submit-15500"]')
btn.click()

# txt = web.find_element_by_css_selector('editHTML take class')
# if ((txt.text) == "the text you take in the site") :
#     print("sucess")




