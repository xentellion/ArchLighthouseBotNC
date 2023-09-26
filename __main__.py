import discord
from discord.ext import commands
import random
import yaml
import re
import asyncio
from src.client import ArchLight


discord.utils.setup_logging()

data = None
quest = None
npc = None
candy = None
ad = None
users = None
client = None

@commands.command(name='лут')
async def random_trophy(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        trophy = f"{random.choice(data['trophy'])}"
        if trophy == 'оружие':
            response = f"```Трофей: оружие\nКласс: {random.choice(data['class_gen'])}\n"\
                        f"Вид: {random.choice(data['kind_weapon'])}\nПроизводство: {mfr().title()}```"
        elif trophy == 'основная броня':
            response = f"```Трофей: основная броня\nКласс: {random.choice(data['class_gen'])}\n" \
                        f"Вид: {random.choice(data['kind_main_armor'])}\nПроизводство: {mfr().title()}```"
        elif trophy == 'дополнительная броня':
            response = f"```Трофей: дополнительная броня\nКласс: {random.choice(data['class_gen'])}\n" \
                        f"Вид: {random.choice(data['kind_extra_armor'])}\nПроизводство: {mfr().title()}```"
        elif trophy == 'вспомогательное снаряжение':
            response = f"```Трофей: вспомогательное снаряжение\nПроизводство: {mfr().title()}```"
        elif trophy == 'расходник':
            response = f"```Трофей: расходник\nПроизводство: {mfr().title()}```"
        elif trophy == 'аксессуар':
            response = f"```Трофей: аксессуар\nВид аксессуара: {access()}\nПроизводство: {mfr().title()}```"
        elif trophy == 'устройство':
            response = f"```Трофей: устройство\nВид устройства: {random.choice(data['kind_device'])}\nЗащита: {random.choice(data['protection'])}\nПроизводство: {mfr().title()}```"
        elif trophy == 'повседневный предмет':
            response = f"```Трофей: повседневный предмет\nВид предмета: {item()}\nПроизводство: {mfr().title()}```"
        elif trophy == 'ценный предмет':
            response = f"```Трофей: ценный предмет\nВид предмета: {item()}\nПроизводство: {mfr().title()}```"
        elif trophy == 'деньги':
            response = f"```Трофей: деньги\nНоситель: {random.choice(data['carrier'])}\n" \
                        f"Производство: {mfr().title()}\nЗначение: {m_amount()}```"
        else:
            response = f"```Трофей: уникальное```"
        await ctx.send(response)

@commands.command(name='команды')
async def trophy_commands(ctx):
    response = f"```Достать случайный трофей: %лут\nУзконаправленные: %оружие %броня %допброня %снаряжение "\
                f"%расходник %аксессуар %устройство %простой %ценный %деньги\nДеньги: %значение\n"\
                f"Можно указывать количество трофеев после команды (до 5).\n\nСоздать разумного: %нпс (до 5 за раз)\n" \
                f"Создать миссию: %квест (до 5 за раз) или %квестосколка <номер осколка без пробелов> (до 5 за раз)\n" \
                f"Сгенерировать блок рекламы: %реклама (до 5 за раз)\n\n" \
                f"Сгенерировать осколок: %осколок <номер осколка>\n" \
                f"Угоститься конфеткой со случайным чипом: %киберконфетка (до 5 за раз)\n\n" \
                f"Рассылка для всех получателей из списка: %рассылка\n" \
                f"Сообщение конкретному пользователю: %сообщение имяпользователя\n" \
                f"Информационная панель: %панельимя без пробелов (до 5 запросов за раз)\n" \
                f"Новости со случайным осколком: %новости или %новостиосколка <номер осколка> (до 5 за раз)```"
    await ctx.message.delete()
    await ctx.send(response)

@commands.command(name='оружие')
async def random_weapon(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: оружие\nКласс: {random.choice(data['class_gen'])}\n"\
                    f"Вид: {random.choice(data['kind_weapon'])}\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='броня')
async def random_main_armor(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: основная броня\nКласс: {random.choice(data['class_gen'])}\n"\
                    f"Вид: {random.choice(data['kind_main_armor'])}\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='допброня')
async def random_extra_armor(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: дополнительная броня\nКласс: {random.choice(data['class_gen'])}\n"\
                    f"Вид: {random.choice(data['kind_extra_armor'])}\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='снаряжение')
async def random_auxiliary_equipment(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: вспомогательное снаряжение\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='расходник')
async def random_consumable(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: расходник\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='аксессуар')
async def random_accessory(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: аксессуар\nВид аксессуара: {access()}\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='устройство')
async def random_device(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: устройство\nВид устройства: {random.choice(data['kind_device'])}\nЗащита: {random.choice(data['protection'])}\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='простой')
async def random_simple_item(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: повседневный предмет\nВид предмета: {item()}\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='ценный')
async def random_valuable_item(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: ценный предмет\nВид предмета: {item()}\nПроизводство: {mfr().title()}```"
        await ctx.send(response)

@commands.command(name='деньги')
async def random_money(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Трофей: деньги\nНоситель: {random.choice(data['carrier'])}\n"\
                    f"Производство: {mfr().title()}\nЗначение: {m_amount()}```"
        await ctx.send(response)

@commands.command(name="значение")
async def money(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):
        response = f"```Значение: {amount()}```"
        await ctx.send(response)

#------- нпс

@commands.command(name='нпс')
async def random_npc(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):

        race_b = random.choice(npc['race'])
        if race_b == 'человек':
            race_b = f'человек'
        elif race_b == 'гарпия':
            race_b = f'гарпия ({random.choice(npc["garp"])})'
        elif race_b == 'сатир':
            race_b = f'сатир ({random.choice(npc["satir"])})'
        elif race_b == 'тифон':
            race_b = f'тифон ({random.choice(npc["tifon"])})'
        elif race_b == 'виверна':
            race_b = f'виверна ({random.choice(npc["vyvern"])})'
        elif race_b == 'тельхин':
            race_b = f'тельхин ({random.choice(npc["telhin"])})'

        age = [12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 54, 56, 58, 60, 64, 68, 70, 74, 78, 80, 84, 88,
                90, 95, 100, 105, 110, 120, 130, '140+']
        age = random.choice(age)

        value = random.randint(1, 5)
        if value == 1:
            health = f'идеальное здоровье'
        elif value == 2:
            health = f'{random.choice(npc["health_time"])}'
        elif value == 3:
            health = f'{random.choice(npc["health_pec"])}'
        elif value == 4:
            health = f'{random.choice(npc["health"])}'
        elif value == 5:
            health = f'{random.choice(npc["health_hard"])} с прогрессией {random.randint(1, 9) * 10}%'
        biol = f'{race_b}, {age}, {health}'

        val = random.randint(1, 4)
        phob = f'нет фобии'
        if val > 3:
            phob = f'{random.choice(npc["phobia"])}'

        val2 = random.randint(1, 4)
        cp = f'нет связей'
        if val2 > 2:
            cp = f'{random.choice(npc["interaction"])} {random.choice(data["corporation"])}'

        response = f"```Биология: {biol}\nПрофессия: {random.choice(npc['cbp_proff'])}, {random.choice(npc['proff'])}\n" \
                    f"Класс: {random.choice(npc['class'])}, {random.choice(npc['podclass'])}\n" \
                    f"Характер: {random.choice(npc['character'])}, {phob}\nСнаряжение:\n- оружие: {random.choice(data['class_gen'])}, "\
                    f"{random.choice(data['kind_weapon'])}\n- броня: {random.choice(data['class_gen'])}, "\
                    f"{random.choice(data['kind_main_armor'])}\n- с собой: {random.choice(data['trophy'])}\n" \
                    f"Особенность: {random.choice(npc['fea'])}\nСвязь с корпорацией: {cp}\n" \
                    f"Трофеев в карманах: {random.randint(1, 3)}```"

        await ctx.send(response)

# ------- квесты

@commands.command(name='квест')
async def random_quest(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):

        form = random.choice(quest['quest_form'])
        if form == 'устранение или охота':
            form = f'{random.choice(quest["hunt"])}'
        elif form == 'спасение':
            form = f'{random.choice(quest["save"])} {random.choice(quest["save_from"])}'
        elif form == 'кража или захват':
            form = f'{random.choice(quest["grab"])}'
        elif form == 'саботаж или шпионаж':
            form = f'{random.choice(quest["sabotage"])}'
        elif form == 'охрана или защита':
            form = f'{random.choice(quest["protect"])} от {random.choice(quest["from"])}'
        elif form == 'расследование или исследование':
            form = f'{random.choice(quest["study"])}'
        elif form == 'уникальное':
            form = f'уникальное'

        dif = random.choice(quest['difficulty'])
        if dif == 'легкая':
            dif = f'легкая, награда: {random.randint(5, 10)}к'
        elif dif == 'средняя':
            dif = f'средняя, награда: {random.randint(10, 20)}к'
        elif dif == 'тяжелая':
            dif = f'тяжелая, награда: {random.randint(20, 30)}к'

        numnum = random.randint(1, 10)
        time_list = ["в течение", "крайний срок через"]
        time_fr = ["с момента взятия задания", "с текущего дня"]
        type_time = ["день", "час"]
        time = f"{random.choice(time_list)} {numnum} ({random.choice(type_time)}) {random.choice(time_fr)}"

        place_num = random.randint(1, 300)
        if place_num > 210:
            place = f"{random.choice(quest['place_dark'])}"
        else:
            place = f"осколок {random.choice(quest['place'])}"

        response = f"```Миссия #{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1, 99)}\n\n" \
                    f"Вид: {form}\nМесто: {place}\nСложность: {dif}\n" \
                    f"Время: {time}\nОсобенность: {random.choice(quest['peculiarity'])}, {random.choice(quest['peculiarity'])}```"

        await ctx.send(response)

@commands.command(name='квестосколка')
async def random_quest_isl(ctx, m='0', n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()
    for i in range(n):

        form = random.choice(quest['quest_form'])
        if form == 'устранение или охота':
            form = f'{random.choice(quest["hunt"])}'
        elif form == 'спасение':
            form = f'{random.choice(quest["save"])} {random.choice(quest["save_from"])}'
        elif form == 'кража или захват':
            form = f'{random.choice(quest["grab"])}'
        elif form == 'саботаж или шпионаж':
            form = f'{random.choice(quest["sabotage"])}'
        elif form == 'охрана или защита':
            form = f'{random.choice(quest["protect"])} от {random.choice(quest["from"])}'
        elif form == 'расследование или исследование':
            form = f'{random.choice(quest["study"])}'
        elif form == 'уникальное':
            form = f'уникальное'

        dif = random.choice(quest['difficulty'])
        if dif == 'легкая':
            dif = f'легкая, награда: {random.randint(5, 10)}к'
        elif dif == 'средняя':
            dif = f'средняя, награда: {random.randint(10, 20)}к'
        elif dif == 'тяжелая':
            dif = f'тяжелая, награда: {random.randint(20, 30)}к'

        numnum = random.randint(1, 10)
        time_list = ["в течение", "крайний срок через"]
        time_fr = ["с момента взятия задания", "с текущего дня"]
        type_time = ["день", "час"]
        time = f"{random.choice(time_list)} {numnum} ({random.choice(type_time)}) {random.choice(time_fr)}"

        place_num = random.randint(1, 300)
        if place_num > 210:
            place = f"{random.choice(quest['place_dark'])}"
        else:
            place = f"осколок {random.choice(quest['place'])}"

        response = f"```Миссия #{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1, 99)}\n\n" \
                    f"Вид: {form}\nМесто: {m}\nСложность: {dif}\n" \
                    f"Время: {time}\nОсобенность: {random.choice(quest['peculiarity'])}, {random.choice(quest['peculiarity'])}```"

        await ctx.send(response)
# ------- конфеты

@commands.command(name='киберконфетка')
async def random_candy(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()

    for i in range(n):
        candy_type = random.choice(candy['candy_type'])
        response = f"```#ОШИБКА ЧТЕНИЯ ЧИПА```"
        if candy_type == 'скидка корпорации':
            response = f"""```ml\n{random.choice(candy['disk']).capitalize()} {random.choice(candy['action'])} """ \
                        f"""в корпорации {random.choice(data['corporation']).title()} """ \
                        f"""(только в официальных магазинах) по коду """ \
                        f"""{random.randint(10, 9999)}-{random.randint(10, 9999)} (активация кода разовая, код действителен с момента """ \
                        f"""его считывания в течение {random.randint(5, 20)}-ти {random.choice(['дней', 'часов'])})```"""

        elif candy_type == 'скидка':
            response = f"""```ml\n{random.choice(candy['disk']).capitalize()} {random.choice(candy['action'])} у привратника по коду """ \
                        f"""{random.randint(10, 9999)}-{random.randint(10, 9999)} (активация кода разовая, код действителен с момента """ \
                        f"""его считывания в течение {random.randint(5, 20)}-ти {random.choice(['дней', 'часов'])})```"""

        elif candy_type == 'пожелание':
            response = f"""```ml\n{random.choice(candy['time']).capitalize()} {random.choice(candy['whom'])} соблаговолит """ \
                        f"""{random.choice(candy['luck'])} {random.choice(candy['in_what'])}```"""

        await ctx.send(response)

# ------- реклама

@commands.command(name='реклама')
async def random_ad(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("В запрос принимаются значения от 1 до 5")
        return
    await ctx.message.delete()

    for i in range(n):
        #response = f"```#ОШИБКА ЧТЕНИЯ ЧИПА```"

        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)
        ft_time = random.choice(['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

        adress = random.randint(1000000000, 9999999999)

        ad_type_per = random.randint(1, 10)

        if ad_type_per > 5:
            ad_type_corp_list = ['акция корпорации', 'мероприятие корпорации', 'реклама корпорации', 'трудоустройство корпорации']
            ad_type_corp = random.choice(ad_type_corp_list)

            if ad_type_corp == 'акция корпорации':
                corp_corp_disc = random.choice(data['corporation'])
                if corp_corp_disc == '':
                    response = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    response = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\nТОЛЬКО СЕГОДНЯ! {random.choice(candy['disk'])} {random.choice(candy['action'])} """ \
                                    f"""в корпорации ▶ {(corp_corp_disc).upper()} ◀ (акция действует только в официальных магазинах) """ \
                                    f"""Узнать полную информацию о действии акции: """ \
                                    f"""{adress}```"""

            elif ad_type_corp == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == '':
                    response = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    response = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""▶ {(corp_corp_fest).upper()} ◀. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif ad_type_corp == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == '':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n\nМы создали этот город, и мы можем дать тем, кто помогает нам строить и защищать его:\n""" \
                                    f"""✔ Приоритет обслуживания Орденам Пантеона Нокс\n""" \
                                    f"""✔ Повышенные лимиты всех подписок и доступ к особым подпискам закрытым для публики\n""" \
                                    f"""✔ Работу в самой престижной и уважаемой корпорации, что творит историю\n""" \
                                    f"""✔ Шедрые премии, зарплата, страховка, гарантии - чтобы вам никогда не пришлось боятся за свое или своих близких будушее\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["nox_vac"])}\n- {random.choice(data["nox_vac"])}\n- {random.choice(data["nox_vac"])}\n\n""" \
                                    f"""Станьте частью тех, на чьих плечах стоит этот город!\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n\nС нами вы:\n""" \
                                    f"""✔ Работаете на уважаемой, статусной и солидной работе\n""" \
                                    f"""✔ Получаете приоритет в пользовании услугами корпорации\n""" \
                                    f"""✔ Имеете шанс проявить свои дизайнерские таланты\n""" \
                                    f"""✔ Работаете с премиальными технологиями в комфортной и удобной среде\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["hh_vac"])}\n- {random.choice(data["hh_vac"])}\n- {random.choice(data["hh_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n\nС нами вы:\n""" \
                                    f"""✔ Получаете приоритет медицинского обслуживания в предприятиях корпорации\n""" \
                                    f"""✔ Получаете медицинскую страховку пропорционально вашему статусу в корпорации\n""" \
                                    f"""✔ Работаете на уважаемой работе в корпорации которая спасает жизни\n""" \
                                    f"""✔ Работаете на самой безопасной работе, в корпорации где наименьший процент рабочих травм\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["aet_vac"])}\n- {random.choice(data["aet_vac"])}\n- {random.choice(data["aet_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n\nС нами вы:\n""" \
                                    f"""✔ Будете знать, что то, что вы создаете - простоит века\n""" \
                                    f"""✔ Будете уверенны в завтра с надежными контрактами и графиками выплат\n""" \
                                    f"""✔ Будете застрахованы на случай производственных травм\n""" \
                                    f"""✔ Получите шанс работать даже имея минимальное образование\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["oir_vac"])}\n- {random.choice(data["oir_vac"])}\n- {random.choice(data["oir_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n\nПредлагает:\n""" \
                                    f"""✔ Работу с отключенным разумом, не работайте ни дня в своей жизни\n""" \
                                    f"""✔ Возможность заработать на продаже своих знаний, заработок без единого движения\n""" \
                                    f"""✔ Мудрое управление и подобранный под вас коллектив, ведь мы читаем ваши мысли\n""" \
                                    f"""✔ Доступ к базам данных для загрузки навыков для повышения квалификации\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["tenta_vac"])}\n- {random.choice(data["tenta_vac"])}\n- {random.choice(data["tenta_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n\nПредлагает:\n""" \
                                    f"""✔ Работу с передовыми технологиями Магнавеб, за которыми - будущее\n""" \
                                    f"""✔ Опции удаленной работы из дома через Магнавеб\n""" \
                                    f"""✔ Бонусы и повышенные лимиты пользования Магнавеб для работников\n""" \
                                    f"""✔ Неограниченный доступ к Когна, Ковен и Стрим для работников\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["magna_vac"])}\n- {random.choice(data["magna_vac"])}\n- {random.choice(data["magna_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n\nМы гарантируем вам:\n""" \
                                    f"""✔ Заботу, дружный коллектив, мудрое покровительство без необходимости волноваться о будущем\n""" \
                                    f"""✔ Предоставление еды, воды и всего критически необходимого - корпорацией\n""" \
                                    f"""✔ Трудоустройство с обучением, адаптацией тела и имплантацией за счет корпорации\n""" \
                                    f"""✔ Эмпатическое стимулирование что сделает ваши дни светлее, а работу - желаннее\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["vis_vac"])}\n- {random.choice(data["vis_vac"])}\n- {random.choice(data["vis_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n\nМы гарантируем вам:\n""" \
                                    f"""✔ Обеспечение трудоустройства любому кто пожелает стать частью Улья\n""" \
                                    f"""✔ Мудрое управление, опыт ассимиляции всех рас длинной в тысячелетия\n""" \
                                    f"""✔ Безопасность и порядок на работе и в вашем Улье\n""" \
                                    f"""✔ Обеспечение собственного жилья любому кто пожелает стать частью Улья\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["prima_vac"])}\n- {random.choice(data["prima_vac"])}\n- {random.choice(data["prima_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n\nМы гарантируем вам:\n""" \
                                    f"""✔ Банковский счет и виртуальный кошелек с выгодными условиями для каждого работника\n""" \
                                    f"""✔ Комфортную рабочую среду\n""" \
                                    f"""✔ Возможность получения премий круизами на наших лучших лайнерах\n""" \
                                    f"""✔ Приоритет в обслуживании для работников коорпорации\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["ail_vac"])}\n- {random.choice(data["ail_vac"])}\n- {random.choice(data["ail_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n\nМы предлагаем вам:\n""" \
                                    f"""✔ Шанс работы в мультикультурном и всерассовом коллективе без дискриминации\n""" \
                                    f"""✔ Шанс работы с самыми передовыми технологиями что соединяют усилия всех рас\n""" \
                                    f"""✔ Шанс трудоустройства и получения жилья в наших Замках и Поместьях\n""" \
                                    f"""✔ Шанс прохождения обучения непревзойденного качества и последущего становления ангелом или даже аватаром архонта\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["kain_vac"])}\n- {random.choice(data["kain_vac"])}\n- {random.choice(data["kain_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n\nМы предлагаем вам:\n""" \
                                    f"""✔ Прозрение, стабильность, надежду, социальную и психологическую помощь от тех, кто знает вашу душу лучше вас\n""" \
                                    f"""✔ Правильно подобранное трудоустройство и коллектив, ведь мы знаем чего вы желаете\n""" \
                                    f"""✔ Всестороннюю помощь в устройстве жизни для всех работников корпорации\n""" \
                                    f"""✔ Возможность помогать другим и вести их к надежде и свету\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["rev_vac"])}\n- {random.choice(data["rev_vac"])}\n- {random.choice(data["rev_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Син Корп':
                        chanse_sin = random.randint(1, 3)
                        if chanse_sin == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nПредлагает:\n""" \
                                        f"""✔ Работу от которой вы будете получать удовольствие\n""" \
                                        f"""✔ Бонусы в заведениях корпорации для сотрудников\n""" \
                                        f"""✔ Интересные и креативные проекты\n""" \
                                        f"""✔ Возможность творческой самореализаци\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif chanse_sin == 2:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nГарантирует:\n""" \
                                        f"""✔ Адаптивный график работы\n""" \
                                        f"""✔ Регулярные корпоративы и мероприятия для работников\n""" \
                                        f"""✔ Дружный коллектив\n""" \
                                        f"""✔ Работу без излишней бюрократии\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif chanse_sin == 3:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nС нами вы:\n""" \
                                        f"""✔ Никогда не заскучаете\n""" \
                                        f"""✔ Найдете коллектив со схожими интересами\n""" \
                                        f"""✔ Будете говорить "жеще папочка" сердитому начальнику\n""" \
                                        f"""✔ Будете работать в корпорации которая честно смотрит на себя и на вас\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n\nПредлагает:\n""" \
                                    f"""✔ Трудоустройство без образования\n""" \
                                    f"""✔ Имплантацию и подготовку за счет корпорации\n""" \
                                    f"""✔ Стабильные и долгие контракты\n""" \
                                    f"""✔ Страховку с выплатами семье и близким в случае смерти\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["mord_vac"])}\n- {random.choice(data["mord_vac"])}\n- {random.choice(data["mord_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n\nПредлагает:\n""" \
                                    f"""✔ Работу поблизости от дома\n""" \
                                    f"""✔ Бонусы в магазинах корпорации для сотрудников\n""" \
                                    f"""✔ Премии продукцией компании которую вы выберете\n""" \
                                    f"""✔ Трудоустройство с минимальным образованием\n\n""" \
                                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["ae_vac"])}\n- {random.choice(data["ae_vac"])}\n- {random.choice(data["ae_vac"])}\n\n""" \
                                    f"""Запишитесь сегодня!\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                response = corp_emp

            elif ad_type_corp == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == '':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                response = corp_emp

        else:
            ad_type = random.choice(ad['ad_type'])
            if ad_type == 'хорниспам':
                response = f"""```ml\n{random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif ad_type == 'разное':
                response = f"""```ml\n{random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""

            elif ad_type == 'покупка':
                if halfer == 1:
                    response = f"""```ml\n{random.choice(ad['how']).capitalize()} {random.choice(ad['pers_action_purch'])} """ \
                                    f"""{random.choice(ad['what_is_ad'])}: {number_id()}```"""
                elif halfer == 2:
                    response = f"""```ml\nСкупка {random.choice(ad['not_obj'])}: {number_id()}```"""

            elif ad_type == 'продажа':
                if halfer == 1:
                    response = f"""```ml\n{random.choice(ad['how']).capitalize()} {random.choice(ad['pers_action_sale'])} """ \
                                    f"""{random.choice(ad['what_is_ad'])}, {price}: {number_id()}```"""
                elif halfer == 2:
                    response = f"""```ml\nПродажа {random.choice(ad['not_obj'])}: {number_id()}```"""

            elif ad_type == 'услуга':
                response = f"""```ml\n{random.choice(ad['service']).capitalize()}: {number_id()}```"""

            elif ad_type == 'трудоустройство':
                service_type = random.choice(['корп', 'проч'])
                if service_type == 'корп':
                    response = f"""```ml\nПомогу с трудоустройством {random.choice(ad['emp_corp_type'])} в корпорацию {random.choice(data['corporation']).title()}: {number_id()}```"""
                elif service_type == 'проч':
                    response = f"""```ml\n{random.choice(ad['employ']).capitalize()}: {number_id()}```"""

            elif ad_type == 'мероприятие':
                response = f"""```ml\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} {random.choice(ad['fest_action'])} """ \
                                f"""{random.choice(ad['fest_type'])}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                f"""Узнать больше информации: {number_id()}```"""

            else:
                response = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        await ctx.send(response)

# ------- почта

@commands.command(name='рассылка')
async def mailing(ctx, *, args):
    users_id = (users['user_id'])
    await ctx.message.delete()
    for channel_id in users_id:
        channel = client.get_channel(channel_id)
        message = f"""```ml\n'ALL' {(args)}```"""
        await channel.send(message)
    mess_us = f"_** **\nСтатус: отправлено_{message}"
    await ctx.send(mess_us)

@commands.command(name='сообщение')
async def pm_send(ctx, user='0', *, args):

    if ctx.author.name in (users['dis_users']):
        if ctx.author.name == '_flamer':
            sender = '164719-399449-473728'
        elif ctx.author.name == 'wingylalka7302':
            sender = '578500-104764-819584'
        elif ctx.author.name == 'venzelsuka':
            sender = '799935-168876-772625'
        elif ctx.author.name == 'mossycorpse':
            sender = '038493-628490-174028'
        elif ctx.author.name == 'justrostok':
            sender = '637326-743969-354438'
        elif ctx.author.name == 'venzelsuka':
            sender = '799935-168876-772625'
        else:
            sender = 'ERROR'
        message = f"""```ml\n'РМ' {(args)} {sender}```"""
    else:
        message = f"""```ml\n'РМ' {(args)}```"""

    await ctx.message.delete()

    pattern = re.compile("\d{6}-\d{6}-\d{6}")

    if user in ("000000-000000-000000", "Маги", "Штиль", "590182-630012-995152"):
        channel = client.get_channel(1139663185696280656)
    elif user in ("дарк", "дарки"):
        channel = client.get_channel(1135590381430522007)

    elif user in ("852457-825573-420543", 'МамаНэрр'):
        channel = client.get_channel(1140030495971872789)
    elif user in ("228267-193891-112289", "Кварта"):
        channel = client.get_channel(1140030495971872789)

    elif user == '637326-743969-354438':
        channel = client.get_channel(1139534804631699616)
    elif user == '578500-104764-819584':
        channel = client.get_channel(1139849919809720431)
    elif user == '164719-399449-473728':
        channel = client.get_channel(1139534722402369536)
    elif user == '799935-168876-772625':
        channel = client.get_channel(1143512126711922719)
    elif user == '038493-628490-174028':
        channel = client.get_channel(1143992714292121741)
    else:
        if pattern.match(user):
            channel = client.get_channel(1143987182877540573)
            mess_us = f"_** **\nПолучатель: {user} (неизвестный номер)\nСтатус: отправлено_{message}"
            await ctx.send(mess_us)
            await channel.send(message)
        else:
            mess_us = f"_** **\nПолучатель: не определен (ошибка номера)\nСтатус: ОШИБКА_{message}"
            await ctx.send(mess_us)
        return

    mess_us = f"_** **\nПолучатель: {user}\nСтатус: отправлено_{message}"
    await ctx.send(mess_us)
    await channel.send(message)

# ------- инфо панели
@commands.command(name='общаяпанель')
async def panel_all(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("_Запрос не может превышать 5 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)

        spam_type = random.choice(users['spam_type'])
        adress = random.randint(1000000000, 9999999999)

        if halfer == 1:
            spam_adress_rnd = adress
        elif halfer == 2:
            spam_adress_rnd = number_id()

        if panel_mess_rnd <= 100:
            spam_type = random.choice(['хорниспам', 'разное'])
            if spam_type == 'хорниспам':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif spam_type == 'разное':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
            panel_ad_type_list = ['акция корпорации', 'мероприятие корпорации', 'реклама корпорации',
                                    'трудоустройство корпорации', 'покупка', 'продажа', 'услуга', 'трудоустройство',
                                    'мероприятие']
            panel_ad_type = random.choice(panel_ad_type_list)
            ft_time = random.choice(['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            if panel_ad_type == 'акция корпорации':
                corp_corp = random.choice(data['corporation'])
                if corp_corp == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\nТОЛЬКО СЕГОДНЯ! {random.choice(candy['disk'])} {random.choice(candy['action'])} """ \
                                    f"""в корпорации {(corp_corp).upper()} (акция действует только в официальных магазинах) """ \
                                    f"""Узнать полную информацию о действии акции: """ \
                                    f"""{adress}```"""

            elif panel_ad_type == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""{(corp_corp_fest).upper()}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif panel_ad_type == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"{ad_corp_empl_nox()}"
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"{ad_corp_empl_hh()}"
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"{ad_corp_empl_aet()}"
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"{ad_corp_empl_oir()}"
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"{ad_corp_empl_tenta()}"
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"{ad_corp_empl_magna()}"
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"{ad_corp_empl_vis()}"
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"{ad_corp_empl_prima()}"
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"{ad_corp_empl_ail()}"
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"{ad_corp_empl_kain()}"
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"{ad_corp_empl_rev()}"
                    elif corp_emp == 'Син Корп':
                        corp_emp = f"{ad_corp_empl_sin()}"
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"{ad_corp_empl_morde()}"
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"{ad_corp_empl_all()}"
                panel_message = corp_emp

            elif panel_ad_type == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        corp_emp = random.choice(data["corporation"])
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                panel_message = corp_emp

            elif panel_ad_type == 'покупка':
                if halfer == 1:
                    panel_message = f"""```ml\nAD {random.choice(ad['how']).capitalize()} {random.choice(ad['pers_action_purch'])} """ \
                                    f"""{random.choice(ad['what_is_ad'])}: {number_id()}```"""
                elif halfer == 2:
                    panel_message = f"""```ml\nAD Скупка {random.choice(ad['not_obj'])}: {number_id()}```"""

            elif panel_ad_type == 'продажа':
                if halfer == 1:
                    panel_message = f"""```ml\nAD {random.choice(ad['how']).capitalize()} {random.choice(ad['pers_action_sale'])} """ \
                                    f"""{random.choice(ad['what_is_ad'])}, {price}: {number_id()}```"""
                elif halfer == 2:
                    panel_message = f"""```ml\nAD Продажа {random.choice(ad['not_obj'])}: {number_id()}```"""

            elif panel_ad_type == 'услуга':
                panel_message = f"""```ml\nAD {random.choice(ad['service']).capitalize()}: {number_id()}```"""

            elif panel_ad_type == 'трудоустройство':
                service_type = random.choice(['корп', 'проч'])
                if service_type == 'корп':
                    panel_message = f"""```ml\nAD Помогу с трудоустройством {random.choice(ad['emp_corp_type'])} в корпорацию {random.choice(data['corporation']).title()}: {number_id()}```"""
                elif service_type == 'проч':
                    panel_message = f"""```ml\nAD {random.choice(ad['employ']).capitalize()}: {number_id()}```"""

            elif panel_ad_type == 'мероприятие':
                panel_message = f"""```ml\nAD {ft_time.capitalize()} на осколке {random.choice(quest['place'])} {random.choice(ad['fest_action'])} """ \
                                f"""{random.choice(ad['fest_type'])}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                f"""Узнать больше информации: {number_id()}```"""

            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif panel_mess_rnd >= 205:
            spam_def = random.randint(1, 100)
            if spam_def < 100:
                if spam_type == 'имплант':
                    panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(users['implant'])}. """ \
                                    f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                elif spam_type == 'посылка':
                    panel_message = f"""```ml\n'РМ' {random.choice(users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                    f"""{random.choice(users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\n'РМ' {random.choice(users['other']).capitalize()}: {spam_adress_rnd}```"""
            else:
                panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

        else:
            panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

        await ctx.send(panel_message)


@commands.command(name='лид')
async def panel_1(ctx, n=1):
    if (n < 1) or (n > 10):
        await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)

        spam_type = random.choice(users['spam_type'])
        adress = random.randint(1000000000, 9999999999)

        if halfer == 1:
            spam_adress_rnd = adress
        elif halfer == 2:
            spam_adress_rnd = number_id()

        if panel_mess_rnd <= 100:
            spam_type = random.choice(['хорниспам', 'разное'])
            if spam_type == 'хорниспам':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif spam_type == 'разное':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
            panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                    'трудоустройство корпорации']
            panel_ad_type = random.choice(panel_ad_type_list)
            ft_time = random.choice(
                ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            if panel_ad_type == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == 'Д':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""{(corp_corp_fest).upper()}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif panel_ad_type == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"{ad_corp_empl_nox()}"
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"{ad_corp_empl_hh()}"
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"{ad_corp_empl_aet()}"
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"{ad_corp_empl_oir()}"
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"{ad_corp_empl_tenta()}"
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"{ad_corp_empl_magna()}"
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"{ad_corp_empl_vis()}"
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"{ad_corp_empl_prima()}"
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"{ad_corp_empl_ail()}"
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"{ad_corp_empl_kain()}"
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"{ad_corp_empl_rev()}"
                    elif corp_emp == 'Син Корп':
                        corp_emp = f"{ad_corp_empl_sin()}"
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"{ad_corp_empl_morde()}"
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"{ad_corp_empl_all()}"
                panel_message = corp_emp

            elif panel_ad_type == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        corp_emp = random.choice(data["corporation"])
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                panel_message = corp_emp
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif panel_mess_rnd >= 205:
            spam_def = random.randint(1, 100)
            if spam_def < 100:
                if spam_type == 'имплант':
                    panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(users['implant'])}. """ \
                                    f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                elif spam_type == 'посылка':
                    panel_message = f"""```ml\n'РМ' {random.choice(users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                    f"""{random.choice(users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\n'РМ' {random.choice(users['other']).capitalize()}: {spam_adress_rnd}```"""
            else:
                panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

        else:
            panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

        await ctx.send(panel_message)

#ЭТО ПАНЕЛЬ АСИ

@commands.command(name='панельАрхимед')
async def panel_2(ctx, n=1):
    if (n < 1) or (n > 10):
        await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)

        spam_type = random.choice(users['spam_type'])
        adress = random.randint(1000000000, 9999999999)

        if halfer == 1:
            spam_adress_rnd = adress
        elif halfer == 2:
            spam_adress_rnd = number_id()

        if panel_mess_rnd <= 100:
            spam_type = random.choice(['хорниспам', 'разное'])
            if spam_type == 'хорниспам':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif spam_type == 'разное':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
            panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                    'трудоустройство корпорации']
            panel_ad_type = random.choice(panel_ad_type_list)
            ft_time = random.choice(
                ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            if panel_ad_type == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == 'Д':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""{(corp_corp_fest).upper()}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif panel_ad_type == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"{ad_corp_empl_nox()}"
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"{ad_corp_empl_hh()}"
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"{ad_corp_empl_aet()}"
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"{ad_corp_empl_oir()}"
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"{ad_corp_empl_tenta()}"
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"{ad_corp_empl_magna()}"
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"{ad_corp_empl_vis()}"
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"{ad_corp_empl_prima()}"
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"{ad_corp_empl_ail()}"
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"{ad_corp_empl_kain()}"
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"{ad_corp_empl_rev()}"
                    elif corp_emp == 'Син Корп':
                        corp_emp = f"{ad_corp_empl_sin()}"
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"{ad_corp_empl_morde()}"
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"{ad_corp_empl_all()}"
                panel_message = corp_emp

            elif panel_ad_type == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        corp_emp = random.choice(data["corporation"])
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                panel_message = corp_emp
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif panel_mess_rnd >= 205:
            spam_def = random.randint(1, 100)
            if spam_def < 100:
                if spam_type == 'имплант':
                    panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(users['implant'])}. """ \
                                    f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                elif spam_type == 'посылка':
                    panel_message = f"""```ml\n'РМ' {random.choice(users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                    f"""{random.choice(users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\n'РМ' {random.choice(users['other']).capitalize()}: {spam_adress_rnd}```"""
            else:
                panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

        else:
            panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

        await ctx.send(panel_message)

# ЭТО ПАНЕЛЬ РОСТИКА

@commands.command(name='панель637326-743969-354438')
async def panel_3(ctx, n=1):
    if (n < 1) or (n > 10):
        await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)

        spam_type = random.choice(users['spam_type'])
        adress = random.randint(1000000000, 9999999999)

        if halfer == 1:
            spam_adress_rnd = adress
        elif halfer == 2:
            spam_adress_rnd = number_id()

        if panel_mess_rnd <= 100:
            spam_type = random.choice(['хорниспам', 'разное'])
            if spam_type == 'хорниспам':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif spam_type == 'разное':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
            panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                    'трудоустройство корпорации']
            panel_ad_type = random.choice(panel_ad_type_list)
            ft_time = random.choice(
                ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            if panel_ad_type == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == 'Д':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""{(corp_corp_fest).upper()}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif panel_ad_type == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"{ad_corp_empl_nox()}"
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"{ad_corp_empl_hh()}"
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"{ad_corp_empl_aet()}"
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"{ad_corp_empl_oir()}"
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"{ad_corp_empl_tenta()}"
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"{ad_corp_empl_magna()}"
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"{ad_corp_empl_vis()}"
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"{ad_corp_empl_prima()}"
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"{ad_corp_empl_ail()}"
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"{ad_corp_empl_kain()}"
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"{ad_corp_empl_rev()}"
                    elif corp_emp == 'Син Корп':
                        corp_emp = f"{ad_corp_empl_sin()}"
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"{ad_corp_empl_morde()}"
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"{ad_corp_empl_all()}"
                panel_message = corp_emp

            elif panel_ad_type == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        corp_emp = random.choice(data["corporation"])
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                panel_message = corp_emp
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif panel_mess_rnd >= 205:
            spam_def = random.randint(1, 100)
            if spam_def < 100:
                if spam_type == 'имплант':
                    panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(users['implant'])}. """ \
                                    f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                elif spam_type == 'посылка':
                    panel_message = f"""```ml\n'РМ' {random.choice(users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                    f"""{random.choice(users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\n'РМ' {random.choice(users['other']).capitalize()}: {spam_adress_rnd}```"""
            else:
                panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

        else:
            panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

        await ctx.send(panel_message)

# ЭТО ПАНЕЛЬ ФЛАМБО

@commands.command(name='панельЗабвение')
async def panel_4(ctx, n=1):
    if (n < 1) or (n > 10):
        await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)

        spam_type = random.choice(users['spam_type'])
        adress = random.randint(1000000000, 9999999999)

        if halfer == 1:
            spam_adress_rnd = adress
        elif halfer == 2:
            spam_adress_rnd = number_id()

        if panel_mess_rnd <= 100:
            spam_type = random.choice(['хорниспам', 'разное'])
            if spam_type == 'хорниспам':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif spam_type == 'разное':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
            panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации', 'покупка', 'продажа', 'услуга',
                                    'трудоустройство корпорации']
            panel_ad_type = random.choice(panel_ad_type_list)
            ft_time = random.choice(
                ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            if panel_ad_type == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == 'Д':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""{(corp_corp_fest).upper()}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif panel_ad_type == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"{ad_corp_empl_nox()}"
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"{ad_corp_empl_hh()}"
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"{ad_corp_empl_aet()}"
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"{ad_corp_empl_oir()}"
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"{ad_corp_empl_tenta()}"
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"{ad_corp_empl_magna()}"
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"{ad_corp_empl_vis()}"
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"{ad_corp_empl_prima()}"
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"{ad_corp_empl_ail()}"
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"{ad_corp_empl_kain()}"
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"{ad_corp_empl_rev()}"
                    elif corp_emp == 'Син Корп':
                        corp_emp = f"{ad_corp_empl_sin()}"
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"{ad_corp_empl_morde()}"
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"{ad_corp_empl_all()}"
                panel_message = corp_emp

            elif panel_ad_type == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        corp_emp = random.choice(data["corporation"])
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                panel_message = corp_emp

            elif panel_ad_type == 'покупка':
                if halfer == 1:
                    panel_message = f"""```ml\nAD {random.choice(ad['how']).capitalize()} {random.choice(ad['pers_action_purch'])} """ \
                                    f"""{random.choice(ad['what_is_ad'])}: {number_id()}```"""
                elif halfer == 2:
                    panel_message = f"""```ml\nAD Скупка {random.choice(ad['not_obj'])}: {number_id()}```"""

            elif panel_ad_type == 'продажа':
                if halfer == 1:
                    panel_message = f"""```ml\nAD {random.choice(ad['how']).capitalize()} {random.choice(ad['pers_action_sale'])} """ \
                                    f"""{random.choice(ad['what_is_ad'])}, {price}: {number_id()}```"""
                elif halfer == 2:
                    panel_message = f"""```ml\nAD Продажа {random.choice(ad['not_obj'])}: {number_id()}```"""

            elif panel_ad_type == 'услуга':
                panel_message = f"""```ml\nAD {random.choice(ad['service']).capitalize()}: {number_id()}```"""

            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""



        elif panel_mess_rnd >= 205:
            spam_def = random.randint(1, 100)
            if spam_def < 100:
                if spam_type == 'имплант':
                    panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(users['implant'])}. """ \
                                    f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                elif spam_type == 'посылка':
                    panel_message = f"""```ml\n'РМ' {random.choice(users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                    f"""{random.choice(users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\n'РМ' {random.choice(users['other']).capitalize()}: {spam_adress_rnd}```"""
            else:
                panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

        else:
            panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

        await ctx.send(panel_message)

# ЭТО ПАНЕЛЬ ЧЕРЕПА

@commands.command(name='панельKayzen')
async def panel_5(ctx, n=1):
    if (n < 1) or (n > 10):
        await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)

        spam_type = random.choice(users['spam_type'])
        adress = random.randint(1000000000, 9999999999)

        if halfer == 1:
            spam_adress_rnd = adress
        elif halfer == 2:
            spam_adress_rnd = number_id()

        if panel_mess_rnd <= 100:
            spam_type = random.choice(['хорниспам', 'разное'])
            if spam_type == 'хорниспам':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif spam_type == 'разное':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
            panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                    'трудоустройство корпорации']
            panel_ad_type = random.choice(panel_ad_type_list)
            ft_time = random.choice(
                ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            if panel_ad_type == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == 'Д':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""{(corp_corp_fest).upper()}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif panel_ad_type == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"{ad_corp_empl_nox()}"
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"{ad_corp_empl_hh()}"
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"{ad_corp_empl_aet()}"
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"{ad_corp_empl_oir()}"
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"{ad_corp_empl_tenta()}"
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"{ad_corp_empl_magna()}"
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"{ad_corp_empl_vis()}"
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"{ad_corp_empl_prima()}"
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"{ad_corp_empl_ail()}"
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"{ad_corp_empl_kain()}"
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"{ad_corp_empl_rev()}"
                    elif corp_emp == 'Син Корп':
                        corp_emp = f"{ad_corp_empl_sin()}"
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"{ad_corp_empl_morde()}"
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"{ad_corp_empl_all()}"
                panel_message = corp_emp

            elif panel_ad_type == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        corp_emp = random.choice(data["corporation"])
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                panel_message = corp_emp
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif panel_mess_rnd >= 205:
            spam_def = random.randint(1, 100)
            if spam_def < 100:
                if spam_type == 'имплант':
                    panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(users['implant'])}. """ \
                                    f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                elif spam_type == 'посылка':
                    panel_message = f"""```ml\n'РМ' {random.choice(users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                    f"""{random.choice(users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\n'РМ' {random.choice(users['other']).capitalize()}: {spam_adress_rnd}```"""
            else:
                panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

        else:
            panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

        await ctx.send(panel_message)

# ЭТО ПАНЕЛЬ МОССИ
@commands.command(name='панельФрейя_Элиор')
async def panel_6(ctx, n=1):
    if (n < 1) or (n > 10):
        await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
        price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
        price = random.choice([price_num, random.choice(ad['price'])])

        halfer = random.randint(1, 2)

        spam_type = random.choice(users['spam_type'])
        adress = random.randint(1000000000, 9999999999)

        if halfer == 1:
            spam_adress_rnd = adress
        elif halfer == 2:
            spam_adress_rnd = number_id()

        if panel_mess_rnd <= 100:
            spam_type = random.choice(['хорниспам', 'разное'])
            if spam_type == 'хорниспам':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['whichs']).upper()} {random.choice(ad['who']).upper()} """ \
                                f"""{random.choice(ad['what_do']).upper()}: {number_id()}```"""

            elif spam_type == 'разное':
                panel_message = f"""```ml\n'ALL' {random.choice(ad['which']).upper()} {random.choice(ad['what'])} """ \
                                f"""{random.choice(ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                f"""ноксов: {number_id()}```"""
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
            panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                    'трудоустройство корпорации']
            panel_ad_type = random.choice(panel_ad_type_list)
            ft_time = random.choice(
                ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            if panel_ad_type == 'мероприятие корпорации':
                corp_corp_fest = random.choice(data['corporation'])
                if corp_corp_fest == 'Д':
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                                    f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                                    f"""{(corp_corp_fest).upper()}. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {adress}```"""

            elif panel_ad_type == 'трудоустройство корпорации':
                corp_emp = random.choice(data['corporation'])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    if corp_emp == 'Пантеон Нокс':
                        corp_emp = f"{ad_corp_empl_nox()}"
                    elif corp_emp == 'Холдинг Хорнс':
                        corp_emp = f"{ad_corp_empl_hh()}"
                    elif corp_emp == 'Дом Аэтерн':
                        corp_emp = f"{ad_corp_empl_aet()}"
                    elif corp_emp == 'Дом Ойр':
                        corp_emp = f"{ad_corp_empl_oir()}"
                    elif corp_emp == 'Тентакорп':
                        corp_emp = f"{ad_corp_empl_tenta()}"
                    elif corp_emp == 'Магнакорп':
                        corp_emp = f"{ad_corp_empl_magna()}"
                    elif corp_emp == 'Королевство Вистара':
                        corp_emp = f"{ad_corp_empl_vis()}"
                    elif corp_emp == 'Королевство Прима':
                        corp_emp = f"{ad_corp_empl_prima()}"
                    elif corp_emp == 'Королевство Айль':
                        corp_emp = f"{ad_corp_empl_ail()}"
                    elif corp_emp == 'Пантеон Кайн':
                        corp_emp = f"{ad_corp_empl_kain()}"
                    elif corp_emp == 'Церковь Прозрения':
                        corp_emp = f"{ad_corp_empl_rev()}"
                    elif corp_emp == 'Син Корп':
                        corp_emp = f"{ad_corp_empl_sin()}"
                    elif corp_emp == 'Мордекорп':
                        corp_emp = f"{ad_corp_empl_morde()}"
                    elif corp_emp == 'Все и Вся Инк':
                        corp_emp = f"{ad_corp_empl_all()}"
                panel_message = corp_emp

            elif panel_ad_type == 'реклама корпорации':
                corp_emp = random.choice(data["corporation"])
                if corp_emp == 'Д':
                    corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                else:
                    chanse_all = random.randint(1, 5)
                    if chanse_all == 1:
                        corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                    f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    else:
                        corp_emp = random.choice(data["corporation"])
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                        f"""{random.choice(data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                        f"""{random.choice(data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                        f"""{random.choice(data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                        f"""{random.choice(data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                        f"""{random.choice(data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                        f"""{random.choice(data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                        f"""{random.choice(data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                        f"""{random.choice(data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                        f"""{random.choice(data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                        f"""{random.choice(data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                        f"""{random.choice(data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                        f"""{random.choice(data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                        f"""{random.choice(data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                panel_message = corp_emp
            else:
                panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

        elif panel_mess_rnd >= 205:
            spam_def = random.randint(1, 100)
            if spam_def < 100:
                if spam_type == 'имплант':
                    panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(users['implant'])}. """ \
                                    f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                elif spam_type == 'посылка':
                    panel_message = f"""```ml\n'РМ' {random.choice(users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                    f"""{random.choice(users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\n'РМ' {random.choice(users['other']).capitalize()}: {spam_adress_rnd}```"""
            else:
                panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

        else:
            panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

        await ctx.send(panel_message)

# ------- осколки

@commands.command(name='осколок')
async def random_fragment(ctx, n='0'):

    place_c = random.choice(quest['place_corp']).title()
    race_list_1 = ["человек", "гарпия", "сатир", "виверна"]
    race_list_2 = ["человек", "тифон", "сатир", "виверна", "тельхин"]
    race_list_3 = ["человек", "тифон", "гарпия", "виверна", "тельхин"]
    if (place_c == 'Магнакорп') or (place_c == 'Тентакорп'):
        race_place_c = random.randint(1, 100)
        if (race_place_c > 25):
            race_place = f"тельхин"
        else:
            race_place = f"{random.choice(race_list_1)}"
    elif (place_c == 'Королевство Вистара') or (place_c == 'Королевство Прима'):
        race_place_c = random.randint(1, 100)
        if (race_place_c > 25):
            race_place = f"тифон"
        else:
            race_place = f"{random.choice(race_list_1)}"
    elif (place_c == 'Королевство Айль') or (place_c == 'Церковь Прозрения'):
        race_place_c = random.randint(1, 100)
        if (race_place_c > 25):
            race_place = f"гарпия"
        else:
            race_place = f"{random.choice(race_list_2)}"
    elif (place_c == 'Холдинг Хорнс') or (place_c == 'Дом Ойр') or (place_c == 'Дом Аэтерн'):
        race_place_c = random.randint(1, 100)
        if (race_place_c > 25):
            race_place = f"сатир"
        else:
            race_place = f"{random.choice(race_list_3)}"
    else:
        race_place = f"{random.choice(npc['race'])}"

    num_corp = random.randint(1, 5)
    if num_corp == 1:
        dop_corp = f"{random.choice(quest['place_corp'])}"
    elif num_corp == 2:
        dop_corp = f"{random.choice(quest['place_corp'])}, {random.choice(quest['place_corp'])}"
    elif num_corp == 3:
        dop_corp = f"{random.choice(quest['place_corp'])}, {random.choice(quest['place_corp'])}, {random.choice(quest['place_corp'])}"
    elif num_corp == 4:
        dop_corp = f"{random.choice(quest['place_corp'])}, {random.choice(quest['place_corp'])}, {random.choice(quest['place_corp'])}, {random.choice(quest['place_corp'])}"
    else:
        dop_corp = f"—"

    low_l = random.randint(1, 5)
    if low_l == 1:
        low_l_d = f"\n- #1 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}"
    elif low_l == 2:
        low_l_d = f"\n- #1 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}\n" \
                    f"- #2 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}"
    elif low_l == 3:
        low_l_d = f"\n- #1 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}\n" \
                    f"- #2 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}\n" \
                    f"- #3 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}"
    elif low_l == 4:
        low_l_d = f"\n- #1 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}\n" \
                    f"- #2 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}\n" \
                    f"- #3 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}\n" \
                    f"- #4 специализация: {random.choice(quest['place_special'])}\n     особенность: {random.choice(quest['low_l_fea'])}"
    else:
        low_l_d = f"отсутствуют"

    if (n == '0'):
        await ctx.send("_Введите название осколка._")
        return
    elif (n not in (quest['place'])):
        await ctx.send("_Такого осколка не существует._")
        return
    else:
        response = f"```ОСКОЛОК #{n}\n\nКорпорация: {place_c}\nАрхонт: {race_place} ({random.choice(npc['class'])}" \
                    f" {random.choice(npc['podclass'])})\n" \
                    f"Специализация осколка: {random.choice(quest['place_special'])}\n" \
                    f"Присутствие других корпораций: {dop_corp}\nПрирода осколка: {random.choice(quest['place_origin'])}\n" \
                    f"Особенность: {random.choice(quest['place_fea'])}, {random.choice(quest['place_fea'])}\nНижние уровни: {low_l_d}```"


        await ctx.send(response)

# ------- новости

@commands.command(name='новостиосколка')
async def news_isl(ctx, m='0', n=1):

    if (n < 1) or (n > 5):
        await ctx.send("_Запрос не может превышать 5 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        if (m == '0'):
            await ctx.send("_Введите название осколка._")
            return
        elif (m not in (quest['place'])):
            await ctx.send("_Такого осколка не существует._")
            return
        else:
            rnd_news = random.randint(1, 10)
            if rnd_news > 8:
                response = f"""```ml\nNEWS На осколке #{m} {random.choice(data['news_isl'])}```"""
            else:
                response = f"""```ml\nNEWS На осколке #{m} {random.choice(data['news_isl_corp'])} {random.choice(data['corporation'])}.```"""
            await ctx.send(response)

@commands.command(name='новости')
async def news_gen(ctx, n=1):
    if (n < 1) or (n > 5):
        await ctx.send("_Запрос не может превышать 5 сообщений за раз ради вашей безопасности._")
        return
    await ctx.message.delete()

    for i in range(n):
        rnd_news = random.randint(1, 10)
        if rnd_news > 8:
            response = f"""```ml\nNEWS На осколке #{random.choice(quest['place'])} {random.choice(data['news_isl'])}```"""
        elif rnd_news < 2:
            corp_corp_fest = random.choice(data['corporation'])
            ft_time = random.choice(['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])
            adress = random.randint(1000000000, 9999999999)
            response = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(quest['place'])} """ \
                        f"""{random.choice(ad['fest_action'])} {random.choice(ad['fest_type_corp'])} """ \
                        f"""▶ {(corp_corp_fest).upper()} ◀. {random.choice(ad['fest_what_do']).capitalize()}! """ \
                        f"""Узнать больше информации: {adress}```"""
        else:
            response = f"""```ml\nNEWS На осколке #{random.choice(quest['place'])} {random.choice(data['news_isl_corp'])} {random.choice(data['corporation'])}.```"""
        await ctx.send(response)


@commands.command(name='тест')
async def test(ctx, user='0', *, args):
    users_list = (users['users_list'])

    message = f"""```ml\n'РМ' {(args)}```"""
    await ctx.message.delete()

    pattern = re.compile("[0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]")

    if user in ("тест"):
        channel = client.get_channel(811399149303234615)
    elif user in ("тестовый"):
        channel = client.get_channel(811399149303234615)
    else:
        if pattern.match(user):
            channel = client.get_channel(811399149303234615)
            mess_us = f"_** **\nПолучатель: {user} (неизвестный номер)\nСтатус: отправлено_{message}"
            await ctx.send(mess_us)
            await channel.send(message)
        else:
            mess_us = f"_** **\nПолучатель: не определен (ошибка номера)\nСтатус: ОШИБКА_{message}"
            await ctx.send(mess_us)
        return

    mess_us = f"_** **\nПолучатель: {user}\nСтатус: отправлено_{message}"
    await ctx.send(mess_us)
    await channel.send(message)






#------- общие дефы

def amount():
    return f'{random.randint(100, 10000)}'.lower()

def mfr():
    if random.choice(data['type']) == 'самопал':
        manufacturer = '—'
    else:
        manufacturer = f'{random.choice(data["corporation"])}'
    return manufacturer.lower()

def access():
    if random.choice(data['kind_accessory']) == 'имплант':
        acc = f'имплант (Защита: {random.choice(data["protection"])})'
    else:
        list = ["ручной", "нательный", "модуль к снаряжению"]
        acc = f'{random.choice(list)}'
    return acc.lower()

def item():
    type_item = ["случайный", "имплант"]
    if random.choice(type_item) == 'имплант':
        itm = f'имплант (защита:{random.choice(data["protection"])})'
    else:
        itm = f'случайный'
    return itm.lower()

def m_amount():
    if random.choice(data['protection']) == 'есть':
        money = f'нет доступа (защищено)'
    else:
        money = f'{amount()}'
    return money.lower()

def number_id():
    num_idf = f'{random.randint(100000, 999999)}-{random.randint(100000, 999999)}-{random.randint(100000, 999999)}'
    return num_idf.lower()

def ad_corp_empl_nox():
    ad_nox = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n\nМы создали этот город, и мы можем дать тем, кто помогает нам строить и защищать его:\n""" \
                f"""✔ Приоритет обслуживания Орденам Пантеона Нокс\n""" \
                f"""✔ Повышенные лимиты всех подписок и доступ к особым подпискам закрытым для публики\n""" \
                f"""✔ Работу в самой престижной и уважаемой корпорации, что творит историю\n""" \
                f"""✔ Шедрые премии, зарплата, страховка, гарантии - чтобы вам никогда не пришлось боятся за свое или своих близких будушее\n\n""" \
                f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["nox_vac"])}\n- {random.choice(data["nox_vac"])}\n- {random.choice(data["nox_vac"])}\n\n""" \
                f"""Станьте частью тех, на чьих плечах стоит этот город!\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
    return ad_nox

def ad_corp_empl_hh():
    ad_hh = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n\nС нами вы:\n""" \
                    f"""✔ Работаете на уважаемой, статусной и солидной работе\n""" \
                    f"""✔ Получаете приоритет в пользовании услугами корпорации\n""" \
                    f"""✔ Имеете шанс проявить свои дизайнерские таланты\n""" \
                    f"""✔ Работаете с премиальными технологиями в комфортной и удобной среде\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["hh_vac"])}\n- {random.choice(data["hh_vac"])}\n- {random.choice(data["hh_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: HornS-{random.randint(1000, 9999)}```"""
    return ad_hh

def ad_corp_empl_aet():
    ad_aet = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n\nС нами вы:\n""" \
                    f"""✔ Получаете приоритет медицинского обслуживания в предприятиях корпорации\n""" \
                    f"""✔ Получаете медицинскую страховку пропорционально вашему статусу в корпорации\n""" \
                    f"""✔ Работаете на уважаемой работе в корпорации которая спасает жизни\n""" \
                    f"""✔ Работаете на самой безопасной работе, в корпорации где наименьший процент рабочих травм\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["aet_vac"])}\n- {random.choice(data["aet_vac"])}\n- {random.choice(data["aet_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: Aethern-{random.randint(1000, 9999)}```"""

    return ad_aet

def ad_corp_empl_oir():
    ad_oir = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n\nС нами вы:\n""" \
                    f"""✔ Будете знать, что то, что вы создаете - простоит века\n""" \
                    f"""✔ Будете уверенны в завтра с надежными контрактами и графиками выплат\n""" \
                    f"""✔ Будете застрахованы на случай производственных травм\n""" \
                    f"""✔ Получите шанс работать даже имея минимальное образование\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["oir_vac"])}\n- {random.choice(data["oir_vac"])}\n- {random.choice(data["oir_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: OirS-{random.randint(1000, 9999)}```"""
    return ad_oir

def ad_corp_empl_tenta():
    ad_tenta = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n\nПредлагает:\n""" \
                    f"""✔ Работу с отключенным разумом, не работайте ни дня в своей жизни\n""" \
                    f"""✔ Возможность заработать на продаже своих знаний, заработок без единого движения\n""" \
                    f"""✔ Мудрое управление и подобранный под вас коллектив, ведь мы читаем ваши мысли\n""" \
                    f"""✔ Доступ к базам данных для загрузки навыков для повышения квалификации\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["tenta_vac"])}\n- {random.choice(data["tenta_vac"])}\n- {random.choice(data["tenta_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
    return ad_tenta

def ad_corp_empl_magna():
    ad_magna = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n\nПредлагает:\n""" \
                    f"""✔ Работу с передовыми технологиями Магнавеб, за которыми - будущее\n""" \
                    f"""✔ Опции удаленной работы из дома через Магнавеб\n""" \
                    f"""✔ Бонусы и повышенные лимиты пользования Магнавеб для работников\n""" \
                    f"""✔ Неограниченный доступ к Когна, Ковен и Стрим для работников\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["magna_vac"])}\n- {random.choice(data["magna_vac"])}\n- {random.choice(data["magna_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
    return ad_magna

def ad_corp_empl_vis():
    ad_vis = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n\nМы гарантируем вам:\n""" \
                    f"""✔ Заботу, дружный коллектив, мудрое покровительство без необходимости волноваться о будущем\n""" \
                    f"""✔ Предоставление еды, воды и всего критически необходимого - корпорацией\n""" \
                    f"""✔ Трудоустройство с обучением, адаптацией тела и имплантацией за счет корпорации\n""" \
                    f"""✔ Эмпатическое стимулирование что сделает ваши дни светлее, а работу - желаннее\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["vis_vac"])}\n- {random.choice(data["vis_vac"])}\n- {random.choice(data["vis_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
    return ad_vis

def ad_corp_empl_prima():
    ad_prima = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n\nМы гарантируем вам:\n""" \
                    f"""✔ Обеспечение трудоустройства любому кто пожелает стать частью Улья\n""" \
                    f"""✔ Мудрое управление, опыт ассимиляции всех рас длинной в тысячелетия\n""" \
                    f"""✔ Безопасность и порядок на работе и в вашем Улье\n""" \
                    f"""✔ Обеспечение собственного жилья любому кто пожелает стать частью Улья\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["prima_vac"])}\n- {random.choice(data["prima_vac"])}\n- {random.choice(data["prima_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
    return ad_prima

def ad_corp_empl_ail():
    ad_ail = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n\nМы гарантируем вам:\n""" \
                    f"""✔ Банковский счет и виртуальный кошелек с выгодными условиями для каждого работника\n""" \
                    f"""✔ Комфортную рабочую среду\n""" \
                    f"""✔ Возможность получения премий круизами на наших лучших лайнерах\n""" \
                    f"""✔ Приоритет в обслуживании для работников коорпорации\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["ail_vac"])}\n- {random.choice(data["ail_vac"])}\n- {random.choice(data["ail_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: IleS-{random.randint(1000, 9999)}```"""
    return ad_ail

def ad_corp_empl_kain():
    ad_kain = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n\nМы предлагаем вам:\n""" \
                    f"""✔ Шанс работы в мультикультурном и всерассовом коллективе без дискриминации\n""" \
                    f"""✔ Шанс работы с самыми передовыми технологиями что соединяют усилия всех рас\n""" \
                    f"""✔ Шанс трудоустройства и получения жилья в наших Замках и Поместьях\n""" \
                    f"""✔ Шанс прохождения обучения непревзойденного качества и последущего становления ангелом или даже аватаром архонта\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["kain_vac"])}\n- {random.choice(data["kain_vac"])}\n- {random.choice(data["kain_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: KineS-{random.randint(1000, 9999)}```"""
    return ad_kain

def ad_corp_empl_rev():
    ad_rev = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n\nМы предлагаем вам:\n""" \
                    f"""✔ Прозрение, стабильность, надежду, социальную и психологическую помощь от тех, кто знает вашу душу лучше вас\n""" \
                    f"""✔ Правильно подобранное трудоустройство и коллектив, ведь мы знаем чего вы желаете\n""" \
                    f"""✔ Всестороннюю помощь в устройстве жизни для всех работников корпорации\n""" \
                    f"""✔ Возможность помогать другим и вести их к надежде и свету\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["rev_vac"])}\n- {random.choice(data["rev_vac"])}\n- {random.choice(data["rev_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
    return ad_rev

def ad_corp_empl_sin():
    chanse_sin = random.randint(1, 3)
    if chanse_sin == 1:
        ad_sin = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nПредлагает:\n""" \
                    f"""✔ Работу от которой вы будете получать удовольствие\n""" \
                    f"""✔ Бонусы в заведениях корпорации для сотрудников\n""" \
                    f"""✔ Интересные и креативные проекты\n""" \
                    f"""✔ Возможность творческой самореализаци\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
    elif chanse_sin == 2:
        ad_sin = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nГарантирует:\n""" \
                    f"""✔ Адаптивный график работы\n""" \
                    f"""✔ Регулярные корпоративы и мероприятия для работников\n""" \
                    f"""✔ Дружный коллектив\n""" \
                    f"""✔ Работу без излишней бюрократии\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
    elif chanse_sin == 3:
        ad_sin = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nС нами вы:\n""" \
                    f"""✔ Никогда не заскучаете\n""" \
                    f"""✔ Найдете коллектив со схожими интересами\n""" \
                    f"""✔ Будете говорить "жеще папочка" сердитому начальнику\n""" \
                    f"""✔ Будете работать в корпорации которая честно смотрит на себя и на вас\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n- {random.choice(data["sin_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
    return ad_sin

def ad_corp_empl_morde():
    ad_morde = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n\nПредлагает:\n""" \
                    f"""✔ Трудоустройство без образования\n""" \
                    f"""✔ Имплантацию и подготовку за счет корпорации\n""" \
                    f"""✔ Стабильные и долгие контракты\n""" \
                    f"""✔ Страховку с выплатами семье и близким в случае смерти\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["mord_vac"])}\n- {random.choice(data["mord_vac"])}\n- {random.choice(data["mord_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
    return ad_morde

def ad_corp_empl_all():
    ad_all = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n\nПредлагает:\n""" \
                    f"""✔ Работу поблизости от дома\n""" \
                    f"""✔ Бонусы в магазинах корпорации для сотрудников\n""" \
                    f"""✔ Премии продукцией компании которую вы выберете\n""" \
                    f"""✔ Трудоустройство с минимальным образованием\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(data["ae_vac"])}\n- {random.choice(data["ae_vac"])}\n- {random.choice(data["ae_vac"])}\n\n""" \
                    f"""Запишитесь сегодня!\nПодробности: AllS-{random.randint(1000, 9999)}```"""
    return ad_all

def stuff(client: commands.Bot):
        client.add_command(random_trophy)
        client.add_command(random_weapon)
        client.add_command(random_main_armor)
        client.add_command(random_extra_armor)
        client.add_command(random_auxiliary_equipment)
        client.add_command(random_consumable)
        client.add_command(random_accessory)
        client.add_command(random_device)
        client.add_command(random_simple_item)
        client.add_command(random_valuable_item)
        client.add_command(random_money)
        client.add_command(money)
        client.add_command(trophy_commands)

        client.add_command(random_npc)

        client.add_command(random_quest)
        client.add_command(random_quest_isl)

        client.add_command(random_candy)

        client.add_command(random_ad)

        client.add_command(random_fragment)

        client.add_command(mailing)
        client.add_command(pm_send)

        client.add_command(panel_all)
        client.add_command(panel_1)
        client.add_command(panel_2)
        client.add_command(panel_3)
        client.add_command(panel_4)
        client.add_command(panel_5)
        client.add_command(panel_6)

        client.add_command(news_isl)
        client.add_command(news_gen)

        client.add_command(test)

async def main():
    global client
    client = ArchLight( 
        intents=discord.Intents.all(),
        data_folder='./Data/',
        activity= None,
        config='config.json')

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    stuff(client)
    # Это много говнокода
    global data 
    data = client.data
    global users 
    users = client.dis_users
    global npc
    npc = client.npc
    global quest
    quest = client.quest
    global ad
    ad = client.ad
    global candy
    candy = client.candy

    await client.start(client.config.token)

if __name__ == '__main__':
    asyncio.run(main())