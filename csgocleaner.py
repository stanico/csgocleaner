# CSGO CLEANER v0.4 12/03/2022
# credits: stanico#1206
# tg: @Stanico
# github.com/stanico/csgocleaner/


import os
import shutil
import time
from distutils.dir_util import copy_tree
from progress.bar import IncrementalBar


log = []


def clear():
    os.system('cls')


def language():
    global lang
    wr = ""
    clear()
    intro()
    if not os.path.exists(main_path + '\\lang.txt'):
        print('[1] Русский')
        print('[2] English')
        ans = input('Выберите язык / Select language: ')
        if ans == '1':
            wr = 'russian'
            lang = lang_ru
        if ans == '2':
            wr = 'english'
            lang = lang_en
        with open(main_path + "\\lang.txt", "w") as file:
            file.write(wr)
            file.close()
            clear()
            intro()
    else:
        with open(main_path + "\\lang.txt", "r") as file:
            a = file.read()
            if a == "russian":
                lang = lang_ru
            if a == "english":
                lang = lang_en
            clear()
            intro()


def remove_file(path, file):
    if os.path.exists(os.path.join(csgo_path + path + file)):
        if os.path.exists(os.path.join(main_path + path)):
            pass
        else:
            os.makedirs(main_path + path)
        shutil.copy(os.path.join(csgo_path + path + file), os.path.join(main_path + path + file))
        os.remove(os.path.join(csgo_path + path + file))
    else:
        log.append('[ERROR] FILE NOT EXISTS ')
        log.append(file + " " + path+" | ")


def restore_file(path, file):
    if os.path.exists(os.path.join(main_path + path + file)):
        if os.path.exists(os.path.join(csgo_path + path)):
            pass
        else:
            os.makedirs(os.path.join(csgo_path + path))
        shutil.copy(os.path.join(main_path + path + file), os.path.join(csgo_path + path + file))
        os.remove(os.path.join(main_path + path + file))
    else:
        log.append('[ERROR] FILE NOT EXISTS ')
        log.append(file + " " + path+" |")


def remove_tree(path):
    if os.path.exists(os.path.join(csgo_path + path)):
        if os.path.exists(os.path.join(main_path + path)):
            pass
        else:
            os.makedirs(os.path.join(main_path + path))
        copy_tree(os.path.join(csgo_path + path), os.path.join(main_path + path))
        shutil.rmtree(os.path.join(csgo_path + path))
    else:
        log.append('[ERROR] TREE NOT FOUND ')
        log.append(path+" | ")


def restore_tree(path):
    if os.path.exists(os.path.join(main_path + path)):
        if os.path.exists(os.path.join(csgo_path + path)):
            pass
        else:
            os.makedirs(os.path.join(csgo_path + path))
        copy_tree(os.path.join(main_path + path), os.path.join(csgo_path + path))
        shutil.rmtree(os.path.join(main_path + path))
    else:
        log.append('[ERROR] TREE NOT EXISTS ')
        log.append(path+' | ')


def remove_byext(ext, path):
    list = os.listdir(os.path.join(csgo_path + path))
    if os.path.exists(os.path.join(main_path + path)):
        pass
    else:
        os.makedirs(os.path.join(main_path + path))
    for item in list:
        if item.endswith(ext):
            shutil.copy(os.path.join(csgo_path + path, item), os.path.join(main_path + path))
            os.remove(os.path.join(csgo_path + path, item))


def clear_files(ext, path):
    list = os.listdir(os.path.join(csgo_path + path))
    if os.path.exists(os.path.join(main_path + path)):
        pass
    else:
        os.makedirs(os.path.join(main_path + path))
    for item in list:
        if item.endswith(ext):
            shutil.copy(os.path.join(csgo_path + path, item), os.path.join(main_path + path))
            os.remove(os.path.join(csgo_path + path, item))
            with open(csgo_path + path+"\\"+item, "w") as file:
                file.write("")
                file.close()


