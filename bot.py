from highrise import BaseBot
from highrise.models import SessionMetadata, User, Position
from highrise.__main__ import main
import asyncio

class PixalPalBot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata):
        self._session_metadata = session_metadata
        print("✅ Bot is online.")
        print(f"🪪 Bot ID: {session_metadata.user_id}")
        print("🤖 Waiting to print full bot username when it joins...")
        await self.highrise.send_message("👋 PixalPal has entered the room! Type !help for commands.", None)

    async def on_user_join(self, user: User):
        if user.id != self._session_metadata.user_id:
            await self.highrise.send_message(f"👋 Welcome @{user.username}!", None)

    async def on_user_leave(self, user: User):
        print(f"👋 {user.username} left the room.")

    async def on_chat(self, user: User, message: str):
        command = message.strip().lower()
        print(f"[💬] {user.username}: {message}")

        if command == "!hello":
            await self.highrise.send_message(f"👋 Hello, @{user.username}!", None)

        elif command == "!help":
            await self.highrise.send_message(
                "📜 Commands: !hello, !jump, !dance, !wave, !info, !clap, !sit, !sleep, !cry",
                None
            )

        elif command == "!jump":
            await self.highrise.teleport(user.id, Position(0, 0, 0))

        elif command == "!dance":
            await self.highrise.emote(user.id, "dance")

        elif command == "!wave":
            await self.highrise.emote(user.id, "wave")

        elif command == "!clap":
            await self.highrise.emote(user.id, "clap")

        elif command == "!sit":
            await self.highrise.emote(user.id, "sit")

        elif command == "!sleep":
            await self.highrise.emote(user.id, "sleep")

        elif command == "!cry":
            await self.highrise.emote(user.id, "cry")

        elif command == "!info":
            await self.highrise.send_message(
                "🤖 You're chatting with PixalPal – built using the Highrise SDK & Python!",
                None
            )

# Structure for passing to highrise.main
class BotDefinition:
    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token

if __name__ == "__main__":
    room_id = "659a0f6c16b47a0ce0a6e673"
    token = "4f89ace23d0f723c40165cd60ebba6fa98ea88e47dde73d96c7fe81f5e301c86"

    bot_instance = PixalPalBot()
    bot_definition = BotDefinition(bot_instance, room_id, token)

    asyncio.run(main([bot_definition]))
