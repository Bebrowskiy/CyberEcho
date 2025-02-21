import subprocess
import logging

# Настраиваем логирование
logging.basicConfig(filename="files/command_executor.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Запрещённые команды (можно расширять)
BLACKLIST_COMMANDS = ["rm", "reboot", "shutdown", "poweroff", "mkfs", "dd", "kill", "pkill"]

def is_safe_command(command):
    """Проверяет, безопасна ли команда"""
    for blacklisted in BLACKLIST_COMMANDS:
        if blacklisted in command:
            return False
    return True

def execute_command(command):
    """Выполняет команду, если она безопасна"""
    if not is_safe_command(command):
        logging.warning(f"⚠️ Блокировка команды: {command}")
        return "⛔ Команда запрещена!"

    try:
        proccess = subprocess.Popen(command, shell=True)
        
        # Логируем выполненную команду
        logging.info(f"✅ Выполнено: {command}\n📄 Результат: {output[:200]}")
        
        return proccess
    except Exception as e:
        logging.error(f"❌ Ошибка выполнения: {command} - {str(e)}")
        process = f"Ошибка выполнения команды: {str(e)}"
