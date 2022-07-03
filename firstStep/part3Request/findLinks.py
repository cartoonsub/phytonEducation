
import requests
import re

pattern = r'href=(?:[\"\']\w+://|[\"\'])([^.]{1,}[\w.-]+)'

text = r'''<li><a href="http://redir.rbc.ru/cgi-bin/redirect.cgi?http://hc.ru/ru/">Хостинг</a></li> #ссылку из редиректа ﻿(hc.ru/ru) не ловим!!
<li><a href="http://www.m-2.ru/">M2</a></li>
<a target="_top" href="http://banner.rbc.ru/banredir.cgi?lid=firstpage_left" empty="true" style="display:none"></a></div>
<li><a href="http://www.biztorg.ru/search.shtml?cfg=biztorg&type=S">Предложения о продаже</a></li>
<li><a href="http://biztorg.ru:80/main_services_new.shtml">Оценка бизнеса</a></li>
<a href="http://static.feed.rbc.ru/rbc/internal/rss.rbc.ru/rbcdaily.ru/mainnews.rss" class="flRight small" style="margin:0 0 0 5px;">'''

match = re.findall(pattern, text)
match.sort()

for url in sorted(set(match)):
    print(url)

import requests
import re

pattern = r'<a.+?href=(?:[\"\']\w+://|[\"\'])([^.]{1,}[\w.-]+)'
link = input()
result = requests.get(link)
text = format(result.content)
match = re.findall(pattern, text, re.IGNORECASE)
for url in sorted(set(match)):
    print(url)

