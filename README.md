# rockimage

## endpoints

- `GET /` Is a Hello World or status check endpoint
- `GET /images` returns a list of images previously upoaded (only available if `ENABLE_API` is `True`)
- `GET /images/$IMAGE_UUID` returns a single image metadata (only available if `ENABLE_API` is `True`)

## config

This API uses env variables for config. They are configured in `rockimage/config`:

- `ENABLE_API` - for enabling certain API endpoints
- `DATABASE_URL` - the database endpoint
