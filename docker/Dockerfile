FROM bvlc/caffe:gpu

RUN cd /usr/lib/x86_64-linux-gnu && ln -s libhdf5_serial.so.10.1.0 libhdf5.so && ln -s libhdf5_serial_hl.so.10.0.2 libhdf5_hl.so

COPY caffe-fast-rcnn-faster-rcnn-upstream-33f2445/ action-faster-rcnn/caffe-fast-rcnn-faster-rcnn-upstream-33f2445/

RUN cd action-faster-rcnn/caffe-fast-rcnn-faster-rcnn-upstream-33f2445/ && make -j8 && make pycaffe

RUN apt-get update && apt-get install -y python-opencv python-tk
RUN pip install easydict
RUN pip install youtube_dl
RUN apt-get install -y vim
