# CSGO CLEANER v0.1 11/03/2022
# credits: stanico#1206
# tg: @Stanico
# github.com/stanico/csgocleaner/

import os
import shutil
import sys
from distutils.dir_util import copy_tree
import time

def remove_file(path, file):
    if os.path.exists(os.path.join(csgo_path + path + file)):
        if os.path.exists(os.path.join(main_path + path)):
            pass
        else:
            os.makedirs(main_path + path)
        shutil.copy(os.path.join(csgo_path + path + file),os.path.join(main_path + path + file))
        os.remove(os.path.join(csgo_path + path + file))
    else:
        print('[ERROR] FILE NOT EXISTS')
        print(file +" "+ path)


def restore_file(path, file):
    if os.path.exists(os.path.join(main_path + path + file)):
        if os.path.exists(os.path.join(csgo_path + path)):
            pass
        else:
            os.makedirs(os.path.join(csgo_path + path))
        shutil.copy(os.path.join(main_path + path + file), os.path.join(csgo_path + path + file))
        os.remove(os.path.join(main_path + path + file))
    else:
        print('[ERROR] FILE NOT EXISTS')
        print(file +" "+ path)


def remove_tree(path):
    if os.path.exists(os.path.join(csgo_path + path)):
        if os.path.exists(os.path.join(main_path + path)):
            pass
        else:
            os.makedirs(os.path.join(main_path + path))
        copy_tree(os.path.join(csgo_path + path), os.path.join(main_path + path))
        shutil.rmtree(os.path.join(csgo_path + path))
    else:
        print('TREE NOT FOUND')

def restore_tree(path):
    if os.path.exists(os.path.join(main_path + path)):
        if os.path.exists(os.path.join(csgo_path + path)):
            pass
        else:
            os.makedirs(os.path.join(csgo_path + path))
        copy_tree(os.path.join(main_path + path), os.path.join(csgo_path + path))
        shutil.rmtree(os.path.join(main_path + path))
    else:
        print('[ERROR] FILE NOT EXISTS')


def remove_byext(ext, path):
    list = os.listdir(os.path.join(csgo_path + path))
    if os.path.exists(os.path.join(main_path + path)):
        pass
    else:
        os.makedirs(os.path.join(main_path + path))
    for item in list:
        if item.endswith(ext):
            shutil.copy(os.path.join( csgo_path + path, item ), os.path.join(main_path + path))
            os.remove(os.path.join( csgo_path + path, item ))

    
