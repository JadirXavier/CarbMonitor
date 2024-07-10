#!/bin/sh

# Garante as permissões para o usuário duser criass as pastas static e media
chown -R duser:duser /data/web/static /data/web/media
chmod -R 755 /data/web/static /data/web/media

exec "$@"