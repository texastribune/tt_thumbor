#!/usr/bin/env bash

echo $THUMBOR_PORT

thumbor --port=$THUMBOR_PORT --conf=/app/thumbor.conf