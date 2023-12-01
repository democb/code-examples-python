from docusign_esign import EnvelopesApi
from flask import session

from ...docusign import create_api_client


class Eg015EnvelopeTabDateController:
    @staticmethod
    def get_args():
        """Get required session arguments"""
        return {
            "account_id": session["ds_account_id"],
            "envelope_id": session["envelope_id"],
            "base_path": session["ds_base_path"],
            "access_token": session["ds_access_token"],
        }

    @staticmethod
    def worker(args):
        """
        1. Call the envelope get method
        """

        # Exceptions will be caught by the calling function
        #ds-snippet-start:eSign15Step2
        api_client = create_api_client(base_path=args["base_path"], access_token=args["access_token"])
        #ds-snippet-end:eSign15Step2
        #ds-snippet-start:eSign15Step3
        envelopes_api = EnvelopesApi(api_client)
        results = envelopes_api.get_form_data(account_id=args["account_id"], envelope_id=args["envelope_id"])
        #ds-snippet-end:eSign15Step3
        return results
