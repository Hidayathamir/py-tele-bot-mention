# py-tele-bot-mention

Telegram Bot to mention

## Quick Start

```shell
docker run -it --rm \
	-e BOT_TOKEN="your_bot_token" \
	-e MAP_MENTION='{"@person_a": ["@person_b", "@person_c"]}' \
	hidayathamir/py-tele-bot-mention
```

## Note

By default, the bot cannot read messages in groups. One way to allow it to read messages is to promote the bot to admin.
