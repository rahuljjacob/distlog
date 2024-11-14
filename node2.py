import threading
import time
import random
from log import generate_info_log, random_log_level, generate_registration_log, generate_warn_log, generate_error_log
from heartbeat import send_heartbeat

def main():
    node_id = "node_02"
    service_name = "Order"

    generate_registration_log(node_id, service_name)

    heartbeat_thread = threading.Thread(target=send_heartbeat, args=(node_id,))
    heartbeat_thread.daemon = True
    heartbeat_thread.start()

    while True:
        log_level = random_log_level()
        log_message = f"Sample log message from {node_id}"
        match log_level:
            case "INFO":
                generate_info_log(node_id, log_level, service_name, log_message)
            case "WARN":
                pass
                generate_warn_log(node_id, log_level, service_name, log_message)
            case "ERROR":
                pass
                generate_error_log(node_id, log_level, service_name, log_message)
        time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    main()
