import json
import random
import time
from datetime import datetime
import os

# Create the logs folder if it doesn't exist
os.makedirs('logs', exist_ok=True)
LOG_FILE = 'logs/security_events.log'

# Fake data to make the logs look real
IP_ADDRESSES = ['192.168.1.15', '10.0.0.42', '172.16.2.8', '203.0.113.50', '198.51.100.22']
USERS = ['admin', 'root', 'jsmith', 'guest', 'backup_svc']
EVENT_TYPES = [
    ('login_success', 40),          # Normal behavior (40% chance)
    ('web_traffic', 30),            # Normal behavior (30% chance)
    ('login_failed', 20),           # Suspicious: Might be a brute-force attack (20% chance)
    ('sql_injection_attempt', 10)   # Highly Suspicious: Hacker trying to steal data (10% chance)
]

def generate_log():
    # Pick a random event based on the weights above
    events, weights = zip(*EVENT_TYPES)
    event = random.choices(events, weights=weights)[0]
    
    # Build the base log structure
    log_entry = {
        "@timestamp": datetime.utcnow().isoformat() + "Z",
        "source_ip": random.choice(IP_ADDRESSES),
        "username": random.choice(USERS),
        "event_action": event,
    }

    # Add specific details based on the type of event
    if event == 'sql_injection_attempt':
        log_entry['status'] = 'blocked'
        log_entry['severity'] = 'high'
        log_entry['payload'] = "SELECT * FROM users WHERE id = 1 OR 1=1--"
    elif event == 'login_failed':
        log_entry['status'] = 'failed'
        log_entry['severity'] = 'medium'
    else:
        log_entry['status'] = 'success'
        log_entry['severity'] = 'low'

    return log_entry

print(f"Starting simulated attack traffic... Writing logs to {LOG_FILE}")
print("Press Ctrl+C to stop the script.")

try:
    # Open the file and continuously write fake logs to it
    with open(LOG_FILE, 'a') as f:
        while True:
            log = generate_log()
            f.write(json.dumps(log) + '\n')
            f.flush() # Ensure it writes immediately
            
            # Wait between 0.5 and 2 seconds before the next log
            time.sleep(random.uniform(0.5, 2.0))
except KeyboardInterrupt:
    print("\nAttack simulation stopped.")
