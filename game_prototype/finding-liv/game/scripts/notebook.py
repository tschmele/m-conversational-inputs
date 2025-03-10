class Notebook:
    def __init__(self):
        self.topics = {
            "cat":[],
            "grandma":[],
            "Marting":[],
            "Robert":[],
            "Christine":[]
        }


    def add_entry(self, topic, clue):
        text = clue["note_text"]
        self.topics[topic].append(text)
    
    
    def get_topics(self):
        return list(self.topics)
    
    def get_topic(self, topic):
        return self.topics[topic]