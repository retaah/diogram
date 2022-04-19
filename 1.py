import json
import matplotlib.pyplot as plt


days = []
quantities = []
filename = 'series_SUGAR.json'
with open(filename) as jf:
    data = json.loads(jf.read())
    data = data['data']['rates']
    for line in data:
        try:
            count = data[line]['SUGAR']
            day = line
            days.append(day)
            quantities.append(count * 0.45)
        except:
            pass

plt.title('sugar for $1')
plt.ylabel('quantity')
crop_days = list(range(0, 190, 10))
plt.xticks(crop_days, rotation=45, fontsize=4)
plt.plot(days, quantities, color='#e834eb', linewidth=4)
plt.savefig('gas.jpg')
plt.show()
