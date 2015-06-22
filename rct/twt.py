import twitter

# takes a config dict
def api(config):
    return twitter.Api(**config)

def search(api, query):
    quoted_q = '"' + query + '"'
    quoted_results = api.GetSearch(term=quoted_q)
    if len(quoted_results) == 0:
        return api.GetSearch(term=query)
    return quoted_results

def filter_ats(list_of_statuses):
    return [x for x in list_of_statuses if x.text.encode('utf-8')[0] != '@']

def list_of_statuses_to_str(list_of_statuses):
    return [status_to_str(s) for s in list_of_statuses]

def status_to_str(stats):
    return """@{}
{}
{} favorites
{} retweets
https://twitter.com/{}/status/{}
{}
""".format(
    stats.user.screen_name.encode('utf-8'),
    stats.relative_created_at,
    stats.favorite_count,
    stats.retweet_count,
    stats.user.screen_name.encode('utf-8'), stats.id,
    stats.text.encode('utf-8'),
)
    
