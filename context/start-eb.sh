#!/usr/bin/env bash
set -o errexit

eb create heatmap-scatterplot
eb status | grep CNAME | sed 's/CNAME: /http:\/\//'