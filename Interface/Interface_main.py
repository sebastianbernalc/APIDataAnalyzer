import tkinter
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
from matplotlib import pyplot as plt
import numpy as np
import requests
from tkcalendar import DateEntry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

class CurrencyExchangeApp:
    def __init__(self):
        self.app = customtkinter.CTk()  # creating custom tkinter window
        self.app.geometry("800x440")
        self.app.title('Currency Exchanges')
        
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        
        self.img1 = ImageTk.PhotoImage(Image.open("./Images/back.jpg"))
        self.l1 = customtkinter.CTkLabel(master=self.app, image=self.img1)
        self.l1.pack()
        
        # creating custom frame
        self.frame = customtkinter.CTkFrame(master=self.l1, width=320, height=250, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        self.l2 = customtkinter.CTkLabel(master=self.frame, text="Select an option ", font=('REFOLTER', 20))
        self.l2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        
        # Create custom button
        self.button1 = customtkinter.CTkButton(
            master=self.frame, 
            width=220, 
            font=('REFOLTER', 11), 
            text="Currency Exchange", 
            command=self.currency_exchange, 
            corner_radius=6, 
            fg_color="#ffffff", 
            bg_color="#1c5715", 
            text_color="#1c5715", 
            hover_color="#89a985"
        )
        self.button1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        
        self.button2 = customtkinter.CTkButton(
            master=self.frame, 
            font=('REFOLTER', 11), 
            width=220, 
            text="Stats", 
            command=self.stats, 
            corner_radius=6, 
            fg_color="#ffffff", 
            bg_color="#1c5715", 
            text_color="#1c5715", 
            hover_color="#89a985"
        )
        self.button2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    
        self.frame_2 = customtkinter.CTkFrame(master=self.l1, width=320, height=350, corner_radius=15)
        self.frame_2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.frame_2.lower()  # Ensure frame_2 is not visible initially

        self.l3 = customtkinter.CTkLabel(master=self.frame_2, text="Currency Exchange", font=('REFOLTER', 20))
        self.l3.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.option_menu_from = customtkinter.CTkOptionMenu(
            master=self.frame_2, 
            font=('REFOLTER', 11), 
            width=220, 
            corner_radius=6, 
            values=["From"], 
            fg_color="#ffffff", 
            text_color="#1c5715"
        )
        self.option_menu_from.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.option_menu_to = customtkinter.CTkOptionMenu(
            master=self.frame_2, 
            font=('REFOLTER', 11), 
            width=220, 
            corner_radius=6, 
            values=["To"], 
            fg_color="#ffffff", 
            text_color="#1c5715"
        )
        self.option_menu_to.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.entry_amount = customtkinter.CTkEntry(
            master=self.frame_2, 
            width=220, 
            font=('REFOLTER', 11), 
            corner_radius=6, 
            fg_color="#ffffff", 
            bg_color="#1c5715", 
            text_color="#1c5715"
        )
        self.entry_amount.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        self.button_convert = customtkinter.CTkButton(
            master=self.frame_2, 
            font=('REFOLTER', 11), 
            width=220, 
            text="Convert", 
            corner_radius=6, 
            fg_color="#ffffff", 
            bg_color="#1c5715", 
            text_color="#1c5715", 
            hover_color="#89a985", 
            command=self.Exchange
        )
        self.button_convert.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

        self.l1_result = customtkinter.CTkLabel(master=self.frame_2, text="Result: ", font=('REFOLTER', 20))
        self.l1_result.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)  # Move it slightly lower to fit in the frame
        
        self.button_back = customtkinter.CTkButton(
            master=self.frame_2, 
            font=('REFOLTER', 11), 
            width=220, 
            text="Back", 
            corner_radius=6, 
            fg_color="#ffffff", 
            bg_color="#1c5715", 
            text_color="#1c5715", 
            hover_color="#89a985", 
            command=self.back_to_main
        )
        self.button_back.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        self.frame_3 = customtkinter.CTkFrame(master=self.l1, width=320, height=350, corner_radius=15)
        self.frame_3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.frame_3.lower()  # Ensure frame_3 is not visible initially
        
        self.l4 = customtkinter.CTkLabel(master=self.frame_3, text="Statistics", font=('REFOLTER', 20))
        self.l4.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        self.l = customtkinter.CTkLabel(master=self.frame_3, text="Select a date", font=('REFOLTER', 15))
        self.l.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.date_entry = DateEntry(master=self.frame_3, width=27, background='#1c5715',
                            foreground='white', borderwidth=2, year=2024, font = ('REFOLTER', 11), date_pattern='y-mm-dd')
        self.date_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.option_menu_to_currency = customtkinter.CTkOptionMenu(
            master=self.frame_3, 
            font=('REFOLTER', 11), 
            width=220, 
            corner_radius=6, 
            values=["Currency"], 
            fg_color="#ffffff", 
            text_color="#1c5715"
        )
        self.option_menu_to_currency.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.button_stats = customtkinter.CTkButton(
            master=self.frame_3, 
            font=('REFOLTER', 11), 
            width=220, 
            text="Get Stats", 
            corner_radius=6, 
            fg_color="#ffffff", 
            bg_color="#1c5715", 
            text_color="#1c5715", 
            hover_color="#89a985",
            command=self.stats_graph
        )
        self.button_stats.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        self.button_back_3 = customtkinter.CTkButton(
            master=self.frame_3, 
            font=('REFOLTER', 11), 
            width=220, 
            text="Back", 
            corner_radius=6, 
            fg_color="#ffffff", 
            bg_color="#1c5715", 
            text_color="#1c5715", 
            hover_color="#89a985", 
            command=self.back_to_main
        )
        self.button_back_3.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

        # Fetch currencies from API and update option menu
        self.fetch_currencies()
    
    def fetch_currencies(self):
        try:
            response = requests.get("https://api.frankfurter.app/currencies")
            response.raise_for_status()  # Raise an error for bad status codes
            data = response.json()

            self.currencies = list(data.keys())

            # Update the option menu with fetched currencies
            self.option_menu_from.configure(values=self.currencies)
            self.option_menu_to.configure(values=self.currencies)
            self.option_menu_to_currency.configure(values=self.currencies)
        except requests.RequestException as e:
            print(f"Error fetching currencies: {e}")
    
    def currency_exchange(self):
        self.frame.lower()  # Hide frame
        self.frame_2.lift()  # Show frame_2
        print("Currency Exchange")

    def stats(self):
        self.frame.lower()  # Hide frame
        self.frame_3.lift()  # Show frame_3

    def back_to_main(self):
        self.frame_2.lower()  # Hide frame_2
        self.frame_3.lower()  # Hide frame_3
        self.frame.lift()  # Show main frame

    def Exchange(self):
        if self.option_menu_from.get() == "From" or self.option_menu_to.get() == "To":
            messagebox.showerror("Error", "You must select currencies")
        elif self.option_menu_from.get() == self.option_menu_to.get():
            messagebox.showerror("Error", "You must select different currencies")
        elif self.entry_amount.get() == "":
            messagebox.showerror("Error", "You must enter an amount")
        elif not self.entry_amount.get().isnumeric() and not self.entry_amount.get().replace('.', '', 1).isdigit():
            messagebox.showerror("Error", "Amount must be a number")
        else:
            try:
                url = f"https://api.frankfurter.app/latest?amount={self.entry_amount.get()}&from={self.option_menu_from.get()}&to={self.option_menu_to.get()}"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    print(data['rates'][self.option_menu_to.get()])
                    self.l1_result.configure(text=f"Result: {data['rates'][self.option_menu_to.get()]} {self.option_menu_to.get()}")
                else:
                    messagebox.showerror("Error", "Failed to get exchange rate")
            except requests.RequestException as e:
                print(f"Error fetching currencies: {e}")
    
    def stats_graph(self):
        self.dates = []
        self.rates = []
        self.coin = []
        
        try:
            url = f"https://api.frankfurter.app/{self.date_entry.get_date()}..?to={self.option_menu_to_currency.get()}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for date, rate in data['rates'].items():
                    self.dates.append(date)
                    for moneda, tasa in rate.items():
                        self.rates.append(tasa)
                        self.coin.append(moneda)

                self.frame_3.lower()  # Hide frame
                # Create the plot
                dates_numeric = np.arange(len(self.dates))  # Convert dates to numeric values for regression
                rates_numeric = np.array(self.rates)
                coefficients = np.polyfit(dates_numeric, rates_numeric, 1)  # Linear fit (degree 1)
                linear_trend = np.polyval(coefficients, dates_numeric)

                fig, ax = plt.subplots(figsize=(10, 8))
                ax.plot(self.dates, self.rates, marker='o', linestyle='-', color='b', label=self.coin[0])
                ax.plot(self.dates, linear_trend, color='r', linestyle='--', label='Trend line')  # Trend line

                ax.set_title('Currency Exchange Rate')
                ax.set_xlabel('Date')
                ax.set_ylabel('Rate')
                ax.legend()
                plt.xticks(rotation=60)

                # Create a canvas for the plot
                self.canvas = FigureCanvasTkAgg(fig, master=self.l1)
                self.canvas.draw()
                self.canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)

                # Add a button to return to the stats frame
                self.button_back_graph = customtkinter.CTkButton(
                    master=self.l1,
                    text="Back",
                    command=self.back_to_stats_frame,
                    font=('REFOLTER', 11),
                    corner_radius=6,
                    fg_color="#ffffff",
                    bg_color="#1c5715",
                    text_color="#1c5715",
                    hover_color="#89a985"
                )
                self.button_back_graph.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

            else:
                messagebox.showerror("Error", "Failed to get exchange rate")
        except requests.RequestException as e:
            print(f"Error fetching currencies: {e}")

    def back_to_stats_frame(self):
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()  # Remove the plot canvas
        if hasattr(self, 'button_back_graph'):
            self.button_back_graph.destroy()  # Remove the additional back button
        self.frame_3.lift()  # Show the stats frame

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    app = CurrencyExchangeApp()
    app.run()