def clean():
    global main_path
    main_path = main_path + "\\restorepoint"
    #bin
    remove_tree("\\bin\\locales")
    remove_tree("\\bin\\map_publish")
    remove_tree("\\bin\\prefabs")
    remove_tree("\\bin\\v8_winxp")
    remove_file("\\bin\\", "convertdmx.lua")
    remove_file("\\bin\\", "libfbxsdk.dll")
    remove_file("\\bin\\", "maplist_csgo.txt")
    remove_file("\\bin\\", "mssdolby.flt")
    remove_file("\\bin\\", "mssdsp.flt")
    remove_file("\\bin\\", "msseax.flt")
    remove_file("\\bin\\", "msssrs.flt")
    remove_file("\\bin\\", "telemetry32c.dll")
    remove_file("\\bin\\", "trxtemplate.xml")
    remove_file("\\bin\\", "vidcfg.bin")
    #csgo
    remove_tree("\\csgo\\expressions")
    remove_tree("\\csgo\\materials")
    remove_tree("\\csgo\\models")
    remove_tree("\\csgo\\scenes")
    remove_tree("\\csgo\\resource")
    restore_tree("\\csgo\\resource\\overviews")
    restore_file("\\csgo\\resource\\ui\\", "buymenuconfig.txt")
    restore_file("\\csgo\\resource\\", "valve_english.txt")
    restore_file("\\csgo\\resource\\", "valve_russian.txt")
    restore_file("\\csgo\\resource\\", "mp3player_english.txt")
    restore_file("\\csgo\\resource\\", "boxrocket_english.txt")
    restore_file("\\csgo\\resource\\", "dmecontrols_english.txt")
    restore_file("\\csgo\\resource\\", "csgo_english.txt")
    restore_file("\\csgo\\resource\\", "gameui_russian.txt")
    restore_file("\\csgo\\resource\\", "chat_russian.txt")
    restore_file("\\csgo\\resource\\", "sfui_russian.txt")
    restore_file("\\csgo\\resource\\", "csgo_russian.txt")
    if stickers == "1":
        pass
    else:
        restore_file("\\csgo\\resource\\", "vmtcache.txt")
    remove_tree("\\csgo\\scripts")
    restore_file("\\csgo\\scripts\\", "instructor_textures.txt")
    restore_file("\\csgo\\scripts\\", "inventory_structure.txt")
    restore_file("\\csgo\\scripts\\items\\", "items_game.txt")
    remove_file("\\csgo\\", "bspconvar_whitelist.txt")
    remove_file("\\csgo\\", "gamemodes_server.txt.example")
    remove_file("\\csgo\\", "demo_polish_settings.cfg")
    remove_file("\\csgo\\", "demoheader.tmp")
    remove_file("\\csgo\\", "gamerulescvars.txt.example")
    remove_file("\\csgo\\", "leaderboardsconfig.txt")
    remove_file("\\csgo\\", "lights.rad")
    remove_file("\\csgo\\", "loadouts.txt")
    remove_file("\\csgo\\", "maplist.txt")
    remove_file("\\csgo\\", "medalsconfig.txt")
    remove_file("\\csgo\\", "motd.txt")
    remove_file("\\csgo\\", "navplace.db")
    remove_file("\\csgo\\", "pure_server_whitelist.txt")
    remove_file("\\csgo\\", "radial_quickinventory.txt")
    remove_file("\\csgo\\", "radial_radio.txt")
    remove_file("\\csgo\\", "scene.cache")
    remove_file("\\csgo\\", "serverconfig.vdf")
    remove_file("\\csgo\\", "splitscreen_config.txt")
    remove_file("\\csgo\\", "unusedcontent.cfg")
    remove_file("\\csgo\\", "whitelist.cfg")
    remove_file("\\csgo\\", "whitelist_beta.cfg")
    remove_byext(".txt", "\\csgo\\maps")
    remove_byext(".nav", "\\csgo\\maps")
    remove_byext(".jpg", "\\csgo\\maps")
    if videos == "1":
        remove_tree("\\csgo\\panorama\\fonts")
    if font == "1":
        remove_tree("\\csgo\\panorama\\videos")

    #platform
    if servers == "2":
        remove_tree("\\platform\\materials")
        remove_tree("\\platform\\resource")
        remove_tree("\\platform\\scripts")
        remove_tree("\\platform\\steam")
        remove_tree("\\platform\\vgui")
    if bots == "1":
        remove_file("\\csgo\\", "botchatter.db")
        remove_file("\\csgo\\", "botprofile.db")
        remove_file("\\csgo\\", "botprofilecoop.db")
def restore():
    root_src_dir = main_path + '\\restorepoint'
    root_dst_dir = csgo_path

    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                if os.path.samefile(src_file, dst_file):
                    continue
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)
    shutil.rmtree(main_path + '\\restorepoint')


def intro():
    print('   ___________ __________     ________    _________    _   ____________ ')
    print('  / ____/ ___// ____/ __ \   / ____/ /   / ____/   |  / | / / ____/ __ \ ')
    print(' / /    \__ \/ / __/ / / /  / /   / /   / __/ / /| | /  |/ / __/ / /_/ / ')
    print('/ /___ ___/ / /_/ / /_/ /  / /___/ /___/ /___/ ___ |/ /|  / /___/ _, _/ ')
    print('\____//____/\____/\____/   \____/_____/_____/_/  |_/_/ |_/v0.1_/_/ |_| ') 
    print('Credits: stanico#1206')
    print('')


def setup():
    global bots
    global stickers
    global videos
    global font
    global servers
    clear = lambda: os.system('cls')
    clear()
    intro()
    print('Отключить ботов? (На картах по типу AimBotz они будут!) [1/5]')
    print('[1] Да')
    print('[2] Нет')
    bots = input('')
    clear()
    intro()
    print('Отключить стикеры? (Их не будет видно на оружиях) [2/5]')
    print('[1] Да')
    print('[2] Нет')
    stickers = input('')
    clear()
    intro()
    print('Отключить фон в меню? (В параметры запуска нужно будет вводить -novid) [3/5]')
    print('[1] Да')
    print('[2] Нет')
    videos = input('')
    clear()
    intro()
    print('Отключить шрифт? (Вместо обычного шрифта, будет системный) [4/5]')
    print('[1] Да')
    print('[2] Нет')
    font = input('')
    clear()
    intro()
    print('Вы играете на серверах сообщества? [5/5]')
    print('[1] Да')
    print('[2] Нет')
    servers = input('')
    clear()
    intro()
    print('Настройка завершена успешно!')
    time.sleep(0.5)
    clear()
    intro()
    main()


