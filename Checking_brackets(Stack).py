class Stack: # Класс эмитирующий работу структуры данных "Стек"
    def __init__(self): # При инициализации объекта создаются списки для хранения открывающихся скобок и их индексов
        self.stack_obj = []
        self.stack_ind = []
    def __push(self, unit, index): #Метод добавления элементов в стеки
        self.stack_obj.append(unit)
        self.stack_ind.append(index + 1)

    def __pop(self): #Удаление и возврат последнего элемента из стека. Если элементов нет, возвращает None
        if len(self.stack_obj) == 0:
            return None
        else:
            self.stack_ind.pop()
            return self.stack_obj.pop()

    def vie(self): #Просмотр стека
        print(self.stack_ind[::-1])
        print(self.stack_obj[::-1])

    def Output_remaining_opening_brackets(self): #Просмотр и вывод всех открывающих скобок,
                                                 #которым не нашлись закрывающие скобки
        for i in range(len(self.stack_ind)):
            print(f"element = {self.stack_obj.pop()}, index = {self.stack_ind.pop()}")

    def checking_brackets(self,line): #Метод принимает строку
        for index in range(len(line)):
            if line[index] in "[{(]})": #Отсеивание лишних символов кроме скобок
                if line[index] in "[{(": #Если скобка открывающаяся и не является последней скобкой в строке,
                                                            # то добавляем в стек.
                    if index != len(line) - 1:
                        self.__push(line[index], index)
                    else: #Иначе последовательность скобок неверна и выводим скобку и индекс
                        print(f"elemennt = {line[index]}, index = {index + 1}")
                        return
                elif line[index] in "]})": #Если скобка закрывающая
                    temp = self.__pop() # Из стека возвращается и удаляется последний эелемент
                    if ((temp == "[" and line[index] == "]") or (temp == "{" and line[index] == "}") or
                            (temp == "(" and line[index] == ")")): #Если открывающаяся скобка,взятая из стека, не равна
                                                            # закрывающей скобке, то последовательно скобок не верна.
                        continue
                    else:
                        print(f"elemennt = {line[index]}, index = {index + 1}")
                        return

        if len(self.stack_ind) != 0: #Если в стеке остались скобки, значит последовательность скобок не верна
            self.Output_remaining_opening_brackets() #Вызов метода для вывода оставшихся элементов в стеке
        else:
            print("Success")

s = "foo(bar[i);"
a = Stack()
a.checking_brackets(s)

