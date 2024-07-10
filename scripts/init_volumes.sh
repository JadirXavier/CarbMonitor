#!/bin/sh

# Garante as permissões par ao usuário duser
chown -R duser:duser /data/web/static /data/web/media
chmod -R 755 /data/web/static /data/web/media

exec "$@"