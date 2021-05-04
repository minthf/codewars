class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        
    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return len(self.collection)//self.items_per_page + 1 if len(self.collection)%self.items_per_page > 0 else 0
      

    def page_item_count(self,page_index):
        if self.page_count() < page_index + 1: return -1
        if page_index + 1 == self.page_count():
            return len(self.collection) % self.items_per_page
        return self.items_per_page

    def page_index(self,item_index):
        if item_index + 1 > self.item_count() or item_index + 1 <= 0:
            return -1
        return (item_index + 1) // self.items_per_page