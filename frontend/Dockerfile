FROM node:18-alpine
WORKDIR /app

# Copy only package files & install dependencies
COPY package*.json vite.config.js /app/
RUN npm install

COPY . /app

# Build the app
RUN npm run build

# Run the app
CMD ["npm", "run", "dev"]