# Use an official node runtime as a parent image
FROM node:12.16.1-alpine

WORKDIR /app/

# Install dependencies
COPY package.json yarn.lock /app/

RUN yarn

# Add rest of the client code
COPY . /app/

EXPOSE 3000

# CMD npm start