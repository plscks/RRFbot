FROM arm32v7/node:alpine
RUN apk add --update \
  python \
  python-dev \
  py-pip \
  build-base \
  git \
  openssh-client \
&& pip install virtualenv \
&& rm -rf /var/cache/apk/*

WORKDIR /usr/app
COPY package.json ./
RUN npm install
COPY . ./
RUN node ./RRFbot.js -t "`wget -O - -q http://localhost:8000/secret.txt`"
