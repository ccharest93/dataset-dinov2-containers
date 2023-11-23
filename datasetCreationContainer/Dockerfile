FROM ubuntu

#Install system requirements
RUN apt update && apt upgrade -y
RUN apt-get install -y \
build-essential \
git \
cmake \
ninja-build \
libcurlpp-dev \
zlib1g-dev

#Clone needed git repositories
RUN git clone https://github.com/ccharest93/dataset-dinov2.git
WORKDIR dataset-dinov2
RUN git clone https://github.com/ccharest93/tarlib.git

#Build tarlib library
RUN cd tarlib \
&& mkdir build \
&& cd build \
&& cmake -GNinja .. \
&& ninja

#Build dataset-dinov2 exe
RUN mkdir build \
&& cd build \
&& cmake .. \
&& make

FROM alpine
RUN apk add libc6-compat libcurl libstdc++ libgcc

COPY --from=0 dataset-dinov2/build/dataset-dinov2 /bin/dataset-dinov2

CMD ["dataset-dinov2"]
