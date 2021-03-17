# We're using Ubuntu 20.10
FROM alfianandaa/alf:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/X-Newbie/XUserbot /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

CMD ["python3","-m","userbot"]
