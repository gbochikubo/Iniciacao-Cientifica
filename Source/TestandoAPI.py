import twitter


def auth():
    api = twitter.Api(consumer_key='yoH1mnJg8pngB0x1qDLOL8iwc',
                      consumer_secret='BAZtxzHEJWMXVZMksfqT1OaNNnpA3t44ZpzS9UKecdvzGcnxkw',
                      access_token_key='1140943115055972352-r76kodjGmZLjVITk6NhQ06l64qNSjA',
                      access_token_secret='p1K9nbYjmcOfY1hBJTcB4V9gXA1SfxD9bfzPdlb2ecDkS')

    return api


def get_msg():
    api = auth()
    response = api.GetSearch(term='neymar', count=100, since='2015-06-10')
    for r in response:
        print(r.__getattribute__('text'))
        print("\n")


def get_trends():
    api = auth()
    response = api.GetTrendsWoeid(woeid='23424768')
    #response = api.GetTrendsCurrent()
    for r in response:
        print(r)


if __name__ == '__main__':
    get_msg()
    # get_trends()
