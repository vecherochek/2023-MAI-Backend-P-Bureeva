# Tест производительности

- [gunicorn](#gunicorn)
- [gunicorn через проксирование nginx](#gunicorn-через-проксирование-nginx)
- [nginx](#nginx)
- [nginx статический файл](#nginx-статический-файл)


## gunicorn

**Finished 1457 requests**
| | |
|:----|:----|
|Concurrency Level|      2|
|Time taken for tests|  1.000 seconds|
|Complete requests|     1326|
|Failed requests|        0|
|Total transferred|      202878 bytes|
|HTML transferred|       18564 bytes|
|Requests per second|    1325.47 [#/sec] (mean)|
|Time per request|       1.509 [ms] (mean)|
|Time per request|       0.754 [ms] (mean, across all concurrent requests)|
|Transfer rate|          198.04 [Kbytes/sec] received|

**Connection Times (ms)**
| | min | mean[+/-sd] | median | max |
|:----|:----:|:----:|:----:|:----:|
|Connect|        0  |  0  | 0.5   |   0   |   10|
|Processing|     0  |  1  | 1.6   |   1   |   43|
|Waiting|        0  |  1  | 1.5   |   1   |   41|
|Total|          0  |  1  | 1.9   |   1   |   53|

**Percentage of the requests served within a certain time (ms)**
| | |
|:----:|:----:|
|  50%     | 1|
|  66%     | 1|
|  75%    |  1|
|  80%     | 2|
|  90%    |  2|
|  95%   |   3|
|  98%  |    4|
|  99% |     4|
| 100%|     53 (longest request)|

## gunicorn через проксирование nginx

**Finished 1061 requests**
| | |
|:----|:----:|
|Server Software|        nginx/1.23.4|
|Server Hostname|        localhost|
|Server Port|            80|

| | |
|:----|:----:|
|Document Path|          /app/|
|Document Length|        14 bytes|

| | |
|:----|:----|
|Concurrency Level|      2|
|Time taken for tests|   1.000 seconds|
|Complete requests|      1061|
|Failed requests|        0|
|Total transferred|      166577 bytes|
|HTML transferred|       14854 bytes|
|Requests per second|    1060.50 [#/sec] (mean)|
|Time per request|       1.886 [ms] (mean)|
|Time per request|       0.943 [ms] (mean, across all concurrent requests)|
|Transfer rate|          162.60 [Kbytes/sec] received|

**Connection Times (ms)**
|              |min|  mean[+/-sd]| median|   max|
|:----|:----:|:----:|:----:|:----:|
|Connect|        0|    0|   0.2|      0|       3|
|Processing|     1|    2|   1.3|      1|      35|
|Waiting|        1|    1|   1.3|      1|      35|
|Total|          1|    2|   1.3|      2|      35|

**Percentage of the requests served within a certain time (ms)**
| | |
|:----|:----:|
|  50%  |    2|
|  66%  |    2|
|  75%  |    2|
|  80%  |    2|
|  90%  |    2|
|  95%  |    2|
|  98% |     3|
|  99%  |    4|
| 100%  |   35 (longest request)|

## nginx
**Finished 1743 requests**

| | |
|:----|:----:|
|Server Software: |       nginx/1.23.4|
|Server Hostname: |       localhost|
|Server Port:    |        80|

| | |
|:----|:----:|
|Document Path: |         /|
|Document Length:  |      187 bytes|

| | |
|:----|:----|
|Concurrency Level:  |    2|
|Time taken for tests:|   1.001 seconds|
|Complete requests: |     1743|
|Failed requests:   |     0|
|Total transferred: |     730317 bytes|
|HTML transferred:  |     325941 bytes|
|Requests per second: |   1740.88 [#/sec] (mean)|
|Time per request:  |     1.149 [ms] (mean)|
|Time per request:  |     0.574 [ms] (mean, across all concurrent requests)|
|Transfer rate:   |       712.33 [Kbytes/sec] received|

**Connection Times (ms)**
|             | min | mean[+/-sd]| median |  max|
|:----|:----:|:----:|:----:|:----:|
|Connect:     |   0  |  0 |  0.4   |   0  |     5|
|Processing:  |   0  |  1 |  0.7  |    1  |     8|
|Waiting:     |   0  |  1 |  0.6   |   0  |     8|
|Total:      |    0  |  1 |  0.9   |   1  |    12|

WARNING: The median and mean for the waiting time are not within a normal deviation
        These results are probably not that reliable.

**Percentage of the requests served within a certain time (ms)**
| | |
|:----|:----:|
|  50%  |    1|
|  66%  |    1|
|  75% |     1|
|  80% |     1|
|  90% |     2|
|  95% |     3|
|  98% |     4|
|  99% |     5|
| 100% |    12 (longest request)|

## nginx статический файл
**Finished 1964 requests**

| | |
|:----|:----:|
|Server Software: |       nginx/1.23.4|
|Server Hostname: |       localhost|
|Server Port:    |        80|

| | |
|:----|:----:|
|Document Path:  |        /haha|
|Document Length: |       18825 bytes|

| | |
|:----|:----|
|Concurrency Level:|      2|
|Time taken for tests:|   1.001 seconds|
|Complete requests: |     1964|
|Failed requests:   |     0|
|Total transferred:  |    37445960 bytes|
|HTML transferred:   |    36980255 bytes|
|Requests per second: |   1962.74 [#/sec] (mean)|
|Time per request:   |    1.019 [ms] (mean)|
|Time per request:   |    0.509 [ms] (mean, across all concurrent requests)|
|Transfer rate:     |     36544.86 [Kbytes/sec] received|

**Connection Times (ms)**
|            |  min | mean[+/-sd]| median|   max|
|:----|:----:|:----:|:----:|:----:|
|Connect:   |     0 |   0|   0.2   |   0   |    3|
|Processing: |    0 |   1 |  0.7   |   1  |     8|
|Waiting:     |   0 |   0 |  0.5  |    0  |     6|
|Total:     |     0  |  1 |  0.8   |   1  |     9|

**Percentage of the requests served within a certain time (ms)**
| | |
|:----|:----:|
|  50%   |   1|
 | 66%  |    1|
|  75%   |   1|
|  80%    |  1|
|  90%   |   2|
|  95%   |   2||
|  98%   |   3|
|  99%   |   4|
| 100%   |   9 (longest request)|

