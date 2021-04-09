


class Dev():
    ENV = 'development'
    DEBUG = True

    # 配置sqlalchemy数据库连接特征
    # 数据库连接的路径 dialect+driver://user:password@ip:port/db?charset=utf8
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@47.102.218.113/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS =True # 可扩张
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True # 发生异常时，回收资源
    SQLALCHEMY_ECH = True # True 显示调试SQL