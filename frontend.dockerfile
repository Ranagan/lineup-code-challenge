# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /code

# install app dependencies
COPY frontend/package.json /code/package.json
COPY frontend/package-lock.json /code/package-lock.json
RUN npm install

# add app
COPY frontend /code/

# start app
ENTRYPOINT ["npm", "start"]