FROM python:3

ADD crawler.py /

RUN pip install scrapy
RUN mkdir results

CMD ["scrapy", "runspider", "crawler.py", "-s", "FEED_URI=results/result.json", "-s", "FEED_FORMAT=json"]
