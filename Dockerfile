FROM keyi/python2-mcr2017a-rpi-isl

COPY JSTMB_O196/ ./JSTMB_O196
COPY setup.py ./
COPY O196_JSTMB_wrapper.py ./
COPY trainData.csv ./
COPY trainTargets.csv ./
