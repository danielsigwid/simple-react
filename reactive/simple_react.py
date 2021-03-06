from charms.reactive import when, when_not, set_state
from charmhelpers.core.hookenv import status_set


@when_not('simple-react.installed')
def install_simple_react():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    print("I hope this is logged!")
    status_set('active', 'Install done')
    set_state('simple-react.installed')
