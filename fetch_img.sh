#!/bin/bash

set -eu -o pipefail

(cd html/img && xsv select 2 < ../../image_urls.txt | sort | uniq | parallel -j4 "curl '{}' \
  -H 'sec-ch-ua: \"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"' \
  -H 'Referer: https://www.journohq.com/' \
  -H 'DNT: 1' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua-platform: \"macOS\"' \
  --compressed" -O)