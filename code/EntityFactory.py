from code.Background import Background
from code.Constants import IMAGE_LEVELS, WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position: tuple = (0, 0)):

        if entity_name and f'lv1_bg' in entity_name:
            bg_list = []
            for i in range(IMAGE_LEVELS['lv1_bg']):
                bg_list.append(Background(f'lv1_bg{i + 1}', (0, 0)))
                bg_list.append(Background(f'lv1_bg{i + 1}', (WIN_WIDTH, 0)))

            return bg_list
