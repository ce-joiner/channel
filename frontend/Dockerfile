FROM node:18-slim
WORKDIR /app

# Copy only manifest + config, install deps (omit Rollup’s optional natives)
COPY package*.json ./

ENV ROLLUP_SKIP_NATIVES=true
ENV npm_config_arch=x64
ENV npm_config_platform=linux

RUN npm install

COPY . .
EXPOSE 5173


# Run the app
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]