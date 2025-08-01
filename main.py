from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

def get_signal(pair, timeframe):
    actions = ["BUY", "SELL"]
    entry_price = round(random.uniform(0.8, 1.2), 5)
    confidence = random.randint(60, 95)
    risk = "LOW" if confidence >= 80 else "MEDIUM" if confidence >= 65 else "HIGH"

    analysis = f"Short-term {timeframe} scalping opportunity. Momentum indicators suggest {actions[1] if actions[0] == 'BUY' else 'bearish'} trend continuation."

    return {
        "pair": pair.replace("_", "/"),
        "action": random.choice(actions),
        "entry_price": f"${entry_price}",
        "expiration": f"{timeframe} minutes",
        "confidence": f"{confidence}%",
        "risk_level": risk,
        "analysis": analysis,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    }

@app.route('/get-signal')
def signal():
    pair = request.args.get('pair', 'EURUSD')
    timeframe = request.args.get('timeframe', '1m')
    result = get_signal(pair, timeframe)
    return jsonify(result)

@app.route('/')
def home():
    return "Binary Signal API is running."

if __name__ == '__main__':
    app.run()