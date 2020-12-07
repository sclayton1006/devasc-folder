def getMerakiSandboxId():

    """ Imports the DevNet organization ID from the DevNet Sandbox. Import the
    function using:

        $ 'from MerakiDevNetID import getMerakiSandboxId as ID'

    I've tried to make the script self-sufficient and it should just work for as
    long as the sandbox is operational - SC """

    from meraki_sdk.meraki_sdk_client import MerakiSdkClient

    key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    meraki = MerakiSdkClient(key)
    orgs = meraki.organizations.get_organizations()

    for org in orgs:
        if org['name'] == "DevNet Sandbox":
            sBox = org['id']
    return sBox

def main():

    """ Imports the DevNet organization ID from the DevNet Sandbox.

    I've tried to make the script self-sufficient and it should just work for as
    long as the sandbox is operational.

        key = 6bec40cf957de430a6f1f2baa056b99a4fac9ea0
        meraki = MerakiSdkClient(key)
        orgs = meraki.organizations.get_organizations()

    SC"""

    from meraki_sdk.meraki_sdk_client import MerakiSdkClient

    key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    meraki = MerakiSdkClient(key)
    orgs = meraki.organizations.get_organizations()

    for org in orgs:
        if org['name'] == "DevNet Sandbox":
            print(f"The {org['name']} has been found under ID {org['id']}")

if __name__ == "__main__":
    main()
