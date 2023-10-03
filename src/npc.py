import random
from discord.ext import commands
from client import ArchLight
from scipy.stats import truncnorm
from enums import Races


class NpcGenerator(commands.Cog):
    def __init__(self, bot: ArchLight):
        self.bot = bot
        super().__init__()

    def get_truncated_normal(self, mean=0, sd=1, low=0, upp=10):
        return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

    @commands.command(name="нпс")
    async def random_npc(self, ctx, n=1):
        if (n < 1) or (n > 5):
            await ctx.send("В запрос принимаются значения от 1 до 5")
            return
        await ctx.message.delete()
        for i in range(n):
            race_b = random.choice(self.bot.npc["race"])
            if race_b == Races.HUMAN.value:
                pass
            else:
                race_b = f"{race_b} ({random.choice(self.bot.npc[Races(race_b).name.lower()])})"

            y = self.get_truncated_normal(37, 20, 12, 140)
            age = int(y.rvs(1))

            match random.randint(1, 5):
                case 1:
                    health = f"идеальное здоровье"
                case 2:
                    health = f'{random.choice(self.bot.npc["health_time"])}'
                case 3:
                    health = f'{random.choice(self.bot.npc["health_pec"])}'
                case 4:
                    health = f'{random.choice(self.bot.npc["health"])}'
                case 5:
                    health = f'{random.choice(self.bot.npc["health_hard"])} с прогрессией {random.randint(1, 9) * 10}%'
            biol = f"{race_b}, {age}, {health}"

            val = random.randint(0, 3)
            phob = "нет фобии" if val != 0 else random.choice(self.bot.npc["phobia"])

            val2 = random.randint(0, 3)
            cp = (
                f"нет связей"
                if val2 != 0
                else f'{random.choice(self.bot.npc["interaction"])} {random.choice(self.bot.data["corporation"])}'
            )

            response = f"""```
Биология: {biol}
Профессия: {random.choice(self.bot.npc['cbp_proff'])}, {random.choice(self.bot.npc['proff'])}
Класс: {random.choice(self.bot.npc['class'])}, {random.choice(self.bot.npc['podclass'])}
Характер: {random.choice(self.bot.npc['character'])}, {phob}
Снаряжение:
- оружие: {random.choice(self.bot.data['class_gen'])}, {random.choice(self.bot.data['kind_weapon'])}
- броня: {random.choice(self.bot.data['class_gen'])}, {random.choice(self.bot.data['kind_main_armor'])}
- с собой: {random.choice(self.bot.data['trophy'])}
Особенность: {random.choice(self.bot.npc['fea'])}
Связь с корпорацией: {cp}
Трофеев в карманах: {random.randint(1, 3)}
```"""
            await ctx.send(response)


async def setup(bot: ArchLight):
    await bot.add_cog(NpcGenerator(bot))
