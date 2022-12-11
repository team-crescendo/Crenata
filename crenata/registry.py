from crenata.abc.command import AbstractCrenataCommand
from crenata.discord import CrenataInteraction


class Registry:
    registered: dict[type[AbstractCrenataCommand], type[AbstractCrenataCommand]] = {}

    @classmethod
    def override(cls, wrapped_class: type[AbstractCrenataCommand]):
        for command_cls in cls.registered:
            if issubclass(command_cls, wrapped_class):
                cls.registered[command_cls] = wrapped_class
            else:
                raise TypeError("Can't found subclass")
        return wrapped_class

    @classmethod
    def register(
        cls,
        wrapped_class: type[AbstractCrenataCommand],
    ):
        cls.registered[wrapped_class] = wrapped_class
        return wrapped_class

    @classmethod
    def get_command(
        cls,
        registered_class: type[AbstractCrenataCommand],
        interaction: CrenataInteraction,
    ):
        return cls.registered[registered_class](interaction)
