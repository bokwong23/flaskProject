from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wbk:wbk@127.0.0.1/config'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import InstanceConfig

# 推入应用上下文
app.app_context().push()

# 创建数据表
db.create_all()
print('Tables created successfully')

