import pusher


pusher_client = pusher.Pusher(
  app_id=u'1055958',
  key=u'deca7a171714c942501e',
  secret=u'c2cf232b80b2a8f7106c',
  cluster=u'us3'
)


def Push(content: str, author: str, time: str):
    pusher_client.trigger(u'my-channel', u'my-event', {"Content": content, "Author": author, "Time": time})
