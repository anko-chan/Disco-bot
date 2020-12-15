import configparser
import os
import errno

class Config:
    def __init__(self):
            #____________________________________
            #config読み込みと各種セットアップ
            #____________________________________
            config = configparser.ConfigParser()
            config_ini_path = 'settings.ini'
            #configファイルがない場合のエラー
            if not os.path.exists(config_ini_path):
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), config_ini_path)

            config.read(config_ini_path, encoding='utf-8')

            self.boss = str(config['Boss']['BossID'])
            self.token = str(config['bot']['BotToken'])
