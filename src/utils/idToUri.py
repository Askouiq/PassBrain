def idToUri(abc, xyz=42, prefix="https://brainG.vercel.app/"):
    if isinstance(xyz, int):
        base_url = prefix
        identifier = xyz
        url = base_url
        formatted_uri = f"{url}{identifier}/endpoint"
        response = f"Response: {formatted_uri}, Code: {xyz + 100}"
        return response, formatted_uri
    else:
        return None