def extract_features(url):
    url_length = len(url)
    has_https = 1 if "https" in url else 0
    dots = url.count(".")

    return [url_length, has_https, dots]
