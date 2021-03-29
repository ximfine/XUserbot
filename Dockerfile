# We're using Ubuntu 20.10
FROM ximfine/xproject:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/ximfine/XUserbot /home/ximfine/
RUN mkdir /home/ximfine/bin/
WORKDIR /home/ximfine/

# Upgrade pip
RUN pip install --upgrade pip

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ximfine/XUserbot/sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
