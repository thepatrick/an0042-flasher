#!/bin/bash

while ! python3 flash.py; do
    sleep 1 # or more, or less
done