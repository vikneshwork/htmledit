import os
from bs4 import BeautifulSoup

# Opening the file ----------------------

with open("testdata2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Work for single table ================================

# tables = soup.find('table', class_='results')

# for td in tables.find_all('td'):
#     # print(td.text)
#     x = x + 1
#     print(x)
#     if td.text == '10021':
#         tables.extract()


# Saving Output ----------------------------

# with open("output1.html", "w", encoding='utf-8') as file:
#     file.write(str(soup))

# Current Testing ==============================

# table =soup.select('table')[-1]

# List of Key Variables
plugin_id = '10021'  # The Plugin Id
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
                    rm_risk_no = int(rm_alert.select('td')[2].text)
                    # Removing the Alert
                    alert_td.parent.extract()
                    for row in summary_tb.findAll('tr'):
                        try:
                            c_row = (str(row.select('td')[0].text)).strip()
                            if c_row == rm_risk_level:
                                row_no = row.select('td')[1]
                                new_no = int(row_no.text) - rm_risk_no
                                row_no.replaceWith(str(new_no))
                        except:
                            continue

# Testing Zone ------------------------------------

# if rm_risk_level == 'False Positives:':
#     print("Yes")
# else:
#     if rm_risk_level == 'Informational':
#         print("Yes2")
#     else:
#         if rm_risk_level == 'Low':
#             print("Yes3")
#         else:
#             if rm_risk_level == 'Medium':
#                 print("Yes4")
#             else:
#                 if rm_risk_level == 'High':
#                     print("Yes5")


# for row in summary_tb.findAll('tr'):
#     try:
#         c_row = (str(row.select('td')[0].text)).strip()
#         if c_row == rm_risk_level:
#             row_no = row.select('td')[1]
#             new_no = int(row_no.text) - rm_risk_no
#             row_no.replaceWith(str(new_no))
#     except:
#         continue

# print(str(summary_tb.text).strip())

# high_row = summary_tb.select('tr')[1]
# high_no = high_row.select('td')[0].text
# print(high_no)


# high_row = summary_tb.select('tr')[1]
# print(high_row.text)
# high_no = high_row.select('td')[1]
# new_high = int(high_no.text) - rm_risk_no
# high_no.replaceWith(str(new_high))
#
# print("After ---------------")
# print(high_row.text)

# Saving the output --------------------------------
# os.remove("output2.html")
with open("output2.html", "w", encoding='utf-8') as file:
    file.write(str(soup))
