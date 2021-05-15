#!/bin/sh
# It needs to have only 1 worker process to avoid starting the scheduler multiple times
gunicorn -w 1 server:app --bind 0.0.0.0:5000
