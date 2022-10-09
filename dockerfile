FROM python

WORKDIR /

COPY . .

CMD [ "python", "TimeHist.py"]