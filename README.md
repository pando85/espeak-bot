ESpeak Bot
=========
Resend text in audio format using espeak.


Setup
=====

You will need to add this enviroment variables:
* BOT_TOKEN: token from [@BotFather](https://telegram.me/BotFather).
* BOT_URL(Optional): url where you setup webhook.
* CERTIFICATE_PATH(Optional): self signed certificated to [set webhook](https://core.telegram.org/bots/api#setwebhook).
* PORT(Optional): listen port in webhook mode.
If BOT_URL or CERTIFICATE_PATH are not set, Bot will run without webhook.

Example using docker-compose:
```yml
espeak-bot:
  restart: always
  image: pando85/espeak-bot
  ports:
     - "5000:5000"
  volumes:
    - ./cert.pem:/tmp/cert.pem:ro
  environment:
    - BOT_TOKEN= Telegram Bot API token
    - BOT_URL= Telegram Bot URL
    - CERTIFICATE_PATH=/tmp/cert.pem
    - PORT=5000
```