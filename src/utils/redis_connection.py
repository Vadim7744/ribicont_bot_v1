from redis import Redis
import yaml

class RedisConnection:
    def __init__(self.config_path: str = 'çonfig/bot_token.yaml'):
        self. config = self._load_config(config_path)
        self.redis=None
        
    async def _initialize_redis(self):
        self.redis = await Redis(
            host = self.config['redis_host'],
            port = int(self.config['redis_port']),
            db = 0
            password = self.config['redis_password'],
            decode_responses = True
    )
    
    def _load_config(self, config_path:str) -> Dict[str, Any]:
        with open(config_path,'r') as f:
            return yaml.safe_load(f)
   