# # Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# # возврат строки без изменений
# # возврат строки с преобразованием регистра без потери символов
# # возврат строки с удалением знаков пунктуации
# # возврат строки с удалением букв других алфавитов
# # возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

# import taskSem as test
# import pytest
# text1 = "abyr"
# text2 = "AbyR"
# text3 = "Ab:,UT"
# text4 = "заяцWolk"
# text5 = "заяцWolk 333jj OP,"


# def testStringOne(text :str):
#     """
#     >>> testStringOne("sajkbdd___+++aslhdajsd;lj JHGHGJG al wqkjqwheh jksahdkjk")
#     'sajkbddaslhdajsdlj jhghgjg al wkjwheh jksahdkjk'
#     >>> testStringOne("567fgh")
#     'fgh'
#     """
#     text = text.lower()
#     myStr = "abcdefghijklmnoprstuvwxyz ".lower()
#     textResult =""
#     for i in text:
#         if i in myStr:
#             textResult = textResult+i
#     return textResult

# def strTestNoChanges():
#     assert text1 == testStringOne(text1)

# def strTestRegistr():
#     #assert text2 == test.testStringOne(text2)
#     assert "abyr" == testStringOne(text2)

# def strTestPoints():
#     #assert text3 == test.testStringOne(text3)
#     assert "abut" == testStringOne(text3)
# def strTestSymbols():
#     #assert text4 == test.testStringOne(text4)
#     assert "wolk" == testStringOne(text4)

# def strTestAll():
#     #assert text5 == testStringOne(text5)
#     assert "wolk jj op" == testStringOne(text5)

# def digitTest():
#     assert (1, 2, 3) == (3, 2, 1)

# if __name__=="__main__":
#     pytest.main(['-v'])

# #про pytest нашел как запускать: файл содержащий тесты должен называться начиная с test и
# # функции-тесты в нем тоже должны начинаться с test ©Михаил


# 2/////
# import unittest
# class Rectangle():
#     def verifyRectangle(self, width, lenght):
#         if width <= 0 or lenght <= 0 :
#             print('сторона меньше или равна 0')
#             return False
#         else: return True

#     def __init__ (self, lenght: int, width: int):
#         if self.verifyRectangle(lenght, width):
#             self.lenght = lenght
#             self.width = width
#         else : print('объект не создан')


#     def __str__(self):
#         text = str(self.width) + " " + str(self.lenght)
#         return text

#     def __eq__(self, other):
#         if (self.width == other.width and self.lenght == other.lenght) or (self.width == other.lenght and self.lenght == other.width):
#             return True
#         else : return False

# class userClass(unittest.TestCase):
#     _rectangle = Rectangle(3, 6)

#     def testOne(self):
#         self.assertEqual(self._rectangle, self._rectangle)
#         #self.assertEqual(self._rectangle, Rectangle(4,5))     # Failed
#         self.assertEqual(self._rectangle, Rectangle(3, 6))
#         self.assertEqual(self._rectangle, Rectangle(6, 3))


# if __name__=="__main__":
#     r1 = Rectangle(3,5)
#     print(r1)
#     unittest.main()


# 3/////
# import doctest

# def testStringOne(text :str):
#     """
#     >>> testStringOne("sajkbdd___+++aslhdajsd;lj JHGHGJG al wqkjqwheh jksahdkjk")
#     'sajkbddaslhdajsdlj jhghgjg al wkjwheh jksahdkjk'
#     >>> testStringOne("567fgh")
#     'fgh'
#     """
#     text = text.lower()
#     myStr = "abcdefghijklmnoprstuvwxyz ".lower()
#     textResult =""
#     for i in text:
#         if i in myStr:
#             textResult = textResult+i
#     return textResult

# if __name__=="__main__":
#     doctest.testmod(verbose=True)
#     testStringOne("555lsjdjlaj")


# 4/////
# # Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# # возврат строки без изменений
# # возврат строки с преобразованием регистра без потери символов
# # возврат строки с удалением знаков пунктуации
# # возврат строки с удалением букв других алфавитов
# # возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

# import taskSem as test
# import unittest

# print(test.testStringOne("He44o"))

# class userClass(unittest.TestCase):
#     def testStr(self):
#         text = "abyrvalg"
#         self.assertEqual(text, test.testStringOne(text))

#     def testStrRegistr(self):
#         text = "DDff"
#         #self.assertEqual(text, test.testStringOne(text))
#         self.assertEqual(text.lower(),test.testStringOne(text))

#     def testStrDelPoints(self):
#         text = "ff,;:ss"
#         #self.assertEqual(text,test.testStringOne(text))
#         self.assertEqual("ffss", test.testStringOne(text))

#     def testStrSymbols(self):
#         text="абыр ппп"
#         #self.assertEqual(text,test.testStringOne(text))
#         self.assertEqual(" ", test.testStringOne(text))

#     def testAll(self):
#         text ="ЫЫ ss, Y"
#         #self.assertEqual(text, test.testStringOne(text))
#         self.assertEqual(" ss y", test.testStringOne(text))

# if __name__=="__main__":
#     unittest.main(verbosity=2)
