from dto import all_dtos

definitions = dict([(dto.__name__, dto.swagger()) for dto in all_dtos])
