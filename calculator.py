import json

# 1 выбор профильного предмета из массива

def select_item(items, index):
    selected_item = ""
    selected_item = (items[index-1])
    return selected_item

prof_objects = ["ИКТ", "Физика", "Химия", "Обществознание", "История"]
prof_objects_dat = ["ИКТ", "Физике", "Химии", "Обществознанию", "Истории"]
prof_objects_forjson = ['IT', 'Physics', 'Chemistry', 'Social Science', 'History']

print("Выберите профильный предмет:")
for i in range(5):
    print(i+1, '. ', prof_objects[i])

n = int(input())
selected_prof_object = select_item(prof_objects_dat, n)
json_oblect = prof_objects_forjson[n-1]

# 2 запрашиваем баллы по 3 предметам и считаем их сумму 

prof_math = 0
rus_lang = 0
prof = 0

print("Введите баллы по Математике:", end=' ')
prof_math = int(input())
print("Введите баллы по Русскому языку:", end=' ')
rus_lang = int(input())
print("Введите баллы по", selected_prof_object, end=': ')
prof = int(input())

score = prof_math + rus_lang + prof
print("Сумма ваших баллов: ", score)

# 3 выбор подходящих дисциплин и вывод данных пользователю 

# проверка на прохождение на бюджет 
def satisfies_budget_condition(block, scores):
    budget = block['exam_scores']['budget']
    if budget == '-':
        return False
    return int(budget.split('/')[0]) >= scores

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


for block in data:
    if satisfies_budget_condition(block, score):
        print(f"{block['code']} {block['name']}")
        print(f"проход.балл/кол-во мест")
        print(f"Договор: {block['exam_scores']['contract']}")
        print(f"Бюджет: {block['exam_scores']['budget']}\n")

