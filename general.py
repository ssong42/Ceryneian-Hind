import  requests
import  os
import  argparse

if __name__ == "__main__":
    base_url = "https://api.intra.42.fr"
    UID = "96ae013feb88e431c4387eb6ac3647fce7812c730e94b3670d10446d55885894"
    SECRET = "71f166ac9494721d3152c4e4b7fdeec04bf28293ced373e642ca4d534e496c18"
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest = "filename")
    args = parser.parse_args()
    auth_resp = requests.post("https://api.intra.42.fr/oauth/token",
            data = {
                "grant_type" : "client_credentials",
                 "client_id" : UID,
                 "client_secret" : SECRET
                 }).json()
    token = auth_resp["access_token"]
    with open(args.filename) as file:
        usernames = file.readlines()
        for username in usernames:
            location = requests.get(f"{base_url}/v2/users/{username.strip()}/locations",
                headers={"Authorization": f"Bearer {token}"}).json()
            if location:
                print(location[0]["host"])
            else:
                print("Incorrect User")
