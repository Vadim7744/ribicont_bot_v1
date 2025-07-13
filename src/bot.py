from aiohttp import ClientSession
import yaml
from typing import Optional, Any, Dict

class Basebot:
    def __init__(self,config_path:str = '.....'):
        self.config = self._load_config(config_path)
        self.redis = self._initialize_redis()
        self.session = None
        
    async def _initialize_redis(self):
        redis_instance = await redis.Redis(
            host = self.config['redis_host'],
            port = int(self.config['redis_host'])
            db = 0,
            password = self.config['redis_psaaword'],
            decode_responses = True
        )
        return redis_instance
    
    async def _load_config(self, config_path: str) -> Dict[str, Any]:
        with open(config_path,'r') as f:
            return yaml.sefe_load(f)
        
    async def _process_feedback(self):
        try:
            async with ClientSession() as session:
                async for feedback in self._get_feedback():
                    await self._send_notification(feedback)
                    
    async def _get_feedback(self):
        while True:
            try:
                async with
session.get('https://rubicont174.ru/bitrix/admin/iblock_element_admin.php', params) as response:
                    if response.status == 200:
                        data = await responce.json()
                        if 'feedback' in data and len(data['feedback']) > 0:
                            yield data['feedback']
            except Exeption as e:
                print(f"Ошибка получения заявок:{e}")
            await asyncio.sleep(5)
            
    async def _send_notification(self, feedback_data:Dict):
        phone =feedback_data.get('phone')
        date =feedback_data.get('date')
        method =feedback_data.get('method')
        
        try:
            await self._telegram_client.send_message(
                chat_id = feedback_data['user_id']
                text=f"Новая заявка:{phone},{date},{method}"
                )
        except Exeption as e:
            print(f"Ошибка отправки уведомления:{e}")
            
    async def run(self):
        self._telegram_client = await self._initialize_telegram()
        while True:
            await self._process_feedback()
            
            
class Bot(Basebot):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.telegram_token = self.config['bot_token']
        self._telegram_client= None
        
    async def _initialize_telegram(self):
        await self._telegram_client = Client(
            token = self.telegram_token,
            loop = self.loop
        )
        
if __name__ == '__main__':
    from paylib import Path
    config_path = Path(__file__).parent.parent/ 'config' / 'bot_token.yaml'
    
    async def main():
        bot = Bot()
        await bot.run()
        
    if __name__ == '__main__':
        from aiohttp import ClientSession
        asyncio.run(main())