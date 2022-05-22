import login
import hanta
import os


if __name__ == "__main__":
	if os.path.exists("config.ht"):
		f=open("config.ht","r")
		print(f.read())
		f.close()
		app = hanta.App()
		app.start()
	else:
		app = login.Login()
		app.start()