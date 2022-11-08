from asyncore import read
from fileinput import close



file_story = open('story.txt','r')
file_story = file_story.read()
words = file_story.split(' ')
num_words = 'кількість слів: ' + str(len(words))
sentence = file_story.split('.')
num_sentence = 'кількість речень: ' + str(len(sentence))


#нижче останні 4 ел добавляю..
item = ''
most_viewed_num = []
most_viewed = []
i = 0
for el in words:
    if words.count(el) > i:
        i = words.count(el)
        item = el
most_viewed.append(item)

for el in words:
    if words.count(el) == i:
        most_viewed.append(el)

if len(set(most_viewed)) < 4:
    i = i-1
    for el in words:
        if words.count(el) == i:
            most_viewed_num.append(el)

most_viewed = most_viewed + most_viewed_num
if len(set(most_viewed)) < 4:
    most_viewed_num = []
    num = 4 - len(set(most_viewed))
    i = i-1
    for el in words:
        if words.count(el) == i:
            most_viewed_num.append(el)
#перевірка чи всі 4 і добавляю, яких не достає...
if len(set(most_viewed_num)) > num:
    most_viewed_num = set(most_viewed_num)
    last_1 = []
    for i in most_viewed_num:
        last_1.append(i)
    last_1 = last_1[0:num]
#кінець:
most_viewed = most_viewed + last_1
most_viewed = set(most_viewed)
#лишилось усе це записати до інших txt*

f_num_sentence = open('num_story_sentence.txt','wt')
f_num_sentence.write(num_sentence)
f_num_sentence.close()

f_num_sentence = open('num_story_words.txt','wt')
f_num_sentence.write(num_words)
f_num_sentence.close()

f_num_sentence = open('story_4mostvived.txt','wt')
for index in most_viewed:
    f_num_sentence.write(index + '\n')
f_num_sentence.close()