#!/bin/bash
ls -F $1 | grep '@$' | tr -d @
