#!/bin/bash
curl -s $1 | grep "href=" | cut -d'"' -f2