def clean():
    global main_path
    if bots == "1" or stickers == "1" or videos == "1" or font == "1" or servers == "2":
        print(lang[8])
    else:
        pass
    if bots == "1":
        print(lang[9])
    if stickers == "1":
        print(lang[10])
    if videos == "1":
        print(lang[11])
    if font == "1":
        print(lang[12])
    if servers == "2":
        print(lang[13])
    print('')
    print(lang[14])
    print(lang[15])
    print(lang[16])
    b = input(lang[7])
    if b == '1':
        clear()
        intro()
        print(lang[17])
    else:
        main()
    bar = IncrementalBar('Progress', max = 100)
    main_path = main_path + "\\restorepoint"
    # File Source: vk.com/boostfixteam
    remove_byext(".mdmp", "\\")
    bar.next()
    remove_file("\\", "chrome.pak")
    bar.next()
    remove_tree("\\directx_installer")
    bar.next()
    remove_tree("\\EmplySteamDepot")
    bar.next()
    # bin
    remove_tree("\\bin\\locales")
    bar.next()
    remove_tree("\\bin\\map_publish")
    bar.next()
    remove_tree("\\bin\\prefabs")
    bar.next()
    remove_tree("\\bin\\v8_winxp")
    bar.next()
    remove_file("\\bin\\", "convertdmx.lua")
    bar.next()
    remove_file("\\bin\\", "libfbxsdk.dll")
    bar.next()
    remove_file("\\bin\\", "maplist_csgo.txt")
    bar.next()
    remove_file("\\bin\\", "mssdolby.flt")
    bar.next()
    remove_file("\\bin\\", "mssdsp.flt")
    bar.next()
    remove_file("\\bin\\", "msseax.flt")
    bar.next()
    remove_file("\\bin\\", "msssrs.flt")
    bar.next()
    remove_file("\\bin\\", "telemetry32c.dll")
    bar.next()
    remove_file("\\bin\\", "trxtemplate.xml")
    bar.next()
    remove_file("\\bin\\", "vidcfg.bin")
    bar.next()
    # csgo
    remove_tree("\\csgo\\expressions")
    bar.next()
    remove_tree("\\csgo\\materials")
    bar.next()
    remove_tree("\\csgo\\models")
    bar.next()
    remove_tree("\\csgo\\scenes")
    bar.next()
    remove_tree("\\csgo\\resource")
    bar.next()
    restore_tree("\\csgo\\resource\\overviews")
    bar.next()
    restore_file("\\csgo\\resource\\ui\\", "buymenuconfig.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "valve_english.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "valve_russian.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "mp3player_english.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "boxrocket_english.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "dmecontrols_english.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "csgo_english.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "gameui_russian.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "chat_russian.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "sfui_russian.txt")
    bar.next()
    restore_file("\\csgo\\resource\\", "csgo_russian.txt")
    bar.next()
    if stickers == "1":
        bar.next()
        pass
    else:
        restore_file("\\csgo\\resource\\", "vmtcache.txt")
        bar.next()
    remove_tree("\\csgo\\scripts")
    bar.next()
    remove_tree("\\csgo\\cache")
    bar.next()
    restore_file("\\csgo\\scripts\\", "instructor_textures.txt")
    bar.next()
    restore_file("\\csgo\\scripts\\", "inventory_structure.txt")
    bar.next()
    restore_file("\\csgo\\scripts\\items\\", "items_game.txt")
    bar.next()
    remove_file("\\csgo\\bin\\", "client_panorama.dll")
    bar.next()
    remove_file("\\csgo\\", "modelsounds.cache")
    bar.next()
    remove_file("\\csgo\\", "bspconvar_whitelist.txt")
    bar.next()
    remove_file("\\csgo\\", "gamemodes_server.txt.example")
    bar.next()
    remove_file("\\csgo\\", "demo_polish_settings.cfg")
    bar.next()
    remove_file("\\csgo\\", "demoheader.tmp")
    bar.next()
    remove_file("\\csgo\\", "gamerulescvars.txt.example")
    bar.next()
    remove_file("\\csgo\\", "leaderboardsconfig.txt")
    bar.next()
    remove_file("\\csgo\\", "lights.rad")
    bar.next()
    remove_file("\\csgo\\", "loadouts.txt")
    bar.next()
    remove_file("\\csgo\\", "maplist.txt")
    bar.next()
    remove_file("\\csgo\\", "medalsconfig.txt")
    bar.next()
    remove_file("\\csgo\\", "motd.txt")
    bar.next()
    remove_file("\\csgo\\", "mapcycle.txt")
    bar.next()
    remove_file("\\csgo\\", "missioncycle.txt")
    bar.next()
    remove_file("\\csgo\\", "steam_appid.txt")
    bar.next()
    remove_file("\\csgo\\", "navplace.db")
    bar.next()
    remove_file("\\csgo\\", "pure_server_whitelist.txt")
    bar.next()
    remove_file("\\csgo\\", "radial_quickinventory.txt")
    bar.next()
    remove_file("\\csgo\\", "radial_radio.txt")
    bar.next()
    remove_file("\\csgo\\", "scene.cache")
    bar.next()
    remove_file("\\csgo\\", "serverconfig.vdf")
    bar.next()
    remove_file("\\csgo\\", "splitscreen_config.txt")
    bar.next()
    remove_file("\\csgo\\", "unusedcontent.cfg")
    bar.next()
    remove_file("\\csgo\\", "whitelist.cfg")
    bar.next()
    remove_file("\\csgo\\", "whitelist_beta.cfg")
    bar.next()
    remove_tree("\\csgo\\maps\\soundcache")
    bar.next()
    remove_tree("\\csgo\\maps\\graphs")
    bar.next()
    remove_tree("\\csgo\\maps\\workshop")
    bar.next()
    remove_byext(".txt", "\\csgo\\maps")
    bar.next()
    remove_byext(".jpg", "\\csgo\\maps")
    bar.next()
    clear_files(".cfg", "\\csgo\\maps\\cfg")
    bar.next()
    if videos == "1":
        remove_tree("\\csgo\\panorama\\fonts")
        bar.next()
    else:
        bar.next()
    if font == '1':
        remove_tree("\\csgo\\panorama\\videos")
        bar.next()
    else:
        bar.next()
    # platform
    if servers == "2":
        remove_tree("\\platform\\materials")
        bar.next()
        remove_tree("\\platform\\resource")
        bar.next()
        remove_tree("\\platform\\scripts")
        bar.next()
        remove_tree("\\platform\\servers")
        bar.next()
        remove_tree("\\platform\\steam")
        bar.next()
        remove_tree("\\platform\\vgui")
        bar.next()
    else:
        bar.next()
        bar.next()
        bar.next()
        bar.next()
        bar.next()
        bar.next()
    if bots == "1":
        remove_byext(".nav", "\\csgo\\maps")
        bar.next()
        remove_file("\\csgo\\", "botchatter.db")
        bar.next()
        remove_file("\\csgo\\", "botprofile.db")
        bar.next()
        remove_file("\\csgo\\", "botprofilecoop.db")
        bar.next()
    else:
        bar.next()
        bar.next()
        bar.next()
        bar.next()
    bar.next()
    bar.next()
    clear()
    intro()
    print(lang[18])
    print(lang[19])
    print(lang[20])
    main_path = '%s\\csgocleaner' % os.environ['APPDATA']
    with open(main_path +'\\log.txt', "w") as file:
            file.write(' '.join(log))
            file.close()
    time.sleep(5)


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
    print('\____//____/\____/\____/   \____/_____/_____/_/  |_/_/ |_/v0.4_/_/ |_| ')
    print('Credits: stanico#1206')
    print('')


def setup():
    global bots
    global stickers
    global videos
    global font
    global servers
    clear()
    intro()
    print(lang[22])
    print(lang[15])
    print(lang[16])
    bots = input(lang[21])
    clear()
    intro()
    print(lang[23])
    print(lang[15])
    print(lang[16])
    stickers = input(lang[21])
    clear()
    intro()
    print(lang[24])
    print(lang[15])
    print(lang[16])
    videos = input(lang[21])
    clear()
    intro()
    print(lang[25])
    print(lang[15])
    print(lang[16])
    font = input(lang[21])
    clear()
    intro()
    print(lang[26])
    print(lang[15])
    print(lang[16])
    servers = input(lang[21])
    clear()
    intro()
    print(lang[27])
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
        os.makedirs(main_path)
        language()
        print(lang[0])
        print(lang[1])
        csgo_path = input()
        if os.path.exists(csgo_path + "\\csgo.exe"):
           
            with open(main_path + '\\path.txt', 'w') as file:
                file.write(csgo_path)
                file.close()
            clear()
            intro()
            print(lang[2])
            print(lang[3])
            print(lang[4])
            a = input(lang[7])
            if a == "1":
                clear()
                intro()
                clean()
            pass
            if a == "2":
                setup()
        else:
            print(lang[28])
            input('')
            exit()
    else:
        language()
        with open(main_path + '\\path.txt', 'r') as file:
            csgo_path = file.read()
            file.close()
        print(lang[3])
        print(lang[4])
        if os.path.exists(main_path + "\\restorepoint"):
            print(lang[5])
            print(lang[6])
        a = input(lang[7] + ' ')

        if a == "1":
            clear()
            intro()
            clean()
            main_path = '%s\\csgocleaner' % os.environ['APPDATA']
            with open(main_path +'\\log.txt', "w") as file:
                file.write(' AAA'.join(log))
                file.close()
        if a == "2":
            setup()

        if os.path.exists(main_path + "\\restorepoint"):
            if a == "3":
                clear()
                intro()
                print(lang[29])
                restore()
                print(lang[18])
                time.sleep(2)
            if a == "4":
                clear()
                intro()
                shutil.rmtree(main_path + "\\restorepoint")
                print(lang[18])
                time.sleep(2)


bots = "1"
font = "1"
videos = "1"
servers = "2"
stickers = "1"

main_path = '%s\\csgocleaner' % os.environ['APPDATA']
lang_ru = ['Введите путь к папке CS:GO', 'Пример: C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive', "Примечание: Перед очисткой желательно посетить вкладку Настройка", '[1] Очистка', '[2] Настройка', '[3] Возврат', '[4] Удалить точку восстановления', 'Выберите действие: ', 'Изменения после очистки: ', ' - Не будут работать боты в локальной игре (На картах по типу AimBotz будут)', ' - Не будут видны стикеры на оружиях', ' - Не будет заднего фона в меню (Будет просто черное)', ' - Будет системный шрифт, вместо обычного', ' - Не будут работать сервера сообщества', 'Начить очистку?', '[1] Да', '[2] Нет', 'Очистка может занять некоторое времья... зависит от ПК', 'Успешно!', 'Заходите в игру, и проверяйте изменения.', 'Если стало хуже вы можете восстановить всё по умолчанию после повторного запуска программы!', 'Выберите ответ: ', 'Отключить ботов? (На картах по типу AimBotz они будут!) [1/5]', 'Отключить стикеры? (Их не будет видно на оружиях) [2/5]', 'Отключить фон в меню? (В параметры запуска нужно будет вводить -novid) [3/5]', 'Отключить шрифт? (Вместо обычного шрифта, будет системный) [4/5]', 'Вы играете на серверах сообщества? [5/5]', 'Настройка завершена успешно, теперь можно приступать к очистке!', 'Не удалось найти csgo.exe!', 'Восстановление может занять некоторое время... зависит от ПК']
lang_en = ['Enter the path to the CS:GO folder', 'Example: C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive', "Note: Before cleaning better to open the settings tab", '[1] Cleaning', '[2] Settings', '[3] Restore files', '[4] Remove restore point', 'Select action: ', 'Changes after cleanup: ', ' - Bots won`t work on local game (On maps like AimBotz they should work)', ' - Stickers on weapons will not be visible', ' - There will be no background in the menu (It will be just black)', ' - There will be a system font instead of default csgo font', ' - Community servers will not work', 'Start cleaning?', '[1] Yes', '[2] No', 'Cleaning up may take some time... depends on your PC', 'Successful!', 'Go into the game and check the changes.', 'If game gets worse you can restore everything into default after restarting the program!', 'Select answer: ', 'Disable bots? (Maps like AimBotz will have them!) [1/5]', "Disable stickers? (They won't be visible on weapons)", 'Disable menu background? (You will need to enter -novid in the launch options)', 'Disable font? (Instead of regular font, it will be system font)', 'Do you play on community servers? [5/5]', 'Setup completed successfully, now you can start cleaning!', 'Could not find csgo.exe!', 'Restoration may take some time... depends on the PC']


main()
