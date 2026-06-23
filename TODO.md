# The Gold

Stop using BITBUCKET_PASSWORD and use BITBUCKET_API_TOKEN instead.

## Status: ✅ Complete

- `DataFile.get_url_to_file()` authenticates with `{BITBUCKET_EMAIL}:{BITBUCKET_API_TOKEN}`
  against `api.bitbucket.org`.
- `get_token_from_environment_variable()` and `get_email_from_environment_variable()`
  are exported and tested.
- Old functions `get_user_from_environment_variable()` and
  `get_password_from_environment_variable()` have been removed, along with their tests
  and the `BITBUCKET_USERNAME`/`BITBUCKET_PASSWORD` environment variables from
  `docker-compose.yml`.
