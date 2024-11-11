import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.RED + 'Красный текст')
print(Back.GREEN + 'Зеленый фон')
print(Style.BRIGHT + 'Яркий текст')
print(Style.RESET_ALL + 'Сброс всех стилей')
