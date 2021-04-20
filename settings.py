import os

# 当前项目的路径
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
# 当前项目下的mainapp的文件路径
BASE_DIR = os.path.join(PROJECT_DIR, 'mainapp')
# mainapp文件下的静态资源static文件的路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# user文件的绝对路径
USER_DIR = os.path.join(STATIC_DIR, 'user')

class Dev():
    ENV = 'development'
    DEBUG = True

    # 配置sqlalchemy数据库连接特征
    # 数据库连接的路径 dialect+driver://user:password@ip:port/db?charset=utf8
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.102.218.113/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS =True # 可扩张
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 发生异常时，回收资源
    SQLALCHEMY_ECHO = True # True 显示调试SQL

if __name__ == '__main__':
    print(os.path.dirname(__file__))
    print(PROJECT_DIR)
    print(BASE_DIR)