

class ErrorHandler(object):
    def __init__(self, config):
        import sentry_sdk

        dsn = config.SENTRY_DSN_URL or None
        env = config.SENTRY_ENVIRONMENT or "test"

        self.sentry = sentry_sdk.init(
            dsn=dsn,
            environment=env,
            integrations=[]
        )

    def handle_error(self, context, handler, exception):
        self.sentry.capture_exception(exception)
