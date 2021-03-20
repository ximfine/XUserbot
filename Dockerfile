# We're using Ubuntu 20.10
FROM ximfine/remix:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/ximfine/XUserbot /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

#Install python requirements
# RUN pip3 install -r https://raw.githubusercontent.com/ximfine/XUserbot/sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
