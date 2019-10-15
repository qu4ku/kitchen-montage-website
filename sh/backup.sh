#!/bin/bash
# cron 
# 0 1 * * * bash  /var/www/knowledgeprotocol/current/src/sh/backup.sh

source /var/www/knowledgeprotocol/current/env/bin/activate
python /var/www/knowledgeprotocol/current/src/manage.py dbbackup -s knowledgeprotocol --settings=project.settings.production
