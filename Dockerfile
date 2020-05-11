FROM arm32v7/node:14-stretch
RUN apt-get update && apt-get install -y \
    libsqlite3-dev
WORKDIR /usr/app
COPY package.json ./
RUN npm install sqlite3 --build-from-source --sqlite=/usr
RUN npm install
COPY . ./
RUN echo "TOKEN IS: $TOKEN"
CMD [ "node",  "--trace-warnings", "--unhandled-rejections=strict", "RRFbot.js", "-t", "${TOKEN}" ]
