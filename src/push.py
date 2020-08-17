import pusher
import config


pusher_client = pusher.Pusher(
  app_id=config.app_id,
  key=config.key,
  secret=config.secret,
  cluster=config.cluster
)


def Push(content: str, author: str, time: str):
    pusher_client.trigger(u'my-channel', u'my-event', {"Content": content, "Author": author, "Time": time})
