## 项目目录
根目录
> app: 接口目录  
> docs: 文档目录  
> migration: 数据库迁移目录  
> .env: 环境变量文件  
> .gitignore: git忽略文件  
> alembic.ini: alembic配置文件  
> main.py: 项目启动文件  
> README.md: 项目说明文件  
> requirements.txt: 项目依赖文件  

app目录
> api: 接口目录  
> config: 配置文件目录  
> core: 核心代码目录  
> db: 数据库目录  
> models: 数据库模型目录  
> repositories: 数据库操作目录  
> schemas: 数据库模型验证目录  
> services: 存放独立的业务逻辑函数或类  
> tests: 测试文件目录  
> app.py: fastapi app实例文件  

app/api目录  
> api_v1: 接口版本1目录  
> api_v2: 接口版本2目录  
> api_routers.py: 总路由文件  


## 开发日志
### 2023-09-10
- [x] 1. 项目初始化


### 2023-09-21
- [x] 1. 完成了数据库中用户表、资料表、社交表、权限表等表的创建
- [x] 2. 部分完成用户名注册、手机号码注册的接口

待完成：
- [ ] 1. 用户注册成功后，返回token的功能


### 2023-09-23
- [x] 1. 完善了RBAC的设计
- [x] 2. 重构项目目录结构