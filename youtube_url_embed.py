from urllib.parse import urlparse, parse_qs
    '''A module that generates HTML code for embedding youtube videos from a simple URL'''

def video_id(value):
    query = urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None


def vid_embed(url):

    vid_id = video_id(url)
    return "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/{0}\" frameborder=\"0\" allowfullscreen></iframe>".format(vid_id)
