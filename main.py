from DecryptLogin import login
import os
import sys

if __name__ == '__main__':
    script, user_account, user_pwd, *_ = sys.argv
    lg = login.Login()
    infos_return, session = lg.zhihu(user_account, user_pwd, 'pc')
    print(infos_return, session)
