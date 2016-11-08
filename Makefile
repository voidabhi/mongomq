
# building deployment directory

build: clean copy tar

clean:
    rm -rf dist dist.tar.gz

copy:
    source ./venv/bin/activate
    pip freeze > requirements.txt
    mkdir dist
    cp -R mongomq dist
    cp -R requirements.txt dist

tar:
    tar -zc dist/ | gzip > dist.tar.gz

.PHONY: build
