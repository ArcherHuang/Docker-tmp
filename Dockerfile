FROM node:8

WORKDIR /app

RUN chown -R node:node /usr/local/lib/node_modules
RUN chown -R node:node /usr/local/bin
USER node

RUN npm install node-red -g
RUN npm i node-red/node-red-dashboard -g

# port 1880 for Node-RED
EXPOSE 1880

CMD node-red