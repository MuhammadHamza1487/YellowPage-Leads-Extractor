import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

def scrape_yellow_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    business_data = []

    # Extracting business names
    names = soup.find_all('a', class_='listing__name--link listing__link jsListingName')
    for name in names:
        business_name = name.get_text(strip=True)
        
        # Extracting phone numbers (assuming they are within the same parent element as names)
        phone_tag = name.find_next('li', class_='mlr__submenu__item')
        phone = phone_tag.h4.get_text(strip=True) if phone_tag else 'N/A'
        
        # Extracting website links
        website_tag = name.find_next('li', class_='mlr__item mlr__item--website')
        junk_website_link = website_tag.a['href'] if website_tag and website_tag.a else 'N/A'

        if junk_website_link != 'N/A':
            website_link = "https://www.yellowpages.ca/"+junk_website_link

        business_data.append({
            'Business Name': business_name,
            'Phone Number': phone,
            'Website': website_link
        })

    return business_data

def start_scraping(url, pages):
    try:
        pages = int(pages)
        # URL of the Yellow Pages search results page
        url1 = 'https://www.yellowpages.ca/search/si/'
        url2 = '/' + url.split('/search/si/')[1].split('/', 1)[1]

        # Create an empty list to store all business data
        all_data = []

        for i in range(1, pages+1):
            new_x = str(i)
            new_url = url1 + new_x + url2
            data = scrape_yellow_pages(new_url)
            all_data.extend(data)  # Append the new data to all_data list

        # Convert to DataFrame
        df = pd.DataFrame(all_data)

        # Iterate through the DataFrame to track groups of consecutive rows with matching data
        for i in range(len(df) - 1):
            # Check if the current row and the next row have the same 'Website' value
            if df.iloc[i, -1] == df.iloc[i + 1, -1]:
                df.iloc[i, -1] = 'N/A'

        # Save to Excel
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Success", f"Data has been scraped and saved to {file_path}")
        else:
            messagebox.showwarning("Warning", "No file selected for saving")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def on_scrape_button_click():
    url = url_entry.get()
    pages = pages_entry.get()
    threading.Thread(target=start_scraping, args=(url, pages)).start()

# Create the main application window
root = tk.Tk()
root.title("Yellow Pages Scraper")

# Create and place the URL label and entry
url_label = tk.Label(root, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=5)

# Create and place the pages label and entry
pages_label = tk.Label(root, text="Number of Pages:")
pages_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
pages_entry = tk.Entry(root, width=50)
pages_entry.grid(row=1, column=1, padx=10, pady=5)

# Create and place the scrape button
scrape_button = tk.Button(root, text="Scrape", command=on_scrape_button_click)
scrape_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
