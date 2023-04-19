## Commands:

### Export project requirements
`poetry export --with dev -f requirements.txt --output src/requirements.txt`

### Generate migrations
`alembic revision --autogenerate -m "init"`  
`alembic upgrade head`

### Deploy commands
`docker-compose -f docker-compose.dev.yml stop`  
`docker-compose -f docker-compose.dev.yml rm -f`  
`docker-compose -f docker-compose.dev.yml build`  
`docker-compose -f docker-compose.dev.yml up -d --remove-orphans`  
