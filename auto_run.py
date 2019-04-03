'''
for green square
'''
import os
from datetime import datetime, timedelta, timezone

# 删除最后一行
#os.system("sed -i '$d' README.md")

# 添加日期
# 世界协调时间
# 2019-04-03 15:11:01.899728+00:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# utc_dt = datetime.utcnow()  2019-04-03 15:11:01.899728

# 北京时间在该时区的+8 UTC+8  2019-04-03 23:11:01.899728+08:00
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))

content = "Auto update by robot instead of human(hzz) "
with open("README_update.md","w") as f:
    f.write(content+"at: {}".format(bj_dt.strftime('%Y-%m-%d %H:%M:%S')))
#os.system('echo '+content+'Last update : {} >> README.md'.format(bj_dt.strftime('%Y-%m-%d %H:%M:%S')))

os.system("git add README_update.md")
os.system('git commit -m "update"')
os.system('git push')
