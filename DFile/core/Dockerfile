FROM debian:latest
MAINTAINER 0mu
RUN apt-get update
RUN apt-get install -y locales
RUN /usr/sbin/locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
ENV PATH $PATH:/opt/pypy3/bin
RUN apt-get install -y python3 python python3-dev curl git
RUN apt-get install -y bzip2
RUN curl -L https://bitbucket.org/pypy/pypy/downloads/pypy3-2.4.0-linux64.tar.bz2 | tar -jxf - && mv pypy* /opt/pypy3
RUN curl -s https://bootstrap.pypa.io/get-pip.py | pypy3
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python3
RUN echo "export VISIBLE=now" >> /etc/profile
ENV HOME /root
WORKDIR /root
