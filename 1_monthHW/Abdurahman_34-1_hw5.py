print("Home Work №5\n")

Geeks = {

    'address': 'Toktogula 175',

    'courses': ['Android', 'Backend', 'Frontend'],

    'bag': {'fails', 'errors', 'stack'}

}

del Geeks['bag']

Geeks['address'] = 'Ibraimova 103, 4 floor'

Geeks['number'] = '+996 506 052 018'
Geeks['instagram'] = 'geeks_edu'

new_courses = ['UX/UI', 'IOS', 'project manager', 'Basics of programming', 'Programming for KIDS']
Geeks['courses'].extend(new_courses)
Geeks['courses'] = set(Geeks['courses'])

Geeks['foundation date'] = '2018'

count_courses = len(Geeks['courses'])
Geeks['count courses'] = count_courses

for keys, value in Geeks.items():
    print(f'{keys} : {value}')
