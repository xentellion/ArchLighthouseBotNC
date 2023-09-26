import os
import json
import yaml
from discord.ext import commands


class ConfigFile:
    def __init__(self, prefix: str = "", token: str = ""):
        self.prefix = prefix
        self.token = token


class EmptyConfig(Exception):
    def __init__(self, config_path: str):
        self.message = f"Please, set up variables in {config_path}"
        super().__init__(self.message)


class ArchLight(commands.Bot):
    def __init__(self, intents, activity, data_folder, config):
        self.data_folder = data_folder
        os.makedirs(self.data_folder, exist_ok=True)
        self.config_path = self.data_folder + config
        # Получить или создать файл с конфигом
        with open(self.config_path, "a+", encoding="utf8") as file:
            file.seek(0)
            try:
                data = json.load(file)
                self.config = ConfigFile(**data)
                if self.config.token == "":
                    raise EmptyConfig(self.config_path)
            except json.JSONDecodeError:
                json.dump(ConfigFile().__dict__, file, sort_keys=False, indent=4)
                raise EmptyConfig(self.config_path)
        # Наследование от commands.Bot
        super().__init__(
            intents=intents, activity=activity, command_prefix=self.config.prefix
        )
        # открываем и сохраняем данные. @TODO - обработчик исключений
        with open(f"{self.data_folder}data.yaml", "r", encoding="utf8") as file:
            self.data = yaml.safe_load(file)

        with open(f"{self.data_folder}npc.yaml", "r", encoding="utf8") as file:
            self.npc = yaml.safe_load(file)

        with open(f"{self.data_folder}quest.yaml", "r", encoding="utf8") as file:
            self.quest = yaml.safe_load(file)

        with open(f"{self.data_folder}ad.yaml", "r", encoding="utf8") as file:
            self.ad = yaml.safe_load(file)

        with open(f"{self.data_folder}users.yaml", "r", encoding="utf8") as file:
            self.dis_users = yaml.safe_load(file)

        with open(f"{self.data_folder}candy.yaml", "r", encoding="utf8") as file:
            self.candy = yaml.safe_load(file)

    async def on_command_error(self, ctx, error):
        print(error)
