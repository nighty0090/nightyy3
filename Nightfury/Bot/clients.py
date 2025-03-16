import asyncio
import logging
from info import *
from pyrogram import Client
from Nightfury.util.config_parser import TokenParser
from . import multi_clients, work_loads, NightfuryBot


async def initialize_clients():
    """Initialize multiple bot clients if additional tokens are available."""
    multi_clients[0] = NightfuryBot
    work_loads[0] = 0
    all_tokens = TokenParser().parse_from_env()

    if not all_tokens:
        logging.info("No additional clients found, using default client.")
        return

    async def start_client(client_id, token):
        """Start a client bot instance with the given token."""
        try:
            logging.info(f"Starting - Client {client_id}")
            if client_id == len(all_tokens):
                await asyncio.sleep(2)
                logging.info("Initializing clients, please wait...")

            client = Client(
                name=str(client_id),
                api_id=API_ID,
                api_hash=API_HASH,
                bot_token=token,
                sleep_threshold=SLEEP_THRESHOLD,
                no_updates=True,
                in_memory=True
            )

            await client.start()
            work_loads[client_id] = 0
            return client_id, client

        except Exception as e:
            logging.error(f"Failed to start Client {client_id}: {e}", exc_info=True)
            return None  # Return None to avoid breaking the loop

    # Start clients asynchronously and filter out failed ones
    clients = await asyncio.gather(*[start_client(i, token) for i, token in all_tokens.items()])
    clients = {client_id: client for client_id, client in clients if client is not None}

    multi_clients.update(clients)

    if len(multi_clients) > 1:
        logging.info("Multi-Client Mode Enabled")
    else:
        logging.info("No additional clients initialized, using default client.")
