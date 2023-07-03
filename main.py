
import re
# Исходный текст
text = """Lorem malesuada ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae fringilla ex. Nullam consectetur sem 
vitae nulla lacinia, sed auctor urna volutpat. Quisque sollicitudin ipsum a neque consectetur, non pellentesque 
tortor laoreet. Proin convallis ligula eget dui venenatis, vel gravida justo faucibus. Integer porttitor libero eget 
mi facilisis, sed cursus metus facilisis. Nullam eleifend nulla sed semper consectetur. Suspendisse non tincidunt 
urna, vel aliquam velit. Morbi eu fermentum arcu. Mauris tristique tortor ac tortor luctus, sed luctus mi bibendum. 
Nullam posuere purus vel ligula vulputate, nec efficitur leo tristique. Fusce vestibulum ultrices ex vitae consequat. 
Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec non arcu quis ex 
dapibus eleifend. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae.

Praesent ac bibendum arcu, a tristique velit. Nullam tincidunt, lorem sit amet euismod porttitor, massa lacus 
tristique velit, nec fringilla nunc nulla eget tortor. Sed luctus auctor metus, ac malesuada velit aliquet sed. Duis 
pellentesque, eros ut volutpat facilisis, ex lacus suscipit felis, et aliquet ipsum est ac ligula. Mauris malesuada 
metus elit, a sagittis purus dapibus vitae. Phasellus accumsan, nisl sed condimentum condimentum, enim arcu gravida 
ex, in mattis elit justo ut erat. Mauris a dui lacinia, iaculis neque ut, vehicula purus. Sed vulputate, 
justo et finibus finibus, 2 elit neque convallis risus, a ultrices mi enim non massa. Maecenas tincidunt fringilla 
ullamcorper. Suspendisse potenti. Nunc mattis posuere turpis nec ultricies. Suspendisse lobortis pharetra magna, 
ac laoreet ligula pulvinar a. Ut aliquam dolor sed ex semper, a dictum metus lacinia. Vivamus mollis interdum dui, 
id convallis mi luctus id. Aliquam tristique sagittis lorem nec viverra.

Du2is quis tincidunt metus. Etiam aliquet leo augue, id scelerisque ipsum aliquet vitae. Vestibulum ut purus eget 
felis viverra interdum. RUN Mauris eget urna sem. Nulla auctor arcu ut nisi tincidunt, a commodo sem tristique. 
Suspendisse dignissim malesuada est, at tristique velit eleifend at. Aliquam ultrices nibh ac ultrices bibendum. 
Donec ultrices mauris at nisi faucibus, id aliquam velit tempor. Nullam id leo nulla. Sed pharetra interdum tortor id 
convallis. Vestibulum faucibus pharetra bibendum. Sed nec congue justo. Curabitur id ipsum volutpat, hendrerit erat 
a, condimentum ligula. Sed varius euismod magna, vel vulputate justo aliquet a. Morbi eget felis at est posuere 
rutrum. Nam tincidunt semper quam, sed pulvinar nulla fermentum a."""
# print(text)

# Задание 1: Найти все слова, начинающиеся с буквы "c".
pattern = r"\b[Cc]\w+\b"
print (re.findall(pattern, text))
# Задание 2: Найти все числа в тексте.
pattern1 = r"\b\d+\b"
print (re.findall(pattern1, text))
# Задание 3: Найти все слова, состоящие только из заглавных букв.
pattern2 = r"\b[A-Z][a-z]+\b"
print (re.findall(pattern2, text))
# Задание 4: Найти все предложения, содержащие слово "sed".
pattern3 = r"(\b[A-Z][^.?!]*\bsed\b[^.?!]*[.?!])"
print (re.findall(pattern3, text))

# Задание 5: Найти все слова, оканчивающиеся на букву "t".
pattern4 = r"\b\w+t\b"
print (re.findall(pattern4, text))

# Задание 6: Найти все предложения, в которых присутствуют числа.
pattern5 = r"[^.?!]*\b\w*\d+\w*\b[^.?!]*[.?!]"
print (re.findall(pattern5, text))

# Задание 7: Заменить все вхождения слова "malesuada" на слово "lorem".
pattern6 = r"\bmalesuada\b"
print (re.sub(pattern6, "lorem", text))
# Задание 8: Найти все предложения, в которых есть как минимум два слова, начинающихся с буквы "a".

# Задание 9: Найти все предложения, заканчивающиеся вопросительным знаком.

# Задание 10: Найти все слова, содержащие только буквы "a", "e", "i", "o", "u".

