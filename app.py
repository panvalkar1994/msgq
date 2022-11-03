from q.Queue import Queue

class Message:
    def __init__(self, name, args) -> None:
        self.name = name
        self.args = args


class Hook:

    def __init__(self, name, method) -> None:
        self.name = name
        self.method = method

    def call(self, args):
        # Todo:Improvement needed
        self.method(args)


def producer(q: Queue, msg: str):
    q.push(msg)


def consumer(hooks: list[Hook], msg: Message):
    for hook in hooks:
        if msg.name == hook.name:
            hook.call(msg.args)

def consume_queue(q:Queue, hooks:list[Hook]):
    while not q.isEmpty():
        msg = q.pop()
        consumer(hooks, msg)


def hello(name: str):
    print(f'hello {name}')


def bye(name: str):
    print(f'bye, {name}!')


hooks: list[Hook] = [
        Hook('hi', hello), 
        Hook('Hi', hello), 
        Hook('hello', hello),
        Hook('bye', bye),
        Hook('tata', bye)
    ]

messages = [
    Message('hi', {'name':'vaibhav'}),
    Message('hello', {'name':'vaibhav'}),
    Message('Hi', {'name':'vaibhav'}),
    Message('bye', {'name':'vaibhav'}),
    Message('tata', {'name':'vaibhav'}),
]

def main():
    # load msg
    q = Queue()
    for msg in messages:
        q.push(msg)
    consume_queue(q, hooks)
    
    
main()
