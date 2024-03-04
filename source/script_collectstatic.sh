#!/bin/bash
python3 manage.py collectstatic --noinput --settings=starter.settings_production
