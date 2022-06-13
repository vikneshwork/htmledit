from bs4 import BeautifulSoup

# Opening the file ----------------------

with open("testdata3.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# List of Key Variables
plugin_id = None  # Default Plugin ID value
# plugin_id = '10202'  # The Plugin Id
tables = soup.findAll("table")  # The list of all tables
alerts_tb = soup.find('table', class_='alerts')  # The alert table
summary_tb = soup.find('table', class_='summary')  # The summary table
rm_table = None  # Table to be removed
rm_alert = []  # Alert details to be removed

# Additional description
# table = Individual tables
# td = Individual td in table
# rm_table = Name of the table to be removed
# alert td = Individual td in the alert table
# rm_risk_level = Risk level to be changed
# rm_risk_no = Value of change


# User Input Plugin ID
plugin_id = input("Plugin ID: ")
plugin_id = plugin_id.strip()
if plugin_id is None or plugin_id == "":
    exit("Plugin ID is Empty")

# Finding the table based on Plugin ID and removes it
for table in tables:
    for td in table.find_all('td'):
        if td.text == plugin_id:
            rm_table = (table.select('th')[1]).text
            table.extract()
            # Removing the error from the Alerts table
            for alert_td in alerts_tb.find_all('td'):
                if str(alert_td.text) == str(rm_table):
                    # Storing Information of the Alert
                    rm_alert = alert_td.parent
                    rm_risk_level = str(rm_alert.select('td')[1].text)
                    rm_risk_no = 1
                    # Removing the Alert
                    alert_td.parent.extract()
                    # Reducing Risk Numbers
                    for row in summary_tb.findAll('tr'):
                        try:
                            ch_row = (str(row.select('td')[0].text)).strip()
                            if ch_row == rm_risk_level:
                                row_no = row.select('td')[1]
                                new_no = int(row_no.text) - rm_risk_no
                                target = row_no.select_one('div')
                                target.string.replaceWith(str(new_no))
                        except:
                            continue

with open("output2.html", "w", encoding='utf-8') as file:
    file.write(str(soup))
