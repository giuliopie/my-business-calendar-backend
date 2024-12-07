# Third-party imports
from flask import Flask, jsonify
from flask_cors import CORS

# Local application imports
from helper import logger
from api import APIExecutors

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "http://localhost:3001"]}})

#retrieve events from Google Calendar
@app.route('/api/fetch-g-events', methods=['GET'])
def fetch_google_calendar_events():
    logger.info("API '/api/fetch-g-events' called.")
    try:
        logger.info("Events fetched!")
        APIExecutors.fetch_g_events()
        return jsonify({"status": "ok", "details": "Events fetched"}), 200
    except Exception as e:
        logger.error(f"Errore durante il recupero degli eventi: {e}")
        return jsonify({"error": "Failed to fetch events from Google calendar", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)