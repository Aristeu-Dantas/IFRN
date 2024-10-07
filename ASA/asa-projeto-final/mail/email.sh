#!/bin/bash
echo "Starting dovecot..."
service dovecot start

echo "Starting Postfix..."
service postfix start
