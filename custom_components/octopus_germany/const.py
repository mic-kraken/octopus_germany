"""Constants for the Octopus Germany integration."""

DOMAIN = "octopus_germany"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"

# Account/state polling interval. Meter interval data is fetched separately.
UPDATE_INTERVAL = 15  # minutes

# Kraken typically ingests interval readings every 3–4 hours.
MEASUREMENTS_UPDATE_INTERVAL_HOURS = 4
MEASUREMENTS_PAGE_SIZE = 100
MEASUREMENTS_MAX_PAGES = 200
MEASUREMENTS_MIN_INTERVAL_HOURS = 3

# Schema exploration (run once for debugging). Off for normal installs.
EXPLORE_SCHEMA_ONCE = False

# Token management
TOKEN_REFRESH_MARGIN = (
    300  # Refresh token if less than 300 seconds (5 minutes) remaining
)
TOKEN_AUTO_REFRESH_INTERVAL = 50 * 60  # Auto refresh token every 50 minutes

# Debug options
DEBUG_ENABLED = False
LOG_API_RESPONSES = False  # Set to True to log full API responses
LOG_TOKEN_RESPONSES = (
    False  # Set to True to log token-related responses (login, refresh)
)
