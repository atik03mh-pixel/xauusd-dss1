
import logging
import os
from datetime import datetime

def setup_logger(name="gold_ai_assistant", log_dir="logs"):
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        # ফাইলে লগ সেভ করার জন্য
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # কনসোলে দেখানোর জন্য
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger
