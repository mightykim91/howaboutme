import random
import json
import os
from random import randint, choice

file_path = './dummy.json'
id_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def get_id():
    text = ""
    for i in range(6):
        text += random.choice(id_alpha)
    text += str(randint(1,99))
    return text
nick = ["기분나쁜","기분좋은","신바람나는","상쾌한","짜릿한","그리운","자유로운","서운한","울적한","비참한","위축되는","긴장되는","두려운","당당한","배부른","수줍은","창피한","멋있는", "열받은","심심한","잘생긴","이쁜","시끄러운"]
name = ["사자","코끼리","호랑이","곰","여우","늑대","너구리","침팬치","고릴라","참새","고슴도치","강아지","고양이","거북이","토끼","앵무새","하이에나","돼지","하마","원숭이","물소","얼룩말","치타", "악어","기린","수달","염소","다람쥐","판다"]
print(len(nick))
print(len(name))
gender = ['여자', '남자']
thirtyone = [1,3,5,7,8,10,12]
thirty = [4,6,9,11]
twentyeight = [2]
# year = [1971~2001]
# month = [12]
# day = [1~30]
# height = [140~200]
body = ['마른','슬림 근육','보통','근육질','통통','우람']
area = ['서울','경기도','부산']
education = ['고등학교 졸업','대학교 졸업','대학원 이상']
job = ['학생','전문직','교육직','공무원','사업가','연구,기술직','군인','기타','무직']
religion = ['무교','기독교','불교','천주교','기타']
hobby1 = ['영화보기','카페가기','코인노래방','수다떨기','여행가기','카페가기','영화보기','춤추기','맛집 탐방','쇼핑하기','볼링 치기','컴퓨터게임','요리하기','운동','독서하기','멍때리기']
hobby2 = ['영화보기','카페가기','코인노래방','수다떨기','여행가기','카페가기','영화보기','춤추기','맛집 탐방','쇼핑하기','볼링 치기','컴퓨터게임','요리하기','운동','독서하기','멍때리기']
blood = ['A','B','AB','O']
drink = ['안마심','가끔','자주','매일']
smoke = ['비흡연','술 마실 때만','가끔','자주','매일','전자담배']
intro = [
    '좋은 사람 만나고 싶어요.',
    '저는 어때요?',
    '자만추',
    '술친구해요~'
]

data = [
{
    "model":"profiles.profile",
    "pk":1,
    "fields": {
        "nickname":'hey',
        "gender":0,
        'birth':'2019-01-01',
        'height':140,
        'hobby1':'요리하기',
        'hobby2':'운동',
        'blood':'O',
        'smoke':'가끔',
        'drink':'가끔',
        'intro':'hihi',
        'age':28,
        'area_id':1,
        'job_id':1,
        'education_id':1,
        'body_id':1,
        'religion_id':1,
        'user_id':5

    }
},
{
    'model':'accounts.user',
    'pk':50,
    'fields': {
        'username':'hihi',
        'password':'ssafy1234',
    }
}]
data = []
nicks = []
ids = []
for i in range(1,101):
    user = {
        'model':'accounts.user',
        'fields': {

        }
    }

    user['pk'] = i
    user['fields']['password'] = 'ssafy1234'
    while True:
        idid = get_id()
        if idid in ids:
            continue
        ids.append(idid)
        break
    user['fields']['username'] = ids[-1]
    user['fields']['profile_saved'] = 1
    user['fields']['image_saved'] = 1
    user['fields']['similarity'] = randint(50,90)
    profile = {
        'model':'profiles.profile',
        'fields': {
            
        }
    }

    profile['pk'] = i
    while True:
        mynick = random.choice(nick)
        myname = random.choice(name)
        nickname = mynick + ' ' + myname
        print(nickname)
        print(nicks)
        if nickname in nicks:
            continue
        nicks.append(nickname)
        break
    
    profile['fields']['nickname'] = nicks[-1]
    if i < 51:
        profile['fields']['gender'] = 1
    else:
        profile['fields']['gender'] = 0
    year = random.randint(1971,2001)
    month = random.randint(1,12)
    if month in thirtyone:
        day = random.randint(1,31)
    elif month in thirty:
        day = random.randint(1,30)
    else:
        day = random.randint(1,28)
    profile['fields']['birth'] = '{}-{}-{}'.format(str(year),str(month),str(day))
    profile['fields']['height'] = randint(140,200)
    myhobby1 = random.choice(hobby1)
    print('hhh')
    while True:
        myhobby2 = random.choice(hobby2)
        if myhobby1 == myhobby2:
            continue
        break
    profile['fields']['hobby1'] = myhobby1
    profile['fields']['hobby2'] = myhobby2
    profile['fields']['blood'] = random.choice(blood)
    profile['fields']['smoke'] = random.choice(smoke)
    profile['fields']['drink'] = random.choice(drink)
    profile['fields']['intro'] = random.choice(intro)
    profile['fields']['age'] = 2021-year
    profile['fields']['area_id'] = random.randint(1,3)
    profile['fields']['job_id'] = random.randint(1,9)
    profile['fields']['education_id'] = randint(1,3)
    profile['fields']['body_id'] = randint(1,6)
    profile['fields']['religion_id'] = randint(1,5)
    profile['fields']['user_id'] = i
    print(i)
    data.append(user)
    data.append(profile)
with open(file_path, 'w', encoding='UTF-8') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)

# with open('./nicks.json','w', encoding='UTF-8-sig') as filewrite:
#     json.dump(nicks, filewrite, indent=4, ensure_ascii=False)

image_file_path = './dummy_images'
file_names = os.listdir(image_file_path)

for i,name in enumerate(file_names):
    src = os.path.join(image_file_path,name)
    dst = nicks[i]
    dst = os.path.join(image_file_path,dst)
    os.rename(src,dst)
