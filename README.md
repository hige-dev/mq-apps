
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
