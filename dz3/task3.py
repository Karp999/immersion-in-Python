# # Задача №3:
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака. 

'''В большой текстовой строке подсчитать количество встречаемых слов и 
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
За основу возьмите любую статью из википедии или из документации к языку.'''

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\
 tempor incididunt ut labore et dolore magna aliqua. Lorem dolor sed viverra\
 ipsum nunc aliquet bibendum enim. Eget arcu dictum varius duis at consectetur.\
 Mauris ultrices eros in cursus turpis massa. Viverra maecenas accumsan lacus\
 vel facilisis volutpat est. In fermentum et sollicitudin ac orci phasellus\
 egestas tellus rutrum. Malesuada fames ac turpis egestas sed. Vitae sapien\
 pellentesque habitant morbi tristique senectus et netus. Mi quis hendrerit dolor\
    magna. Lorem mollis aliquam ut porttitor leo a. A iaculis at erat pellentesque\
    adipiscing. Et netus et malesuada fames ac turpis. Nunc sed blandit libero volutpat\
    sed. Tortor posuere ac ut consequat semper viverra nam libero justo.'

text = "".join([i for i in text.lower() if i.isalpha() or i == " "])
text = text.split()

n = 10
dictText = dict()
for i in text:
    dictText[i] = dictText.get(i, 0) + 1
# сортировка по количеству и по алфавиту
sortWord = sorted(dictText.items(), key=lambda x: (-x[1], x[0]))[:n]
for word, count in sortWord:
    print(f"Слово {word} встречается {count} раз")