# Задание 1. Работу выполнил Владислав Юдин.
import requests
import subprocess

# Функция для скачивания файла по ссылке и сохранения в указанной директории
def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

# Функция для добавления значений из .reg файла в реестр Windows
def add_registry_values(reg_file):
    subprocess.call(['reg', 'import', reg_file])

# Функция для запуска Steam или игры
def launch_game():
    # Выбираем запуск Steam или игры
    subprocess.Popen(['C:\Program Files (x86)\Steam\Steam.exe'])
    #subprocess.Popen(['D:\SteamLibrary\steamapps\common\Goose Goose Duck\Goose Goose Duck.exe'])

# Основная функция скрипта
def main():

    reg_file_path = "D:\SteamLibrary\steamapps\common\Goose Goose Duck\settings.reg" # путь к файлу .reg

    reg_file_url = 'https://drive.usercontent.google.com/download?id=1IGENwFzLm8bBEboISadYSNEdxbnjz1fH&export=download&authuser=0&confirm=t&uuid=03009bf6-3d92-44ea-baeb-22bcd749f6a5&at=APZUnTVq6IELw5D3XWGl0CSuO48e%3A1713441279148' # адрес .reg файла

    download_file(reg_file_url, reg_file_path) # скачивание файла .reg

    add_registry_values(reg_file_path) # добавление значений из .reg файла в реестр Windows

    launch_game() # запуск Steam или игры. Это зависит от выбора в функции

if __name__ == "__main__": # запуск скрипта
    main()