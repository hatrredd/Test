import logging as log

sum = 0

log.basicConfig(level=log.DEBUG, filename='test_logs.log', format='%(levelname)s (%(asctime)s): %(message)s', datefmt='%d/%m/%Y %I:%M:%S', encoding='utf-8')
log.info("Программа запущена!")

with open("test.txt", encoding="utf-8") as file:
    quantity = file.readline()
    log.info(f"Количество вопросов в тесте - {quantity}")
    for q in range(int(quantity)):
        question = file.readline()
        answers = file.readline()
        correct_answer = file.readline()
        print(question, end="")
        log.info(f"Вопрос №{q+1}:{question}")
        log.info("Варианты ответа: ")
        for i in range(1, int(answers)+1):
            answer = file.readline()
            print(f"{i}){answer}", end="")
            log.info(f"{i}){answer}")
        a = int(input("Ваш ответ: "))
        while a < 1 or a > int(answers):
            a = int(input("Вы ввели некорректный ответ, попробуйте ещё раз: "))
            log.error("Пользователь ввёл некорректный вариант ответа")
        log.info(f"Пользователь выбрал {a} вариант ответа")
        if a == int(correct_answer):
            print(f"Ответ {a} верный!\n")
            log.info(f"Ответ {a} верный!\n")
            sum += 1
        else:
            print(f"Ответ {a} неверный, верный ответ - {correct_answer}")
            log.info(f"Ответ {a} неверный, верный ответ - {correct_answer}")
            sum = sum
print(f"Вы ответили на {sum} из {int(quantity)} вопросов правильно ({round(sum/int(quantity)*100)}%)")
log.info(f"Пользователь ответил на {sum} из {int(quantity)} вопросов правильно ({round(sum/int(quantity)*100)}%)")
log.info("Программа завершена!\n")