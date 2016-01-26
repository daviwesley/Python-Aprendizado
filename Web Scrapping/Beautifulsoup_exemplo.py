#!C:\Python27\python.exe

from bs4 import BeautifulSoup

html = """
  <table class="details" border="0" cellpadding="5" cellspacing="2" width="95%">
    <tr valign="top">
      <th>Tests</th>
      <th>Failures</th>
      <th>Success Rate</th>
      <th>Average Time</th>
      <th>Min Time</th>
      <th>Max Time</th>
   </tr>
   <tr valign="top" class="Failure">
     <td>103</td>
     <td>24</td>
     <td>76.70%</td>
     <td>71 ms</td>
     <td>0 ms</td>
     <td>829 ms</td>
  </tr>
</table>"""

soup = BeautifulSoup(html,"html.parser")#corrige exibição de alerta
table = soup.find("table", attrs={"class":"details"})

# The first tr contains the field names.
headings = [th.get_text() for th in table.find("tr").find_all("th")]

datasets = []
for row in table.find_all("tr")[1:]:
    dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
    datasets.append(dataset)

for dataset in datasets:
    for field in dataset:
        print "{0:<16}: {1}".format(field[0], field[1])
