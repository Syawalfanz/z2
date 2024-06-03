import tkinter as tk
import tkinter.messagebox as messagebox
from parcel_calculator import calculate_price
from Conn import connect_to_mysql

def save_parcel_details(length, width, height, weight):
    with open("parcel_details.txt", "a") as file:
        file.write(f"Length: {length} cm, Width: {width} cm, Height: {height} cm, Weight: {weight} kg\n")

def reset_fields_file():
    with open("parcel_details.txt", "w") as file:
        file.write("")  # Clear the contents of the file

class ParcelCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Parcel Calculator")
        
        # Create length input label and entry field
        self.length_label = tk.Label(master, text="Length (cm):")
        self.length_label.grid(row=0, column=0, padx=10, pady=5)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Create width input label and entry field
        self.width_label = tk.Label(master, text="Width (cm):")
        self.width_label.grid(row=1, column=0, padx=10, pady=5)
        self.width_entry = tk.Entry(master)
        self.width_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Create height input label and entry field
        self.height_label = tk.Label(master, text="Height (cm):")
        self.height_label.grid(row=2, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(master)
        self.height_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Create weight input label and entry field
        self.weight_label = tk.Label(master, text="Weight (kg):")
        self.weight_label.grid(row=3, column=0, padx=10, pady=5)
        self.weight_entry = tk.Entry(master)
        self.weight_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Create calculate button
        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate_price)
        self.calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Create reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_fields)
        self.reset_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        
        # Create price label
        self.price_label = tk.Label(master, text="")
        self.price_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
    
    def calculate_price(self):
        try:
            # Get parcel dimensions and weight from entry fields
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())

            # Save parcel details to file
            save_parcel_details(length, width, height, weight)

            # Calculate parcel price using imported function
            volume, price = calculate_price(length, width, height, weight)

            # Connect to MySQL server
            conn = connect_to_mysql()
            
            if conn:
                try:
                    # Generate item_id
                    item_id = f"ITEM-{length}-{width}-{height}"
                    
                    # Insert data into the database
                    cursor = conn.cursor()
                    cursor.execute('''INSERT INTO shipments (item_id, item_height, item_width, item_length, item_volume, item_price)
                                      VALUES (%s, %s, %s, %s, %s, %s)''', (item_id, str(height), str(width), str(length), str(volume), str(price)))
                    conn.commit()
                    cursor.close()
                    
                    # Notify the user that the data has been stored
                    messagebox.showinfo("Success", f"Volume: {volume} cm³\nThe price of your parcel is: RM{price}\nData has been stored in the database.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {str(e)}")
                finally:
                    # Close MySQL connection
                    if conn.is_connected():
                        conn.close()
            else:
                messagebox.showerror("Error", "Failed to connect to the database.")
                
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for dimensions and weight.")
    
    def reset_fields(self):
        # Clear all input fields
        self.length_entry.delete(0, tk.END)
        self.width_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.price_label.config(text="")
        # Reset parcel details file
        reset_fields_file()

def main():
    # Create the main application window
    root = tk.Tk()
    
    # Create an instance of the ParcelCalculatorGUI class
    parcel_calculator_gui = ParcelCalculatorGUI(root)
    
    # Start the application's main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
