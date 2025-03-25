import numpy as np

# HW4_程式練習 (II)

## 題目一 (25%)
numbers = [51, 30, 78, 20, 96, 40, 62]
print("第一個數字：", numbers[0])
print("第三個數字：", numbers[2])
print("最後一個數字：", numbers[-1])

print("最大值：", max(numbers))
print("最小值：", min(numbers))
numbers.sort()
print("由小到大排序：", numbers)
print("總和：",sum(numbers))
print("平均值：" , sum(numbers)/len(numbers))
new_numbers = []
for i in numbers:
  if i >= 50:
    new_numbers.append(i)
print(new_numbers)

## 題目二 (25%)

asian_countries = {
    'Taiwan': 'Taipei',
    'Japan': 'Tokyo',
    'South Korea': 'Seoul',
    'Myanmar': 'Yangon',
    'Germany': 'Berlin'
    }

print('字典:', asian_countries)
asian_countries['Myanmar'] = 'Naypyidaw'
asian_countries.pop('Germany')
asian_countries['Thailand'] = 'Bangkok'
print('新字典:', asian_countries)
sorted_asian_countries = sorted(asian_countries.items())
print('排序後新字典:', sorted_asian_countries)


## 題目三 (25%)

scores = {
    "Linda": [85, 90, 78],
    "Richard": [72, 88, 91],
    "Una": [90, 85, 87],
    "Brian": [60, 75, 70]
}


for name, score in scores.items():
  avg = sum(score)/len(score)
  if avg >= 85:
    comment = '優秀'
  elif avg >= 70:
    comment = '及格'
  else:
    comment = '需加強'
  print(name, '平均分數:', f"{avg:.2f}", '評語:', comment)

total_avg = sum([sum(score) for score in scores.values()]) / sum([len(score) for score in scores.values()])
print('全班平均分數:', f"{total_avg:.2f}")

max_avg = max([sum(score) / len(score) for score in scores.values()])
max_name = [name for name, score in scores.items() if sum(score) / len(score) == max_avg][0]
print('平均分數最高的學生:', max_name, '平均分數:', f"{max_avg:.2f}")

## 題目四 (25%)
class check_password:
  def __init__(self, password):
    self.password = password
  def check_password(self):
    if len(self.password) > 5 and any(c.isupper() for c in self.password) and any(c.islower() for c in self.password) and any(c.isdigit() for c in self.password) and ' ' not in self.password:
      return 'Valid Password'
    else:
      return 'INVALID'

print(check_password("GenAI4Humanities").check_password())
print(check_password("genai4humanities").check_password())
print(check_password("GENAI4HUMANITIES").check_password())
print(check_password("GenAIGenAI").check_password())
print(check_password("GenAI 2025").check_password())
print(check_password("GenAI").check_password())

