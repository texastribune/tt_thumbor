import sentry_sdk
from sentry_sdk.utils import event_from_exception, exc_info_from_error


class ErrorHandler(object):
    def __init__(self, config):
        dsn = config.SENTRY_DSN_URL
        env = config.SENTRY_ENVIRONMENT or "test"

        if not dsn:
            raise RuntimeError(
                "If you set USE_CUSTOM_ERROR_HANDLING to True, and you are using thumbor.error_handlers.sentry, " +
                "then you must specify the Sentry DSN using the SENTRY_DSN_URL configuration."
            )

        sentry_sdk.init(
            dsn=dsn,
            environment=env,
            integrations=[]
        )

    def handle_error(self, context, handler, exception):
        req = handler.request

        exc_info = exc_info_from_error(exception)

        with sentry_sdk.push_scope():
            event, hint = event_from_exception(exc_info)
            event["request"] = {
                "url": req.full_url(),
                "method": req.method,
                "data": req.arguments,
                "query_string": req.query,
                "headers": req.headers,
                "body": req.body,
            }
            sentry_sdk.capture_event(event, hint=hint)