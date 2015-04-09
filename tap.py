import requests


def latest_release():
    url = 'https://api.github.com/repos/alphagov/govuk_template/releases'
    response = requests.get(url)
    return response.json()[0]


def mustache_asset(release):
    assets_url = release['assets_url']
    response = requests.get(assets_url)
    response.json
    mustache_assets = []
    for asset in response.json():
        if asset['name'].startswith('mustache_govuk_template'):
            mustache_assets.append(asset)

    return mustache_assets[0]


def download(asset):
    local_filename = asset['name']
    response = requests.get(asset['browser_download_url'], stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    return local_filename


def download_mustache():
    release = latest_release()
    mustache = mustache_asset(release)
    download(mustache)
