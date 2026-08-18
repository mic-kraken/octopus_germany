"""Constants for the Octopus Germany integration."""

DOMAIN = "octopus_germany"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"

# Account/state polling interval. Meter interval data is fetched separately.
UPDATE_INTERVAL = 15  # minutes

# Schema exploration (run once for debugging)
EXPLORE_SCHEMA_ONCE = True  # Set to True to run schema exploration once

# Token management
TOKEN_REFRESH_MARGIN = (
    300  # Refresh token if less than 300 seconds (5 minutes) remaining
)
TOKEN_AUTO_REFRESH_INTERVAL = 50 * 60  # Auto refresh token every 50 minutes

# Debug options
DEBUG_ENABLED = True
LOG_API_RESPONSES = False  # Set to True to log full API responses
LOG_TOKEN_RESPONSES = (
    False  # Set to True to log token-related responses (login, refresh)
)
