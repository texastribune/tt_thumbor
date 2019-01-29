import sentry_sdk


class ErrorHandler(object):
    def __init__(self, config):
        dsn = config.SENTRY_DSN_URL or None
        env = config.SENTRY_ENVIRONMENT or "test"

        sentry_sdk.init(
            dsn=dsn,
            environment=env,
            integrations=[]
        )

    def handle_error(self, context, handler, exception):
        req = handler.request

        with sentry_sdk.configure_scope() as scope:
            scope.set_extra('Headers', req.headers)
            scope.set_extra('URL', req.full_url())
            scope.set_extra('Context', str(context))
        sentry_sdk.capture_exception(exception)
