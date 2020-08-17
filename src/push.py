import pusher
import config

# Setup pusher with config
pusher_client = pusher.Pusher(
  app_id=config.app_id,
  key=config.key,
  secret=config.secret,
  cluster=config.cluster
)


def Push(content: str, author: str, time: str):
    # Push json
    pusher_client.trigger(u'my-channel', u'my-event', {"Content": content, "Author": author, "Time": time})
