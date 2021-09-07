import os

from sanic import Sanic, Request
from sanic import response
from sanic.log import logger


app = Sanic("balancer-app")
counter = 0
cdn_adress = os.getenv('CDN_HOSTS', '127.0.0.0')
cdns = [f'http://{cdn_adress}:800{i}' for i in range(0,int(os.getenv('CDN_COUNT', 10)))]


@app.get("/")
async def hello_world(request: Request) -> response.HTTPResponse:
    video: str = request.args.get('video')
    if video is None:
        return response.json({'error': 'parameter video is required'}, 400)
    global counter
    counter += 1
    if counter == 10:
        counter = 0
        logger.info('redirect to origin')
        return response.redirect(video, status=301)
    redirect_url = cdns[counter // len(cdns)] + '/video' + video.split('video')[1]
    logger.info(f'redirect to cdn {redirect_url}')
    return response.redirect(redirect_url, status=301)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8010, debug=False)
