'''This is the main file to run the application. It imports the splash screen and the main interface of the application'''

from Interface import splash, Interface_main


if __name__ == '__main__':
    splash.SplashScreen()
    app = Interface_main.CurrencyExchangeApp()
    app.run()



