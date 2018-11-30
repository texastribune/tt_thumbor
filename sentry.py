

class ErrorHandler(object):
    def __init__(self, config):
        import sentry_sdk

        dsn = config.SENTRY_DSN_URL
        if not dsn:
            raise RuntimeError(
                "If you set USE_CUSTOM_ERROR_HANDLING to True, and you are using thumbor.error_handlers.sentry, " +
                "then you must specify the Sentry DSN using the SENTRY_DSN_URL configuration."
            )

        env = config.SENTRY_ENVIRONMENT or "test"

        self.sentry = sentry_sdk.init(
            dsn=dsn,
            environment=env,
            integrations=[]
        )

    def handle_error(self, context, handler, exception):
        self.sentry.capture_exception(exception)
