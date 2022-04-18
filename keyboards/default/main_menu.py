from .consts import DefaultConstructor


class MainMenu(DefaultConstructor):
    @staticmethod
    def main_menu():
        schema = [1]
        actions = ['​']
        caption = "Слава Украине!"
        return MainMenu._create_kb(actions, schema, input_field_placeholder=caption)
