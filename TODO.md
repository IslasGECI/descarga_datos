# The Gold

Stop using BITBUCKET_PASSWORD and use BITBUCKET_API_TOKEN instead.

## Plan

### Cycle 1 — Add token reader (🔴 RED → 🟢 GREEN)
- **RED:** Write a failing test for `get_token_from_enviormet_variable()`.
  - *Scenario:* BITBUCKET_API_TOKEN is set in the environment.
  - *Expected:* The function returns the token value.
  - *Fails because:* The function does not exist.
- **GREEN:** Implement the function and export it.
  - Wire it into `DataFile.get_url_to_file()` using the static username
    `x-bitbucket-api-token-auth` and the token, replacing the current
    `{username}:{password}` pattern.
  - Remove `get_password_from_enviormet_variable()` from any production
    call sites, but keep the function and its test alive.
  - This keeps the test suite green while the old code remains untouched.

### Cycle 2 — Remove old credential functions (🔴 RED → 🟢 GREEN)
- **RED:** Remove the two old tests from `test_environment.py`:
  `test_get_user_from_enviorment_variable` and
  `test_get_password_from_enviormet_variable`.
  - *Fails because:* The count of passing tests drops or the old functions
    are no longer covered.
- **GREEN:** Remove the old production functions:
  `get_user_from_enviorment_variable()` and
  `get_password_from_enviormet_variable()`.
  - Clean up `enviroment.py` and its exports in `__init__.py`.
  - Remove `BITBUCKET_USERNAME` and `BITBUCKET_PASSWORD` from
    `docker-compose.yml`.
  - All tests pass with only the token-based auth path remaining.
