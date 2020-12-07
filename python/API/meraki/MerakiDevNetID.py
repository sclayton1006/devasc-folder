""" This is the big one, my own API to Meraki, which will pull information
about devices. I will use rich tables to make this a little sexier on the
eye... """

def getMerakiSandboxId():
    from meraki_sdk.meraki_sdk_client import MerakiSdkClient

    key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    meraki = MerakiSdkClient(key)
    orgs = meraki.organizations.get_organizations()

    for org in orgs:
        if org['name'] == "DevNet Sandbox":
            sBox = org['id']
    return sBox

def main():
    from meraki_sdk.meraki_sdk_client import MerakiSdkClient

    key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
    meraki = MerakiSdkClient(key)
    orgs = meraki.organizations.get_organizations()

    for org in orgs:
        if org['name'] == "DevNet Sandbox":
            print(f"The {org['name']} has been found under ID {org['id']}")

if __name__ == "__main__":
    main()
