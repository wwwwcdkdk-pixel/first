# FastAPI + MySQL + Docker

## 项目功能
- FastAPI 提供商品查询 API
- PyMySQL 连接 MySQL
- Docker Compose 管理容器
- MySQL Volume 数据持久化
- Healthcheck 健康检查

## 技术栈
Python 3.11 / FastAPI / MySQL 8 / Docker Compose

## 启动步骤

1. 复制 .env.example 为 .env
2. 配置数据库密码
3. 启动项目：

docker compose up -d --build

## API

GET /products
GET /health

## API 文档

http://localhost:9000/docs