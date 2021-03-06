# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/none' resources
# =============================================


class GtmMonitorNoneSchema(MetaParser):

    schema = {}


class GtmMonitorNone(GtmMonitorNoneSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/none
    """

    cli_command = "/mgmt/tm/gtm/monitor/none"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
