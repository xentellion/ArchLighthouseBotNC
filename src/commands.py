import re
import random
from discord.ext import commands
from client import ArchLight
from static import StaticMethods


class Commands(commands.Cog):
    def __init__(self, bot: ArchLight):
        self.bot = bot
        super().__init__()

    @commands.command(name='квест')
    async def random_quest(self, ctx, n=1):
        if (n < 1) or (n > 5):
            await ctx.send("В запрос принимаются значения от 1 до 5")
            return
        await ctx.message.delete()
        for i in range(n):

            form = random.choice(self.bot.quest['quest_form'])
            if form == 'устранение или охота':
                form = f'{random.choice(self.bot.quest["hunt"])}'
            elif form == 'спасение':
                form = f'{random.choice(self.bot.quest["save"])} {random.choice(self.bot.quest["save_from"])}'
            elif form == 'кража или захват':
                form = f'{random.choice(self.bot.quest["grab"])}'
            elif form == 'саботаж или шпионаж':
                form = f'{random.choice(self.bot.quest["sabotage"])}'
            elif form == 'охрана или защита':
                form = f'{random.choice(self.bot.quest["protect"])} от {random.choice(self.bot.quest["from"])}'
            elif form == 'расследование или исследование':
                form = f'{random.choice(self.bot.quest["study"])}'
            elif form == 'уникальное':
                form = f'уникальное'

            dif = random.choice(self.bot.quest['difficulty'])
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
                place = f"{random.choice(self.bot.quest['place_dark'])}"
            else:
                place = f"осколок {random.choice(self.bot.quest['place'])}"

            response = f"```Миссия #{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1, 99)}\n\n" \
                        f"Вид: {form}\nМесто: {place}\nСложность: {dif}\n" \
                        f"Время: {time}\nОсобенность: {random.choice(self.bot.quest['peculiarity'])}, {random.choice(self.bot.quest['peculiarity'])}```"

            await ctx.send(response)

    @commands.command(name='квестосколка')
    async def random_quest_isl(self, ctx, m='0', n=1):
        if (n < 1) or (n > 5):
            await ctx.send("В запрос принимаются значения от 1 до 5")
            return
        await ctx.message.delete()
        for i in range(n):

            form = random.choice(self.bot.quest['quest_form'])
            if form == 'устранение или охота':
                form = f'{random.choice(self.bot.quest["hunt"])}'
            elif form == 'спасение':
                form = f'{random.choice(self.bot.quest["save"])} {random.choice(self.bot.quest["save_from"])}'
            elif form == 'кража или захват':
                form = f'{random.choice(self.bot.quest["grab"])}'
            elif form == 'саботаж или шпионаж':
                form = f'{random.choice(self.bot.quest["sabotage"])}'
            elif form == 'охрана или защита':
                form = f'{random.choice(self.bot.quest["protect"])} от {random.choice(self.bot.quest["from"])}'
            elif form == 'расследование или исследование':
                form = f'{random.choice(self.bot.quest["study"])}'
            elif form == 'уникальное':
                form = f'уникальное'

            dif = random.choice(self.bot.quest['difficulty'])
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
                place = f"{random.choice(self.bot.quest['place_dark'])}"
            else:
                place = f"осколок {random.choice(self.bot.quest['place'])}"

            response = f"```Миссия #{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1, 99)}\n\n" \
                        f"Вид: {form}\nМесто: {m}\nСложность: {dif}\n" \
                        f"Время: {time}\nОсобенность: {random.choice(self.bot.quest['peculiarity'])}, {random.choice(self.bot.quest['peculiarity'])}```"

            await ctx.send(response)
    # ------- конфеты

    @commands.command(name='киберконфетка')
    async def random_candy(self, ctx, n=1):
        if (n < 1) or (n > 5):
            await ctx.send("В запрос принимаются значения от 1 до 5")
            return
        await ctx.message.delete()

        for i in range(n):
            candy_type = random.choice(self.bot.candy['candy_type'])
            response = f"```#ОШИБКА ЧТЕНИЯ ЧИПА```"
            if candy_type == 'скидка корпорации':
                response = f"""```ml\n{random.choice(self.bot.candy['disk']).capitalize()} {random.choice(self.bot.candy['action'])} """ \
                            f"""в корпорации {random.choice(self.bot.data['corporation']).title()} """ \
                            f"""(только в официальных магазинах) по коду """ \
                            f"""{random.randint(10, 9999)}-{random.randint(10, 9999)} (активация кода разовая, код действителен с момента """ \
                            f"""его считывания в течение {random.randint(5, 20)}-ти {random.choice(['дней', 'часов'])})```"""

            elif candy_type == 'скидка':
                response = f"""```ml\n{random.choice(self.bot.candy['disk']).capitalize()} {random.choice(self.bot.candy['action'])} у привратника по коду """ \
                            f"""{random.randint(10, 9999)}-{random.randint(10, 9999)} (активация кода разовая, код действителен с момента """ \
                            f"""его считывания в течение {random.randint(5, 20)}-ти {random.choice(['дней', 'часов'])})```"""

            elif candy_type == 'пожелание':
                response = f"""```ml\n{random.choice(self.bot.candy['time']).capitalize()} {random.choice(self.bot.candy['whom'])} соблаговолит """ \
                            f"""{random.choice(self.bot.candy['luck'])} {random.choice(self.bot.candy['in_what'])}```"""

            await ctx.send(response)

    # ------- реклама

    @commands.command(name='реклама')
    async def random_ad(self, ctx, n=1):
        if (n < 1) or (n > 5):
            await ctx.send("В запрос принимаются значения от 1 до 5")
            return
        await ctx.message.delete()

        for i in range(n):
            #response = f"```#ОШИБКА ЧТЕНИЯ ЧИПА```"

            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)
            ft_time = random.choice(['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

            adress = random.randint(1000000000, 9999999999)

            ad_type_per = random.randint(1, 10)

            if ad_type_per > 5:
                ad_type_corp_list = ['акция корпорации', 'мероприятие корпорации', 'реклама корпорации', 'трудоустройство корпорации']
                ad_type_corp = random.choice(ad_type_corp_list)

                if ad_type_corp == 'акция корпорации':
                    corp_corp_disc = random.choice(self.bot.data['corporation'])
                    if corp_corp_disc == '':
                        response = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        response = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\nТОЛЬКО СЕГОДНЯ! {random.choice(self.bot.candy['disk'])} {random.choice(self.bot.candy['action'])} """ \
                                        f"""в корпорации ▶ {(corp_corp_disc).upper()} ◀ (акция действует только в официальных магазинах) """ \
                                        f"""Узнать полную информацию о действии акции: """ \
                                        f"""{adress}```"""

                elif ad_type_corp == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == '':
                        response = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        response = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""▶ {(corp_corp_fest).upper()} ◀. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif ad_type_corp == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == '':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n\nМы создали этот город, и мы можем дать тем, кто помогает нам строить и защищать его:\n""" \
                                        f"""✔ Приоритет обслуживания Орденам Пантеона Нокс\n""" \
                                        f"""✔ Повышенные лимиты всех подписок и доступ к особым подпискам закрытым для публики\n""" \
                                        f"""✔ Работу в самой престижной и уважаемой корпорации, что творит историю\n""" \
                                        f"""✔ Шедрые премии, зарплата, страховка, гарантии - чтобы вам никогда не пришлось боятся за свое или своих близких будушее\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["nox_vac"])}\n- {random.choice(self.bot.data["nox_vac"])}\n- {random.choice(self.bot.data["nox_vac"])}\n\n""" \
                                        f"""Станьте частью тех, на чьих плечах стоит этот город!\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n\nС нами вы:\n""" \
                                        f"""✔ Работаете на уважаемой, статусной и солидной работе\n""" \
                                        f"""✔ Получаете приоритет в пользовании услугами корпорации\n""" \
                                        f"""✔ Имеете шанс проявить свои дизайнерские таланты\n""" \
                                        f"""✔ Работаете с премиальными технологиями в комфортной и удобной среде\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["hh_vac"])}\n- {random.choice(self.bot.data["hh_vac"])}\n- {random.choice(self.bot.data["hh_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n\nС нами вы:\n""" \
                                        f"""✔ Получаете приоритет медицинского обслуживания в предприятиях корпорации\n""" \
                                        f"""✔ Получаете медицинскую страховку пропорционально вашему статусу в корпорации\n""" \
                                        f"""✔ Работаете на уважаемой работе в корпорации которая спасает жизни\n""" \
                                        f"""✔ Работаете на самой безопасной работе, в корпорации где наименьший процент рабочих травм\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["aet_vac"])}\n- {random.choice(self.bot.data["aet_vac"])}\n- {random.choice(self.bot.data["aet_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n\nС нами вы:\n""" \
                                        f"""✔ Будете знать, что то, что вы создаете - простоит века\n""" \
                                        f"""✔ Будете уверенны в завтра с надежными контрактами и графиками выплат\n""" \
                                        f"""✔ Будете застрахованы на случай производственных травм\n""" \
                                        f"""✔ Получите шанс работать даже имея минимальное образование\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["oir_vac"])}\n- {random.choice(self.bot.data["oir_vac"])}\n- {random.choice(self.bot.data["oir_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n\nПредлагает:\n""" \
                                        f"""✔ Работу с отключенным разумом, не работайте ни дня в своей жизни\n""" \
                                        f"""✔ Возможность заработать на продаже своих знаний, заработок без единого движения\n""" \
                                        f"""✔ Мудрое управление и подобранный под вас коллектив, ведь мы читаем ваши мысли\n""" \
                                        f"""✔ Доступ к базам данных для загрузки навыков для повышения квалификации\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["tenta_vac"])}\n- {random.choice(self.bot.data["tenta_vac"])}\n- {random.choice(self.bot.data["tenta_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n\nПредлагает:\n""" \
                                        f"""✔ Работу с передовыми технологиями Магнавеб, за которыми - будущее\n""" \
                                        f"""✔ Опции удаленной работы из дома через Магнавеб\n""" \
                                        f"""✔ Бонусы и повышенные лимиты пользования Магнавеб для работников\n""" \
                                        f"""✔ Неограниченный доступ к Когна, Ковен и Стрим для работников\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["magna_vac"])}\n- {random.choice(self.bot.data["magna_vac"])}\n- {random.choice(self.bot.data["magna_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n\nМы гарантируем вам:\n""" \
                                        f"""✔ Заботу, дружный коллектив, мудрое покровительство без необходимости волноваться о будущем\n""" \
                                        f"""✔ Предоставление еды, воды и всего критически необходимого - корпорацией\n""" \
                                        f"""✔ Трудоустройство с обучением, адаптацией тела и имплантацией за счет корпорации\n""" \
                                        f"""✔ Эмпатическое стимулирование что сделает ваши дни светлее, а работу - желаннее\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["vis_vac"])}\n- {random.choice(self.bot.data["vis_vac"])}\n- {random.choice(self.bot.data["vis_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n\nМы гарантируем вам:\n""" \
                                        f"""✔ Обеспечение трудоустройства любому кто пожелает стать частью Улья\n""" \
                                        f"""✔ Мудрое управление, опыт ассимиляции всех рас длинной в тысячелетия\n""" \
                                        f"""✔ Безопасность и порядок на работе и в вашем Улье\n""" \
                                        f"""✔ Обеспечение собственного жилья любому кто пожелает стать частью Улья\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["prima_vac"])}\n- {random.choice(self.bot.data["prima_vac"])}\n- {random.choice(self.bot.data["prima_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n\nМы гарантируем вам:\n""" \
                                        f"""✔ Банковский счет и виртуальный кошелек с выгодными условиями для каждого работника\n""" \
                                        f"""✔ Комфортную рабочую среду\n""" \
                                        f"""✔ Возможность получения премий круизами на наших лучших лайнерах\n""" \
                                        f"""✔ Приоритет в обслуживании для работников коорпорации\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["ail_vac"])}\n- {random.choice(self.bot.data["ail_vac"])}\n- {random.choice(self.bot.data["ail_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n\nМы предлагаем вам:\n""" \
                                        f"""✔ Шанс работы в мультикультурном и всерассовом коллективе без дискриминации\n""" \
                                        f"""✔ Шанс работы с самыми передовыми технологиями что соединяют усилия всех рас\n""" \
                                        f"""✔ Шанс трудоустройства и получения жилья в наших Замках и Поместьях\n""" \
                                        f"""✔ Шанс прохождения обучения непревзойденного качества и последущего становления ангелом или даже аватаром архонта\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["kain_vac"])}\n- {random.choice(self.bot.data["kain_vac"])}\n- {random.choice(self.bot.data["kain_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n\nМы предлагаем вам:\n""" \
                                        f"""✔ Прозрение, стабильность, надежду, социальную и психологическую помощь от тех, кто знает вашу душу лучше вас\n""" \
                                        f"""✔ Правильно подобранное трудоустройство и коллектив, ведь мы знаем чего вы желаете\n""" \
                                        f"""✔ Всестороннюю помощь в устройстве жизни для всех работников корпорации\n""" \
                                        f"""✔ Возможность помогать другим и вести их к надежде и свету\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["rev_vac"])}\n- {random.choice(self.bot.data["rev_vac"])}\n- {random.choice(self.bot.data["rev_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Син Корп':
                            chanse_sin = random.randint(1, 3)
                            if chanse_sin == 1:
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nПредлагает:\n""" \
                                            f"""✔ Работу от которой вы будете получать удовольствие\n""" \
                                            f"""✔ Бонусы в заведениях корпорации для сотрудников\n""" \
                                            f"""✔ Интересные и креативные проекты\n""" \
                                            f"""✔ Возможность творческой самореализаци\n\n""" \
                                            f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n\n""" \
                                            f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif chanse_sin == 2:
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nГарантирует:\n""" \
                                            f"""✔ Адаптивный график работы\n""" \
                                            f"""✔ Регулярные корпоративы и мероприятия для работников\n""" \
                                            f"""✔ Дружный коллектив\n""" \
                                            f"""✔ Работу без излишней бюрократии\n\n""" \
                                            f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n\n""" \
                                            f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif chanse_sin == 3:
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nС нами вы:\n""" \
                                            f"""✔ Никогда не заскучаете\n""" \
                                            f"""✔ Найдете коллектив со схожими интересами\n""" \
                                            f"""✔ Будете говорить "жеще папочка" сердитому начальнику\n""" \
                                            f"""✔ Будете работать в корпорации которая честно смотрит на себя и на вас\n\n""" \
                                            f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n\n""" \
                                            f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n\nПредлагает:\n""" \
                                        f"""✔ Трудоустройство без образования\n""" \
                                        f"""✔ Имплантацию и подготовку за счет корпорации\n""" \
                                        f"""✔ Стабильные и долгие контракты\n""" \
                                        f"""✔ Страховку с выплатами семье и близким в случае смерти\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["mord_vac"])}\n- {random.choice(self.bot.data["mord_vac"])}\n- {random.choice(self.bot.data["mord_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n\nПредлагает:\n""" \
                                        f"""✔ Работу поблизости от дома\n""" \
                                        f"""✔ Бонусы в магазинах корпорации для сотрудников\n""" \
                                        f"""✔ Премии продукцией компании которую вы выберете\n""" \
                                        f"""✔ Трудоустройство с минимальным образованием\n\n""" \
                                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["ae_vac"])}\n- {random.choice(self.bot.data["ae_vac"])}\n- {random.choice(self.bot.data["ae_vac"])}\n\n""" \
                                        f"""Запишитесь сегодня!\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                    response = corp_emp

                elif ad_type_corp == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == '':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    response = corp_emp

            else:
                ad_type = random.choice(self.bot.ad['ad_type'])
                if ad_type == 'хорниспам':
                    response = f"""```ml\n{random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif ad_type == 'разное':
                    response = f"""```ml\n{random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""

                elif ad_type == 'покупка':
                    if halfer == 1:
                        response = f"""```ml\n{random.choice(self.bot.ad['how']).capitalize()} {random.choice(self.bot.ad['pers_action_purch'])} """ \
                                        f"""{random.choice(self.bot.ad['what_is_ad'])}: {StaticMethods.number_id()}```"""
                    elif halfer == 2:
                        response = f"""```ml\nСкупка {random.choice(self.bot.ad['not_obj'])}: {StaticMethods.number_id()}```"""

                elif ad_type == 'продажа':
                    if halfer == 1:
                        response = f"""```ml\n{random.choice(self.bot.ad['how']).capitalize()} {random.choice(self.bot.ad['pers_action_sale'])} """ \
                                        f"""{random.choice(self.bot.ad['what_is_ad'])}, {price}: {StaticMethods.umber_id()}```"""
                    elif halfer == 2:
                        response = f"""```ml\nПродажа {random.choice(self.bot.ad['not_obj'])}: {StaticMethods.number_id()}```"""

                elif ad_type == 'услуга':
                    response = f"""```ml\n{random.choice(self.bot.ad['service']).capitalize()}: {StaticMethods.number_id()}```"""

                elif ad_type == 'трудоустройство':
                    service_type = random.choice(['корп', 'проч'])
                    if service_type == 'корп':
                        response = f"""```ml\nПомогу с трудоустройством {random.choice(self.bot.ad['emp_corp_type'])} в корпорацию {random.choice(self.bot.data['corporation']).title()}: {StaticMethods.number_id()}```"""
                    elif service_type == 'проч':
                        response = f"""```ml\n{random.choice(self.bot.ad['employ']).capitalize()}: {StaticMethods.number_id()}```"""

                elif ad_type == 'мероприятие':
                    response = f"""```ml\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} {random.choice(self.bot.ad['fest_action'])} """ \
                                    f"""{random.choice(self.bot.ad['fest_type'])}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {StaticMethods.number_id()}```"""

                else:
                    response = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            await ctx.send(response)

    # ------- почта

    @commands.command(name='рассылка')
    async def mailing(self, ctx, *, args):
        users_id = (self.dis_users['user_id'])
        await ctx.message.delete()
        for channel_id in users_id:
            channel = self.bot.get_channel(channel_id)
            message = f"""```ml\n'ALL' {(args)}```"""
            await channel.send(message)
        mess_us = f"_** **\nСтатус: отправлено_{message}"
        await ctx.send(mess_us)

    @commands.command(name='сообщение')
    async def pm_send(self, ctx, user='0', *, args):

        if ctx.author.name in (self.dis_users['dis_users']):
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
            channel = self.bot.get_channel(1139663185696280656)
        elif user in ("дарк", "дарки"):
            channel = self.bot.get_channel(1135590381430522007)

        elif user in ("852457-825573-420543", 'МамаНэрр'):
            channel = self.bot.get_channel(1140030495971872789)
        elif user in ("228267-193891-112289", "Кварта"):
            channel = self.bot.get_channel(1140030495971872789)

        elif user == '637326-743969-354438':
            channel = self.bot.get_channel(1139534804631699616)
        elif user == '578500-104764-819584':
            channel = self.bot.get_channel(1139849919809720431)
        elif user == '164719-399449-473728':
            channel = self.bot.get_channel(1139534722402369536)
        elif user == '799935-168876-772625':
            channel = self.bot.get_channel(1143512126711922719)
        elif user == '038493-628490-174028':
            channel = self.bot.get_channel(1143992714292121741)
        else:
            if pattern.match(user):
                channel = self.bot.get_channel(1143987182877540573)
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
    async def panel_all(self, ctx, n=1):
        if (n < 1) or (n > 5):
            await ctx.send("_Запрос не может превышать 5 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)

            spam_type = random.choice(self.dis_users['spam_type'])
            adress = random.randint(1000000000, 9999999999)

            if halfer == 1:
                spam_adress_rnd = adress
            elif halfer == 2:
                spam_adress_rnd = StaticMethods.number_id()

            if panel_mess_rnd <= 100:
                spam_type = random.choice(['хорниспам', 'разное'])
                if spam_type == 'хорниспам':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif spam_type == 'разное':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
                panel_ad_type_list = ['акция корпорации', 'мероприятие корпорации', 'реклама корпорации',
                                        'трудоустройство корпорации', 'покупка', 'продажа', 'услуга', 'трудоустройство',
                                        'мероприятие']
                panel_ad_type = random.choice(panel_ad_type_list)
                ft_time = random.choice(['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

                if panel_ad_type == 'акция корпорации':
                    corp_corp = random.choice(self.bot.data['corporation'])
                    if corp_corp == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\nТОЛЬКО СЕГОДНЯ! {random.choice(self.bot.candy['disk'])} {random.choice(self.bot.candy['action'])} """ \
                                        f"""в корпорации {(corp_corp).upper()} (акция действует только в официальных магазинах) """ \
                                        f"""Узнать полную информацию о действии акции: """ \
                                        f"""{adress}```"""

                elif panel_ad_type == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""{(corp_corp_fest).upper()}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif panel_ad_type == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"{self.bot.ad_corp_empl_nox()}"
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"{self.bot.ad_corp_empl_hh()}"
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"{self.bot.ad_corp_empl_aet()}"
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"{self.bot.ad_corp_empl_oir()}"
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_tenta()}"
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_magna()}"
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"{self.bot.ad_corp_empl_vis()}"
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"{self.bot.ad_corp_empl_prima()}"
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"{self.bot.ad_corp_empl_ail()}"
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"{self.bot.ad_corp_empl_kain()}"
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"{self.bot.ad_corp_empl_rev()}"
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"{self.bot.ad_corp_empl_sin()}"
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"{self.bot.ad_corp_empl_morde()}"
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"{self.bot.ad_corp_empl_all()}"
                    panel_message = corp_emp

                elif panel_ad_type == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == 'Дом Аэтерн' or 'Холдинг Хорнс' or 'Дом Ойр':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            corp_emp = random.choice(self.bot.data["corporation"])
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    panel_message = corp_emp

                elif panel_ad_type == 'покупка':
                    if halfer == 1:
                        panel_message = f"""```ml\nAD {random.choice(self.bot.ad['how']).capitalize()} {random.choice(self.bot.ad['pers_action_purch'])} """ \
                                        f"""{random.choice(self.bot.ad['what_is_ad'])}: {StaticMethods.number_id()}```"""
                    elif halfer == 2:
                        panel_message = f"""```ml\nAD Скупка {random.choice(self.bot.ad['not_obj'])}: {StaticMethods.number_id()}```"""

                elif panel_ad_type == 'продажа':
                    if halfer == 1:
                        panel_message = f"""```ml\nAD {random.choice(self.bot.ad['how']).capitalize()} {random.choice(self.bot.ad['pers_action_sale'])} """ \
                                        f"""{random.choice(self.bot.ad['what_is_ad'])}, {price}: {StaticMethods.number_id()}```"""
                    elif halfer == 2:
                        panel_message = f"""```ml\nAD Продажа {random.choice(self.bot.ad['not_obj'])}: {StaticMethods.number_id()}```"""

                elif panel_ad_type == 'услуга':
                    panel_message = f"""```ml\nAD {random.choice(self.bot.ad['service']).capitalize()}: {StaticMethods.number_id()}```"""

                elif panel_ad_type == 'трудоустройство':
                    service_type = random.choice(['корп', 'проч'])
                    if service_type == 'корп':
                        panel_message = f"""```ml\nAD Помогу с трудоустройством {random.choice(self.bot.ad['emp_corp_type'])} в корпорацию {random.choice(self.bot.data['corporation']).title()}: {StaticMethods.number_id()}```"""
                    elif service_type == 'проч':
                        panel_message = f"""```ml\nAD {random.choice(self.bot.ad['employ']).capitalize()}: {StaticMethods.number_id()}```"""

                elif panel_ad_type == 'мероприятие':
                    panel_message = f"""```ml\nAD {ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} {random.choice(self.bot.ad['fest_action'])} """ \
                                    f"""{random.choice(self.bot.ad['fest_type'])}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                    f"""Узнать больше информации: {StaticMethods.number_id()}```"""

                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif panel_mess_rnd >= 205:
                spam_def = random.randint(1, 100)
                if spam_def < 100:
                    if spam_type == 'имплант':
                        panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(self.dis_users['implant'])}. """ \
                                        f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                    elif spam_type == 'посылка':
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                        f"""{random.choice(self.dis_users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                    else:
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['other']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

            else:
                panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

            await ctx.send(panel_message)


    @commands.command(name='лид')
    async def panel_1(self, ctx, n=1):
        if (n < 1) or (n > 10):
            await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)

            spam_type = random.choice(self.dis_users['spam_type'])
            adress = random.randint(1000000000, 9999999999)

            if halfer == 1:
                spam_adress_rnd = adress
            elif halfer == 2:
                spam_adress_rnd = StaticMethods.number_id()

            if panel_mess_rnd <= 100:
                spam_type = random.choice(['хорниспам', 'разное'])
                if spam_type == 'хорниспам':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif spam_type == 'разное':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
                panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                        'трудоустройство корпорации']
                panel_ad_type = random.choice(panel_ad_type_list)
                ft_time = random.choice(
                    ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

                if panel_ad_type == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == 'Д':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""{(corp_corp_fest).upper()}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif panel_ad_type == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"{self.bot.ad_corp_empl_nox()}"
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"{self.bot.ad_corp_empl_hh()}"
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"{self.bot.ad_corp_empl_aet()}"
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"{self.bot.ad_corp_empl_oir()}"
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_tenta()}"
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_magna()}"
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"{self.bot.ad_corp_empl_vis()}"
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"{self.bot.ad_corp_empl_prima()}"
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"{self.bot.ad_corp_empl_ail()}"
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"{self.bot.ad_corp_empl_kain()}"
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"{self.bot.ad_corp_empl_rev()}"
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"{self.bot.ad_corp_empl_sin()}"
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"{self.bot.ad_corp_empl_morde()}"
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"{self.bot.ad_corp_empl_all()}"
                    panel_message = corp_emp

                elif panel_ad_type == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            corp_emp = random.choice(self.bot.data["corporation"])
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    panel_message = corp_emp
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif panel_mess_rnd >= 205:
                spam_def = random.randint(1, 100)
                if spam_def < 100:
                    if spam_type == 'имплант':
                        panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(self.dis_users['implant'])}. """ \
                                        f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                    elif spam_type == 'посылка':
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                        f"""{random.choice(self.dis_users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                    else:
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['other']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

            else:
                panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

            await ctx.send(panel_message)

    #ЭТО ПАНЕЛЬ АСИ

    @commands.command(name='панельАрхимед')
    async def panel_2(self, ctx, n=1):
        if (n < 1) or (n > 10):
            await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)

            spam_type = random.choice(self.dis_users['spam_type'])
            adress = random.randint(1000000000, 9999999999)

            if halfer == 1:
                spam_adress_rnd = adress
            elif halfer == 2:
                spam_adress_rnd = StaticMethods.number_id()

            if panel_mess_rnd <= 100:
                spam_type = random.choice(['хорниспам', 'разное'])
                if spam_type == 'хорниспам':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif spam_type == 'разное':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
                panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                        'трудоустройство корпорации']
                panel_ad_type = random.choice(panel_ad_type_list)
                ft_time = random.choice(
                    ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

                if panel_ad_type == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == 'Д':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""{(corp_corp_fest).upper()}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif panel_ad_type == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"{self.bot.ad_corp_empl_nox()}"
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"{self.bot.ad_corp_empl_hh()}"
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"{self.bot.ad_corp_empl_aet()}"
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"{self.bot.ad_corp_empl_oir()}"
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_tenta()}"
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_magna()}"
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"{self.bot.ad_corp_empl_vis()}"
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"{self.bot.ad_corp_empl_prima()}"
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"{self.bot.ad_corp_empl_ail()}"
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"{self.bot.ad_corp_empl_kain()}"
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"{self.bot.ad_corp_empl_rev()}"
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"{self.bot.ad_corp_empl_sin()}"
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"{self.bot.ad_corp_empl_morde()}"
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"{self.bot.ad_corp_empl_all()}"
                    panel_message = corp_emp

                elif panel_ad_type == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            corp_emp = random.choice(self.bot.data["corporation"])
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    panel_message = corp_emp
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif panel_mess_rnd >= 205:
                spam_def = random.randint(1, 100)
                if spam_def < 100:
                    if spam_type == 'имплант':
                        panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(self.dis_users['implant'])}. """ \
                                        f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                    elif spam_type == 'посылка':
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                        f"""{random.choice(self.dis_users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                    else:
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['other']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

            else:
                panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

            await ctx.send(panel_message)

    # ЭТО ПАНЕЛЬ РОСТИКА

    @commands.command(name='панель637326-743969-354438')
    async def panel_3(self, ctx, n=1):
        if (n < 1) or (n > 10):
            await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)

            spam_type = random.choice(self.dis_users['spam_type'])
            adress = random.randint(1000000000, 9999999999)

            if halfer == 1:
                spam_adress_rnd = adress
            elif halfer == 2:
                spam_adress_rnd = StaticMethods.number_id()

            if panel_mess_rnd <= 100:
                spam_type = random.choice(['хорниспам', 'разное'])
                if spam_type == 'хорниспам':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif spam_type == 'разное':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
                panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                        'трудоустройство корпорации']
                panel_ad_type = random.choice(panel_ad_type_list)
                ft_time = random.choice(
                    ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

                if panel_ad_type == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == 'Д':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""{(corp_corp_fest).upper()}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif panel_ad_type == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"{self.bot.ad_corp_empl_nox()}"
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"{self.bot.ad_corp_empl_hh()}"
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"{self.bot.ad_corp_empl_aet()}"
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"{self.bot.ad_corp_empl_oir()}"
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_tenta()}"
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_magna()}"
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"{self.bot.ad_corp_empl_vis()}"
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"{self.bot.ad_corp_empl_prima()}"
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"{self.bot.ad_corp_empl_ail()}"
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"{self.bot.ad_corp_empl_kain()}"
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"{self.bot.ad_corp_empl_rev()}"
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"{self.bot.ad_corp_empl_sin()}"
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"{self.bot.ad_corp_empl_morde()}"
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"{self.bot.ad_corp_empl_all()}"
                    panel_message = corp_emp

                elif panel_ad_type == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            corp_emp = random.choice(self.bot.data["corporation"])
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    panel_message = corp_emp
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif panel_mess_rnd >= 205:
                spam_def = random.randint(1, 100)
                if spam_def < 100:
                    if spam_type == 'имплант':
                        panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(self.dis_users['implant'])}. """ \
                                        f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                    elif spam_type == 'посылка':
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                        f"""{random.choice(self.dis_users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                    else:
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['other']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

            else:
                panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

            await ctx.send(panel_message)

    # ЭТО ПАНЕЛЬ ФЛАМБО

    @commands.command(name='панельЗабвение')
    async def panel_4(self, ctx, n=1):
        if (n < 1) or (n > 10):
            await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)

            spam_type = random.choice(self.dis_users['spam_type'])
            adress = random.randint(1000000000, 9999999999)

            if halfer == 1:
                spam_adress_rnd = adress
            elif halfer == 2:
                spam_adress_rnd = StaticMethods.number_id()

            if panel_mess_rnd <= 100:
                spam_type = random.choice(['хорниспам', 'разное'])
                if spam_type == 'хорниспам':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif spam_type == 'разное':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
                panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации', 'покупка', 'продажа', 'услуга',
                                        'трудоустройство корпорации']
                panel_ad_type = random.choice(panel_ad_type_list)
                ft_time = random.choice(
                    ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

                if panel_ad_type == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == 'Д':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""{(corp_corp_fest).upper()}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif panel_ad_type == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"{self.bot.ad_corp_empl_nox()}"
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"{self.bot.ad_corp_empl_hh()}"
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"{self.bot.ad_corp_empl_aet()}"
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"{self.bot.ad_corp_empl_oir()}"
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_tenta()}"
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_magna()}"
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"{self.bot.ad_corp_empl_vis()}"
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"{self.bot.ad_corp_empl_prima()}"
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"{self.bot.ad_corp_empl_ail()}"
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"{self.bot.ad_corp_empl_kain()}"
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"{self.bot.ad_corp_empl_rev()}"
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"{self.bot.ad_corp_empl_sin()}"
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"{self.bot.ad_corp_empl_morde()}"
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"{self.bot.ad_corp_empl_all()}"
                    panel_message = corp_emp

                elif panel_ad_type == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            corp_emp = random.choice(self.bot.data["corporation"])
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    panel_message = corp_emp

                elif panel_ad_type == 'покупка':
                    if halfer == 1:
                        panel_message = f"""```ml\nAD {random.choice(self.bot.ad['how']).capitalize()} {random.choice(self.bot.ad['pers_action_purch'])} """ \
                                        f"""{random.choice(self.bot.ad['what_is_ad'])}: {StaticMethods.number_id()}```"""
                    elif halfer == 2:
                        panel_message = f"""```ml\nAD Скупка {random.choice(self.bot.ad['not_obj'])}: {StaticMethods.number_id()}```"""

                elif panel_ad_type == 'продажа':
                    if halfer == 1:
                        panel_message = f"""```ml\nAD {random.choice(self.bot.ad['how']).capitalize()} {random.choice(self.bot.ad['pers_action_sale'])} """ \
                                        f"""{random.choice(self.bot.ad['what_is_ad'])}, {price}: {StaticMethods.number_id()}```"""
                    elif halfer == 2:
                        panel_message = f"""```ml\nAD Продажа {random.choice(self.bot.ad['not_obj'])}: {StaticMethods.number_id()}```"""

                elif panel_ad_type == 'услуга':
                    panel_message = f"""```ml\nAD {random.choice(self.bot.ad['service']).capitalize()}: {StaticMethods.number_id()}```"""

                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""



            elif panel_mess_rnd >= 205:
                spam_def = random.randint(1, 100)
                if spam_def < 100:
                    if spam_type == 'имплант':
                        panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(self.dis_users['implant'])}. """ \
                                        f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                    elif spam_type == 'посылка':
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                        f"""{random.choice(self.dis_users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                    else:
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['other']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

            else:
                panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

            await ctx.send(panel_message)

    # ЭТО ПАНЕЛЬ ЧЕРЕПА

    @commands.command(name='панельKayzen')
    async def panel_5(self, ctx, n=1):
        if (n < 1) or (n > 10):
            await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)

            spam_type = random.choice(self.dis_users['spam_type'])
            adress = random.randint(1000000000, 9999999999)

            if halfer == 1:
                spam_adress_rnd = adress
            elif halfer == 2:
                spam_adress_rnd = StaticMethods.number_id()

            if panel_mess_rnd <= 100:
                spam_type = random.choice(['хорниспам', 'разное'])
                if spam_type == 'хорниспам':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif spam_type == 'разное':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
                panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                        'трудоустройство корпорации']
                panel_ad_type = random.choice(panel_ad_type_list)
                ft_time = random.choice(
                    ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

                if panel_ad_type == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == 'Д':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""{(corp_corp_fest).upper()}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif panel_ad_type == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"{self.bot.ad_corp_empl_nox()}"
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"{self.bot.ad_corp_empl_hh()}"
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"{self.bot.ad_corp_empl_aet()}"
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"{self.bot.ad_corp_empl_oir()}"
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_tenta()}"
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_magna()}"
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"{self.bot.ad_corp_empl_vis()}"
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"{self.bot.ad_corp_empl_prima()}"
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"{self.bot.ad_corp_empl_ail()}"
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"{self.bot.ad_corp_empl_kain()}"
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"{self.bot.ad_corp_empl_rev()}"
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"{self.bot.ad_corp_empl_sin()}"
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"{self.bot.ad_corp_empl_morde()}"
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"{self.bot.ad_corp_empl_all()}"
                    panel_message = corp_emp

                elif panel_ad_type == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            corp_emp = random.choice(self.bot.data["corporation"])
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    panel_message = corp_emp
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif panel_mess_rnd >= 205:
                spam_def = random.randint(1, 100)
                if spam_def < 100:
                    if spam_type == 'имплант':
                        panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(self.dis_users['implant'])}. """ \
                                        f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                    elif spam_type == 'посылка':
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                        f"""{random.choice(self.dis_users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                    else:
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['other']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

            else:
                panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

            await ctx.send(panel_message)

    # ЭТО ПАНЕЛЬ МОССИ
    @commands.command(name='панельФрейя_Элиор')
    async def panel_6(self, ctx, n=1):
        if (n < 1) or (n > 10):
            await ctx.send("_Запрос не может превышать 10 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            panel_mess_rnd = random.randint(1, 300)  # 1-100 спам, 101-200 реклама, 201-300 рассылка)
            price_num = f"{random.randrange(100, 3000, 10)} ноксов {random.choice(['с торгом', 'без торга'])}"
            price = random.choice([price_num, random.choice(self.bot.ad['price'])])

            halfer = random.randint(1, 2)

            spam_type = random.choice(self.dis_users['spam_type'])
            adress = random.randint(1000000000, 9999999999)

            if halfer == 1:
                spam_adress_rnd = adress
            elif halfer == 2:
                spam_adress_rnd = StaticMethods.number_id()

            if panel_mess_rnd <= 100:
                spam_type = random.choice(['хорниспам', 'разное'])
                if spam_type == 'хорниспам':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['whichs']).upper()} {random.choice(self.bot.ad['who']).upper()} """ \
                                    f"""{random.choice(self.bot.ad['what_do']).upper()}: {StaticMethods.number_id()}```"""

                elif spam_type == 'разное':
                    panel_message = f"""```ml\n'ALL' {random.choice(self.bot.ad['which']).upper()} {random.choice(self.bot.ad['what'])} """ \
                                    f"""{random.choice(self.bot.ad['what_is']).upper()} всего за {random.randrange(100, 1000, 10)} """ \
                                    f"""ноксов: {StaticMethods.number_id()}```"""
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif (panel_mess_rnd >= 101) and (panel_mess_rnd <= 200):
                panel_ad_type_list = ['мероприятие корпорации', 'реклама корпорации',
                                        'трудоустройство корпорации']
                panel_ad_type = random.choice(panel_ad_type_list)
                ft_time = random.choice(
                    ['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])

                if panel_ad_type == 'мероприятие корпорации':
                    corp_corp_fest = random.choice(self.bot.data['corporation'])
                    if corp_corp_fest == 'Д':
                        panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        panel_message = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                                        f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                                        f"""{(corp_corp_fest).upper()}. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                                        f"""Узнать больше информации: {adress}```"""

                elif panel_ad_type == 'трудоустройство корпорации':
                    corp_emp = random.choice(self.bot.data['corporation'])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        if corp_emp == 'Пантеон Нокс':
                            corp_emp = f"{self.bot.ad_corp_empl_nox()}"
                        elif corp_emp == 'Холдинг Хорнс':
                            corp_emp = f"{self.bot.ad_corp_empl_hh()}"
                        elif corp_emp == 'Дом Аэтерн':
                            corp_emp = f"{self.bot.ad_corp_empl_aet()}"
                        elif corp_emp == 'Дом Ойр':
                            corp_emp = f"{self.bot.ad_corp_empl_oir()}"
                        elif corp_emp == 'Тентакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_tenta()}"
                        elif corp_emp == 'Магнакорп':
                            corp_emp = f"{self.bot.ad_corp_empl_magna()}"
                        elif corp_emp == 'Королевство Вистара':
                            corp_emp = f"{self.d_corp_empl_vis()}"
                        elif corp_emp == 'Королевство Прима':
                            corp_emp = f"{self.bot.ad_corp_empl_prima()}"
                        elif corp_emp == 'Королевство Айль':
                            corp_emp = f"{self.bot.ad_corp_empl_ail()}"
                        elif corp_emp == 'Пантеон Кайн':
                            corp_emp = f"{self.bot.ad_corp_empl_kain()}"
                        elif corp_emp == 'Церковь Прозрения':
                            corp_emp = f"{self.bot.ad_corp_empl_rev()}"
                        elif corp_emp == 'Син Корп':
                            corp_emp = f"{self.bot.ad_corp_empl_sin()}"
                        elif corp_emp == 'Мордекорп':
                            corp_emp = f"{self.bot.ad_corp_empl_morde()}"
                        elif corp_emp == 'Все и Вся Инк':
                            corp_emp = f"{self.bot.ad_corp_empl_all()}"
                    panel_message = corp_emp

                elif panel_ad_type == 'реклама корпорации':
                    corp_emp = random.choice(self.bot.data["corporation"])
                    if corp_emp == 'Д':
                        corp_emp = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""
                    else:
                        chanse_all = random.randint(1, 5)
                        if chanse_all == 1:
                            corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                        f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                        else:
                            corp_emp = random.choice(self.bot.data["corporation"])
                            if corp_emp == 'Пантеон Нокс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_nox'])}\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Холдинг Хорнс':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_hh'])}\nПодробности: HornS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Аэтерн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_aet'])}\nПодробности: Aethern-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Все и Вся Инк':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_all'])}\nПодробности: AllS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Дом Ойр':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_oir'])}\nПодробности: OirS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Тентакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_tenta'])}\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Магнакорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_magna'])}\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Вистара':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_vis'])}\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Прима':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_prima'])}\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Королевство Айль':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_ail'])}\nПодробности: IleS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Пантеон Кайн':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_kine'])}\nПодробности: KineS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Церковь Прозрения':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_rev'])}\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Син Корп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_sin'])}\nПодробности: SinS-{random.randint(1000, 9999)}```"""
                            elif corp_emp == 'Мордекорп':
                                corp_emp = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n""" \
                                            f"""{random.choice(self.bot.data['ad_morde'])}\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
                    panel_message = corp_emp
                else:
                    panel_message = f"""```ml\nСообщение повреждено. Код ошибки: {random.randint(1000, 9999)}```"""

            elif panel_mess_rnd >= 205:
                spam_def = random.randint(1, 100)
                if spam_def < 100:
                    if spam_type == 'имплант':
                        panel_message = f"""```ml\n'РМ' Внимание! В вашем импланте магнакора {random.choice(self.dis_users['implant'])}. """ \
                                        f"""Срочно сделайте запрос по адресу: {adress} с пометкой 'Магнакор' для связи с пауком-специалистом.```"""
                    elif spam_type == 'посылка':
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['package']).capitalize()}. Код: {random.randint(1000, 9999)}-{random.randint(1000, 9999)}. """ \
                                        f"""{random.choice(self.dis_users['package_info']).capitalize()}: {spam_adress_rnd}```"""
                    else:
                        panel_message = f"""```ml\n'РМ' {random.choice(self.dis_users['other']).capitalize()}: {spam_adress_rnd}```"""
                else:
                    panel_message = f"""```ml\nСообщение было помечено как SPAM, проверьте настройки панели.```"""

            else:
                panel_message = f"""```ml\n'РМ' {spam_adress_rnd}```"""

            await ctx.send(panel_message)

    # ------- осколки

    @commands.command(name='осколок')
    async def random_fragment(self, ctx, n='0'):

        place_c = random.choice(self.bot.quest['place_corp']).title()
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
            race_place = f"{random.choice(self.npc['race'])}"

        num_corp = random.randint(1, 5)
        if num_corp == 1:
            dop_corp = f"{random.choice(self.bot.quest['place_corp'])}"
        elif num_corp == 2:
            dop_corp = f"{random.choice(self.bot.quest['place_corp'])}, {random.choice(self.bot.quest['place_corp'])}"
        elif num_corp == 3:
            dop_corp = f"{random.choice(self.bot.quest['place_corp'])}, {random.choice(self.bot.quest['place_corp'])}, {random.choice(self.bot.quest['place_corp'])}"
        elif num_corp == 4:
            dop_corp = f"{random.choice(self.bot.quest['place_corp'])}, {random.choice(self.bot.quest['place_corp'])}, {random.choice(self.bot.quest['place_corp'])}, {random.choice(self.bot.quest['place_corp'])}"
        else:
            dop_corp = f"—"

        low_l = random.randint(1, 5)
        if low_l == 1:
            low_l_d = f"\n- #1 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}"
        elif low_l == 2:
            low_l_d = f"\n- #1 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}\n" \
                        f"- #2 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}"
        elif low_l == 3:
            low_l_d = f"\n- #1 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}\n" \
                        f"- #2 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}\n" \
                        f"- #3 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}"
        elif low_l == 4:
            low_l_d = f"\n- #1 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}\n" \
                        f"- #2 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}\n" \
                        f"- #3 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}\n" \
                        f"- #4 специализация: {random.choice(self.bot.quest['place_special'])}\n     особенность: {random.choice(self.bot.quest['low_l_fea'])}"
        else:
            low_l_d = f"отсутствуют"

        if (n == '0'):
            await ctx.send("_Введите название осколка._")
            return
        elif (n not in (self.bot.quest['place'])):
            await ctx.send("_Такого осколка не существует._")
            return
        else:
            response = f"```ОСКОЛОК #{n}\n\nКорпорация: {place_c}\nАрхонт: {race_place} ({random.choice(self.npc['class'])}" \
                        f" {random.choice(self.npc['podclass'])})\n" \
                        f"Специализация осколка: {random.choice(self.bot.quest['place_special'])}\n" \
                        f"Присутствие других корпораций: {dop_corp}\nПрирода осколка: {random.choice(self.bot.quest['place_origin'])}\n" \
                        f"Особенность: {random.choice(self.bot.quest['place_fea'])}, {random.choice(self.bot.quest['place_fea'])}\nНижние уровни: {low_l_d}```"


            await ctx.send(response)

    # ------- новости

    @commands.command(name='новостиосколка')
    async def news_isl(self, ctx, m='0', n=1):

        if (n < 1) or (n > 5):
            await ctx.send("_Запрос не может превышать 5 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            if (m == '0'):
                await ctx.send("_Введите название осколка._")
                return
            elif (m not in (self.bot.quest['place'])):
                await ctx.send("_Такого осколка не существует._")
                return
            else:
                rnd_news = random.randint(1, 10)
                if rnd_news > 8:
                    response = f"""```ml\nNEWS На осколке #{m} {random.choice(self.bot.data['news_isl'])}```"""
                else:
                    response = f"""```ml\nNEWS На осколке #{m} {random.choice(self.bot.data['news_isl_corp'])} {random.choice(self.bot.data['corporation'])}.```"""
                await ctx.send(response)

    @commands.command(name='новости')
    async def news_gen(self, ctx, n=1):
        if (n < 1) or (n > 5):
            await ctx.send("_Запрос не может превышать 5 сообщений за раз ради вашей безопасности._")
            return
        await ctx.message.delete()

        for i in range(n):
            rnd_news = random.randint(1, 10)
            if rnd_news > 8:
                response = f"""```ml\nNEWS На осколке #{random.choice(self.bot.quest['place'])} {random.choice(self.bot.data['news_isl'])}```"""
            elif rnd_news < 2:
                corp_corp_fest = random.choice(self.bot.data['corporation'])
                ft_time = random.choice(['Сегодня', 'Завтра', 'Через 2 дня', 'Через 3 дня', 'Через 4 дня', 'Через 5 дней'])
                adress = random.randint(1000000000, 9999999999)
                response = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n{ft_time.capitalize()} на осколке {random.choice(self.bot.quest['place'])} """ \
                            f"""{random.choice(self.bot.ad['fest_action'])} {random.choice(self.bot.ad['fest_type_corp'])} """ \
                            f"""▶ {(corp_corp_fest).upper()} ◀. {random.choice(self.bot.ad['fest_what_do']).capitalize()}! """ \
                            f"""Узнать больше информации: {adress}```"""
            else:
                response = f"""```ml\nNEWS На осколке #{random.choice(self.bot.quest['place'])} {random.choice(self.bot.data['news_isl_corp'])} {random.choice(self.bot.data['corporation'])}.```"""
            await ctx.send(response)


    # @commands.command(name='тест')
    # async def test(ctx, user='0', *, args):
    #     users_list = (users['users_list'])

    #     message = f"""```ml\n'РМ' {(args)}```"""
    #     await ctx.message.delete()

    #     pattern = re.compile("\d{6}-\d{6}-\d{6}")

    #     if user in ("тест"):
    #         channel = client.get_channel(811399149303234615)
    #     elif user in ("тестовый"):
    #         channel = client.get_channel(811399149303234615)
    #     else:
    #         if pattern.match(user):
    #             channel = client.get_channel(811399149303234615)
    #             mess_us = f"_** **\nПолучатель: {user} (неизвестный номер)\nСтатус: отправлено_{message}"
    #             await ctx.send(mess_us)
    #             await channel.send(message)
    #         else:
    #             mess_us = f"_** **\nПолучатель: не определен (ошибка номера)\nСтатус: ОШИБКА_{message}"
    #             await ctx.send(mess_us)
    #         return

    #     mess_us = f"_** **\nПолучатель: {user}\nСтатус: отправлено_{message}"
    #     await ctx.send(mess_us)
    #     await channel.send(message)

    #------- общие дефы

    def ad_corp_empl_nox(self):
        ad_nox = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Нокс ◀\n\nМы создали этот город, и мы можем дать тем, кто помогает нам строить и защищать его:\n""" \
                    f"""✔ Приоритет обслуживания Орденам Пантеона Нокс\n""" \
                    f"""✔ Повышенные лимиты всех подписок и доступ к особым подпискам закрытым для публики\n""" \
                    f"""✔ Работу в самой престижной и уважаемой корпорации, что творит историю\n""" \
                    f"""✔ Шедрые премии, зарплата, страховка, гарантии - чтобы вам никогда не пришлось боятся за свое или своих близких будушее\n\n""" \
                    f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["nox_vac"])}\n- {random.choice(self.bot.data["nox_vac"])}\n- {random.choice(self.bot.data["nox_vac"])}\n\n""" \
                    f"""Станьте частью тех, на чьих плечах стоит этот город!\nПодробности: NoxS-{random.randint(1000, 9999)}```"""
        return ad_nox

    def ad_corp_empl_hh(self):
        ad_hh = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Холдинг Хорнс ◀\n\nС нами вы:\n""" \
                        f"""✔ Работаете на уважаемой, статусной и солидной работе\n""" \
                        f"""✔ Получаете приоритет в пользовании услугами корпорации\n""" \
                        f"""✔ Имеете шанс проявить свои дизайнерские таланты\n""" \
                        f"""✔ Работаете с премиальными технологиями в комфортной и удобной среде\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["hh_vac"])}\n- {random.choice(self.bot.data["hh_vac"])}\n- {random.choice(self.bot.data["hh_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: HornS-{random.randint(1000, 9999)}```"""
        return ad_hh

    def ad_corp_empl_aet(self):
        ad_aet = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Аэтерн ◀\n\nС нами вы:\n""" \
                        f"""✔ Получаете приоритет медицинского обслуживания в предприятиях корпорации\n""" \
                        f"""✔ Получаете медицинскую страховку пропорционально вашему статусу в корпорации\n""" \
                        f"""✔ Работаете на уважаемой работе в корпорации которая спасает жизни\n""" \
                        f"""✔ Работаете на самой безопасной работе, в корпорации где наименьший процент рабочих травм\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["aet_vac"])}\n- {random.choice(self.bot.data["aet_vac"])}\n- {random.choice(self.bot.data["aet_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: Aethern-{random.randint(1000, 9999)}```"""

        return ad_aet

    def ad_corp_empl_oir(self):
        ad_oir = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Дом Ойр ◀\n\nС нами вы:\n""" \
                        f"""✔ Будете знать, что то, что вы создаете - простоит века\n""" \
                        f"""✔ Будете уверенны в завтра с надежными контрактами и графиками выплат\n""" \
                        f"""✔ Будете застрахованы на случай производственных травм\n""" \
                        f"""✔ Получите шанс работать даже имея минимальное образование\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["oir_vac"])}\n- {random.choice(self.bot.data["oir_vac"])}\n- {random.choice(self.bot.data["oir_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: OirS-{random.randint(1000, 9999)}```"""
        return ad_oir

    def ad_corp_empl_tenta(self):
        ad_tenta = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Тентакорп ◀\n\nПредлагает:\n""" \
                        f"""✔ Работу с отключенным разумом, не работайте ни дня в своей жизни\n""" \
                        f"""✔ Возможность заработать на продаже своих знаний, заработок без единого движения\n""" \
                        f"""✔ Мудрое управление и подобранный под вас коллектив, ведь мы читаем ваши мысли\n""" \
                        f"""✔ Доступ к базам данных для загрузки навыков для повышения квалификации\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["tenta_vac"])}\n- {random.choice(self.bot.data["tenta_vac"])}\n- {random.choice(self.bot.data["tenta_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: ТentaS-{random.randint(1000, 9999)}```"""
        return ad_tenta

    def ad_corp_empl_magna(self):
        ad_magna = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Магнакорп ◀\n\nПредлагает:\n""" \
                        f"""✔ Работу с передовыми технологиями Магнавеб, за которыми - будущее\n""" \
                        f"""✔ Опции удаленной работы из дома через Магнавеб\n""" \
                        f"""✔ Бонусы и повышенные лимиты пользования Магнавеб для работников\n""" \
                        f"""✔ Неограниченный доступ к Когна, Ковен и Стрим для работников\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["magna_vac"])}\n- {random.choice(self.bot.data["magna_vac"])}\n- {random.choice(self.bot.data["magna_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: MagnaS-{random.randint(1000, 9999)}```"""
        return ad_magna

    def ad_corp_empl_vis(self):
        ad_vis = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Вистара ◀\n\nМы гарантируем вам:\n""" \
                        f"""✔ Заботу, дружный коллектив, мудрое покровительство без необходимости волноваться о будущем\n""" \
                        f"""✔ Предоставление еды, воды и всего критически необходимого - корпорацией\n""" \
                        f"""✔ Трудоустройство с обучением, адаптацией тела и имплантацией за счет корпорации\n""" \
                        f"""✔ Эмпатическое стимулирование что сделает ваши дни светлее, а работу - желаннее\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["vis_vac"])}\n- {random.choice(self.bot.data["vis_vac"])}\n- {random.choice(self.bot.data["vis_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: VistaraS-{random.randint(1000, 9999)}```"""
        return ad_vis

    def ad_corp_empl_prima(self):
        ad_prima = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Прима ◀\n\nМы гарантируем вам:\n""" \
                        f"""✔ Обеспечение трудоустройства любому кто пожелает стать частью Улья\n""" \
                        f"""✔ Мудрое управление, опыт ассимиляции всех рас длинной в тысячелетия\n""" \
                        f"""✔ Безопасность и порядок на работе и в вашем Улье\n""" \
                        f"""✔ Обеспечение собственного жилья любому кто пожелает стать частью Улья\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["prima_vac"])}\n- {random.choice(self.bot.data["prima_vac"])}\n- {random.choice(self.bot.data["prima_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: PrimaS-{random.randint(1000, 9999)}```"""
        return ad_prima

    def ad_corp_empl_ailself(self):
        ad_ail = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Королевство Айль ◀\n\nМы гарантируем вам:\n""" \
                        f"""✔ Банковский счет и виртуальный кошелек с выгодными условиями для каждого работника\n""" \
                        f"""✔ Комфортную рабочую среду\n""" \
                        f"""✔ Возможность получения премий круизами на наших лучших лайнерах\n""" \
                        f"""✔ Приоритет в обслуживании для работников коорпорации\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["ail_vac"])}\n- {random.choice(self.bot.data["ail_vac"])}\n- {random.choice(self.bot.data["ail_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: IleS-{random.randint(1000, 9999)}```"""
        return ad_ail

    def ad_corp_empl_kain(self):
        ad_kain = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Пантеон Кайн ◀\n\nМы предлагаем вам:\n""" \
                        f"""✔ Шанс работы в мультикультурном и всерассовом коллективе без дискриминации\n""" \
                        f"""✔ Шанс работы с самыми передовыми технологиями что соединяют усилия всех рас\n""" \
                        f"""✔ Шанс трудоустройства и получения жилья в наших Замках и Поместьях\n""" \
                        f"""✔ Шанс прохождения обучения непревзойденного качества и последущего становления ангелом или даже аватаром архонта\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["kain_vac"])}\n- {random.choice(self.bot.data["kain_vac"])}\n- {random.choice(self.bot.data["kain_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: KineS-{random.randint(1000, 9999)}```"""
        return ad_kain

    def ad_corp_empl_rev(self):
        ad_rev = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Церковь Прозрения ◀\n\nМы предлагаем вам:\n""" \
                        f"""✔ Прозрение, стабильность, надежду, социальную и психологическую помощь от тех, кто знает вашу душу лучше вас\n""" \
                        f"""✔ Правильно подобранное трудоустройство и коллектив, ведь мы знаем чего вы желаете\n""" \
                        f"""✔ Всестороннюю помощь в устройстве жизни для всех работников корпорации\n""" \
                        f"""✔ Возможность помогать другим и вести их к надежде и свету\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["rev_vac"])}\n- {random.choice(self.bot.data["rev_vac"])}\n- {random.choice(self.bot.data["rev_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: RevelationS-{random.randint(1000, 9999)}```"""
        return ad_rev

    def ad_corp_empl_sin(self):
        chanse_sin = random.randint(1, 3)
        if chanse_sin == 1:
            ad_sin = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nПредлагает:\n""" \
                        f"""✔ Работу от которой вы будете получать удовольствие\n""" \
                        f"""✔ Бонусы в заведениях корпорации для сотрудников\n""" \
                        f"""✔ Интересные и креативные проекты\n""" \
                        f"""✔ Возможность творческой самореализаци\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
        elif chanse_sin == 2:
            ad_sin = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nГарантирует:\n""" \
                        f"""✔ Адаптивный график работы\n""" \
                        f"""✔ Регулярные корпоративы и мероприятия для работников\n""" \
                        f"""✔ Дружный коллектив\n""" \
                        f"""✔ Работу без излишней бюрократии\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
        elif chanse_sin == 3:
            ad_sin = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Син Корп ◀\n\nС нами вы:\n""" \
                        f"""✔ Никогда не заскучаете\n""" \
                        f"""✔ Найдете коллектив со схожими интересами\n""" \
                        f"""✔ Будете говорить "жеще папочка" сердитому начальнику\n""" \
                        f"""✔ Будете работать в корпорации которая честно смотрит на себя и на вас\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n- {random.choice(self.bot.data["sin_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: SinS-{random.randint(1000, 9999)}```"""
        return ad_sin

    def ad_corp_empl_morde(self):
        ad_morde = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Мордекорп ◀\n\nПредлагает:\n""" \
                        f"""✔ Трудоустройство без образования\n""" \
                        f"""✔ Имплантацию и подготовку за счет корпорации\n""" \
                        f"""✔ Стабильные и долгие контракты\n""" \
                        f"""✔ Страховку с выплатами семье и близким в случае смерти\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["mord_vac"])}\n- {random.choice(self.bot.data["mord_vac"])}\n- {random.choice(self.bot.data["mord_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: MordeS-{random.randint(1000, 9999)}```"""
        return ad_morde

    def ad_corp_empl_all(self):
        ad_all = f"""```ml\n◈ 'ОБЪЯВЛЕНИЕ КОРПОРАЦИИ'\n▶ Все и Вся Инк ◀\n\nПредлагает:\n""" \
                        f"""✔ Работу поблизости от дома\n""" \
                        f"""✔ Бонусы в магазинах корпорации для сотрудников\n""" \
                        f"""✔ Премии продукцией компании которую вы выберете\n""" \
                        f"""✔ Трудоустройство с минимальным образованием\n\n""" \
                        f"""Свободные вакансии, которые могут вам подойди:\n- {random.choice(self.bot.data["ae_vac"])}\n- {random.choice(self.bot.data["ae_vac"])}\n- {random.choice(self.bot.data["ae_vac"])}\n\n""" \
                        f"""Запишитесь сегодня!\nПодробности: AllS-{random.randint(1000, 9999)}```"""
        return ad_all
    

async def setup(bot: ArchLight):
    await bot.add_cog(Commands(bot))