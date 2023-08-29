from crenata.application.error.handler import ErrorHandler

error_handler = ErrorHandler()


@error_handler.handle_this_exception(Exception)
async def handle_exception():
    ...
