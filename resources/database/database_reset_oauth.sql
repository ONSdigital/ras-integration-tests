/* Clean OAuth DB */

TRUNCATE public.credentials_oauthuser CASCADE;

TRUNCATE auth.user CASCADE;