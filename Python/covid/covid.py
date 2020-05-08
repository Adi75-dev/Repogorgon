import COVID19Py
covid19 = COVID19Py.COVID19(data_source="csbs")
latest = covid19.getLatest()
changes = covid19.getLatestChanges()
data = covid19.getAll()
print(changes)