def main():
    global csgo_path
    global main_path
    clear()
    intro()
    if not os.path.exists(main_path):
        print('*** first run')
        print('Введите путь к папке CS:GO')
        print('Пример: C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive')
        csgo_path = input()
        if os.path.exists(csgo_path + "\csgo.exe"):
            os.makedirs(main_path)
            with open(main_path + '\path.txt', 'w') as file:
                file.write(csgo_path)
                file.close()
            clear()
            intro()
            print("Примечание: Перед оптимизацией желательно настроить")
            print('[1] Очистка')
            print('[2] Настройка')
            a = input()
            if a == "1":
                clear()
                intro()
                if bots == "1" or stickers == "1" or videos == "1" or font == "1" or servers == "2":
                    print('Изменения после очистки: ')
                else:
                    pass
                if bots == "1":
                    print(' - Не будут работать боты в локальной игре (На картах по типу AimBotz будут)')
                if stickers == "1":
                    print(' - Не будут видны стикеры на оружиях')
                if videos == "1":
                    print(' - Не будет заднего фона в меню (Будет просто черное)')
                if font == "1":
                    print(' - Будет системный шрифт, вместо обычного')
                if servers == "2":
                    print(' - Не будут работать сервера сообщества')
                print('')
                print('Начить оптимизацию?')
                print('[1] Да')
                print('[2] Нет')
                b = input('')
                if b == '1':
                    clear()
                    intro()
                    print('Оптимизация может занять некоторое времья... зависит от ПК')
                    clean()
                    clear()
                    intro()
                    print('Успешно!')
                    print('Заходите в игру, и проверяйте изменения.')
                    print('Если стало хуже вы можете восстановить всё по умолчанию после повторного запуска программы!')
                    time.sleep(5)
                else:
                    main()
            pass
            if a == "2":
                setup()
        else:
            print('Не удалось найти csgo.exe!!!')
            input('')
            exit()
    else:
        with open(main_path + '\path.txt', 'r') as file:
            csgo_path = file.read()
            file.close()
        print('[1] Очистка')
        print('[2] Настройка')
        if os.path.exists(main_path + "\\restorepoint"):
            print('[3] Возврат')
            print('[4] Удалить точку восстановления')
        else:
            print('Точка восстановления не найдена!')
        a = input()
        if a == "1":
            clear()
            intro()
            if bots == "1" or stickers == "1" or videos == "1" or font == "1" or servers == "2":
                print('Изменения после очистки: ')
            if bots == "1":
                print(' - Не будут работать боты в локальной игре (На картах по типу AimBotz будут)')
            if stickers == "1":
                print(' - Не будут видны стикеры на оружиях')
            if videos == "1":
                print(' - Не будет заднего фона в меню (Будет просто черное)')
            if font == "1":
                print(' - Будет системный шрифт, вместо обычного')
            if servers == "2":
                print(' - Не будут работать сервера сообщества')
            print('')
            print('Начить оптимизацию?')
            print('[1] Да')
            print('[2] Нет')
            b = input('')
            if b == '1':
                clear()
                intro()
                print('Оптимизация может занять некоторое времья... зависит от ПК')
                clean()
                clear()
                intro()
                print('Успешно!')
                print('Заходите в игру, и проверяйте изменения.')
                print('Если стало хуже вы можете восстановить всё по умолчанию после повторного запуска программы!')
                time.sleep(5)
            else:
                main()
        if a == "2":
            setup()
        if os.path.exists(main_path + "\\restorepoint"):
            if a == "3":
                clear()
                intro()
                print('Восстановление может занять некоторое времья... зависит от ПК')
                restore()
                print('Успешно!')
                time.sleep(2)
            if a == "4":
                clear()
                intro()
                shutil.rmtree(main_path + "\\restorepoint")
                print('Успешно!')
                time.sleep(2)

bots = "1"
font = "1"
videos = "1"
servers = "2"
stickers = "1"

    
main_path = '%s\\csgocleaner' %  os.environ['APPDATA']
clear = lambda: os.system('cls')

main()

























