import random
from enums import Loot
from discord.ext import commands
from client import ArchLight
from static import StaticMethods
from discord import NotFound


class LootGenerator(commands.Cog):
    def __init__(self, bot: ArchLight):
        self.bot = bot
        super().__init__()

    @commands.command(name="лут")
    async def random_trophy(self, ctx, n=1):
        for _ in range(n):
            trophy = random.choice(self.bot.data['trophy'])
            await self.generate_trophy(ctx, 1, trophy)

    async def generate_trophy(self, ctx, n, trophy):
        try:
            await ctx.message.delete()
        except NotFound:
            pass
        if not (1 <= n <= 5):
            await ctx.send("В запрос принимаются значения от 1 до 5")
            return
        for _ in range(n):
            response = ["```Трофей: "]
            response.append(trophy + "\n")
            match trophy:
                case Loot.WEAPON.value:
                    response.append(
                        f"Класс: {random.choice(self.bot.data['class_gen'])}\nВид: {random.choice(self.bot.data['kind_weapon'])}"
                    )
                case Loot.ARMOR.value:
                    response.append(
                        f"Класс: {random.choice(self.bot.data['class_gen'])}\nВид: {random.choice(self.bot.data['kind_main_armor'])}"
                    )
                case Loot.EXTRA_ARMOR.value:
                    response.append(
                        f"Класс: {random.choice(self.bot.data['class_gen'])}\nВид: {random.choice(self.bot.data['kind_extra_armor'])}"
                    )
                case Loot.ACCESSORY.value:
                    response.append(
                        f"Вид аксессуара: {StaticMethods.access(self.bot.data)}"
                    )
                case Loot.DEVICE.value:
                    response.append(
                        f"Вид устройства: {random.choice(self.bot.data['kind_device'])}\nЗащита: {random.choice(self.bot.data['protection'])}"
                    )
                case Loot.GENERIC.value:
                    response.append(f"Вид предмета: {StaticMethods.item(self.bot.data)}")
                case Loot.RARE.value:
                    response.append(f"Вид предмета: {StaticMethods.item(self.bot.data)}")
                case Loot.MONEY.value:
                    response.append(f"Носитель: {random.choice(self.bot.data['carrier'])}")
                case _:
                    pass
            response.append(f"\nПроизводство: {StaticMethods.mfr(self.bot.data).title()}\n")
            if trophy == "деньги":
                response.append(f"Значение: {StaticMethods.m_amount(self.bot.data)}")
            if trophy == "уникальное":
                response.pop()
            response.append("```")
            await ctx.send("".join(response))

    @commands.command(name="оружие")
    async def random_weapon(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.WEAPON.value)

    @commands.command(name="броня")
    async def random_main_armor(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.ARMOR.value)

    @commands.command(name="допброня")
    async def random_extra_armor(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.EXTRA_ARMOR.value)

    @commands.command(name="снаряжение")
    async def random_auxiliary_equipment(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.EQUIPMENT.value)

    @commands.command(name="расходник")
    async def random_consumable(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.CONSUMABLE.value)

    @commands.command(name="аксессуар")
    async def random_accessory(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.ACCESSORY.value)

    @commands.command(name="устройство")
    async def random_device(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.DEVICE.value)

    @commands.command(name="простой")
    async def random_simple_item(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.GENERIC.value)

    @commands.command(name="ценный")
    async def random_valuable_item(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.RARE.value)

    @commands.command(name="деньги")
    async def random_money(self, ctx, n=1):
        return await self.generate_trophy(ctx, n, Loot.MONEY.value)

    @commands.command(name="значение")
    async def money(self, ctx, n=1):
        if not (1 <= n <= 5):
            await ctx.send("В запрос принимаются значения от 1 до 5")
            return
        await ctx.message.delete()
        for i in range(n):
            response = f"```Значение: {StaticMethods.amount()}```"
            await ctx.send(response)


async def setup(bot: ArchLight):
    await bot.add_cog(LootGenerator(bot))
