
```bash
if [ ! -f app/db/dbconfig.ini ]; then
cat << EOF > app/db/dbconfig.ini
[postgresql]
host     = postgres
port     = 5432
user     = ...
dbname   = ...
password = ...
EOF
fi
```

```bash
apk add --no-cache build-base postgresql-dev
cd /app
python -m pip install -r requirements.txt
```
