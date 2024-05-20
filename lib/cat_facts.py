import requests


class CatFacts:

    def __init__(self, requester):
        self.requester = requester


    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.requester.get("https://catfact.ninja/fact")
        return response.json()

# Below code uses above code to get a random generated fact, 
# above code passes a ddetermined test

cat_facts = CatFacts(requests)

print(cat_facts.provide())