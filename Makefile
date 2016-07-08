
# building deployment directory

build: clean copy tar

clean:
    rm -rf dist dist.tar.gz

copy:
    mkdir dist
    cp -R mongomq dist

tar:
    tar -zc dist/ | gzip > dist.tar.gz

.PHONY: build
