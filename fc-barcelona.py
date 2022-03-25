from bs4 import BeautifulSoup
import requests
import requests_cache


requests_cache.install_cache('demo_cache')


url = 'https://fbref.com/fr/equipes/206d90db/Barcelona-Stats'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

# Stats


stats = soup.select_one(
    'table[id^="stats_standard_11174"]')


title_stats = stats.caption.get_text()

header_stats = stats.thead
body_stats = stats.tbody


fields = []
sub_fields = []
players = []

for th in header_stats.find_all('tr')[0].find_all('th'):
    fields.append(th.get_text())

for th in header_stats.find_all('tr')[1].find_all('th'):
    sub_fields.append(th.get_text())

for tr in body_stats.find_all('tr'):
    player = []
    player.append(tr.th.get_text())
    for td in tr.find_all('td'):
        player.append(td.get_text())
    players.append(player)

fields[0] = sub_fields[0]
sub_fields[0] = 'Nom'


schema = [4, 4, 7, 5, 4, 5, 1]

values = []

for p in players:
    i = 0
    sbs = list(sub_fields)
    value = {}
    for f in fields:
        count = schema[i]
        value[f] = {}
        for c in range(0, count):
            value[f][sbs[0]] = p[0]
            sbs.remove(sbs[0])
            p.remove(p[0])
        i += 1
    values.append(value)


data_stats = {
    title_stats: values,
}

# Calendar


calendar = soup.select_one(
    'table[id^="matchlogs_for"]')


title_calendar = calendar.caption.get_text()

header_calendar = calendar.thead
body_calendar = calendar.tbody


fields_calendar = []

infos = []

for th in header_calendar.find_all('tr')[0].find_all('th'):
    fields_calendar.append(th.get_text())

for tr in body_calendar.find_all('tr'):
    info = []
    info.append(tr.th.get_text())
    for td in tr.find_all('td'):
        info.append(td.get_text())
    infos.append(info)
lines = []

for i in infos:
    line = {}
    count = 0
    for v in i:
        line[fields_calendar[count]] = v
        count += 1
    lines.append(line)


data_calendar = {

    title_calendar: lines,

}

all_data = []
all_data.append(data_stats)
all_data.append(data_calendar)


print(all_data)

# shoots


'''

table_shoots = soup.select_one(
    'table[id^="stats_shooting_11174"]')

title_shoots = table_shoots.caption.get_text()

header_shoots = table_shoots.thead
body_shoots = table_shoots.tbody

fields_shoots = []
sub_fields_shoots = []
shoots = []

for th in header_shoots.find_all('tr')[0].find_all('th'):
    if len(th.get_text()) <= 0:
        continue
    fields_shoots.append(th.get_text())

for th in header_shoots.find_all('tr')[1].find_all('th'):
    sub_fields.append(th.get_text())

for tr in body_shoots.find_all('tr'):
    player = []
    player.append(tr.th.get_text())
    for td in tr.find_all('td'):
        player.append(td.get_text())
    players.append(player)

custom_fieds = {
    'Standard': {
        "count": 12,
        "start": 5,
        "end": 16
    },
    'Attendu': {
        "count": 5,
        "start": 17,
        "end": 21
    },
}

lines = []

for s in shoots:
    line = {}
    count = 0
    for v in s:
        if count >= custom_fieds['Standard']['start'] and count <= custom_fieds['Standard']['end']:
          for f in fields:
                  count = schema[i]
                  value[f] = {}
                  for c in range(0, count):
                      value[f][sbs[0]] = p[0]
                      sbs.remove(sbs[0])
                      p.remove(p[0])
                  i += 1
              values.append(value)
        else:
          line[sub_fields[count]] = v
          count += 1
    lines.append(line)

print(lines)
'''
