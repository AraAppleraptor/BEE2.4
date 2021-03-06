"""Run the BEE2 application."""
from multiprocessing import freeze_support, set_start_method
import os
import sys

# We need to add dummy files if these are None - MultiProccessing tries to flush
# them.

if sys.stdout is None:
    sys.stdout = open(os.devnull, 'w')
if sys.stderr is None:
    sys.stderr = open(os.devnull, 'w')
if sys.stdin is None:
    sys.stdin = open(os.devnull, 'r')

if sys.platform == "darwin":
    # Disable here, can't get this to work.
    sys.modules['pyglet'] = None

if not sys.platform.startswith('win'):
    set_start_method('spawn')
freeze_support()

if __name__ == '__main__':
    import srctools.logger
    import tk_tools
    import utils

    if len(sys.argv) > 1:
        log_name = app_name = sys.argv[1].lower()
        if app_name not in ('backup', 'compilepane'):
            log_name = 'bee2'
    else:
        log_name = app_name = 'bee2'

    # We need to initialise logging as early as possible - that way
    # it can record any errors in the initialisation of modules.
    utils.fix_cur_directory()
    LOGGER = srctools.logger.init_logging(
        str(utils.install_path(f'logs/{log_name}.log')),
        __name__,
        on_error=tk_tools.on_error,
    )
    utils.setup_localisations(LOGGER)

    LOGGER.info('Arguments: {}', sys.argv)
    LOGGER.info('Running "{}":', app_name)

    if app_name == 'bee2':
        import BEE2
    elif app_name == 'backup':
        import backup
        backup.init_application()
    elif app_name == 'compilepane':
        import CompilerPane
        CompilerPane.init_application()
    else:
        raise ValueError(f'Invalid component name "{app_name}"!')

    # Run the TK loop forever.
    tk_tools.TK_ROOT.mainloop()

