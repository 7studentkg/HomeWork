print('Home Work №8 - Работа с файлами.\n')


result_dict = {}
with open('results.txt', 'r') as file:
    #print(file.read)

    lines = file.readlines()

    for i in lines:
        parts = i.split()

        key = parts[0]
        if parts[1].isdigit():
            value = int(parts[1])
        else:
            value = parts[1]
        result_dict[key] = value


result_dict.pop('34-1')
sorted_result = dict(sorted(result_dict.items(), key=lambda x: x[1], reverse=True))

top_result = [f'{k} - {v}' for k, v in sorted_result.items()]

sorted_result = {'34-1': 'RESULTS', **sorted_result}

results = []
for k, v in sorted_result.items():
   results.append(f'{k} - {v}')
   result = '\n'.join(results)

with open('sorted_results.txt', 'w', encoding='utf-8') as file:
    file.write(result)

print(f'Топ 3 лучших студенда по оценкам')
for i in top_result[:3]:
    print(i)
