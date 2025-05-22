FROM node:20

WORKDIR /app

RUN npm install -g @angular/cli

COPY . .

RUN npm install 

EXPOSE 4200

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]