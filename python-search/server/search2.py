class Item:
    def __init__(self, name, price, keywords):
        self.name = name
        self.price = price
        self.keywords = keywords

db = [
    Item('Apple', 1, ['apple', 'fruit', 'food', 'healthy']),
    Item('Bike', 80, ['healthy', 'exercise', 'moving', 'travel', 'bike']),
    Item('Asus Vivobook Laptop', 550, ['work', 'computer', 'expensive', 'laptop', 'luxury', 'asus', 'office', 'tech']),
    Item('Chromebook', 90, ['school', 'computer', 'cheap', 'laptop', 'chromebook', 'tech']),
    Item('Running Shoes', 45, ['exercise', 'healthy', 'travel', 'running', 'shoes']),
    Item('T-shirt', 10, ['shirt', 't-shirt', 'clothing', 'comfy', 'cotton']),
    Item('Painting of a Lake', 30, ['painting', 'art', 'luxury', 'decoration', 'decor', 'paint', 'nature', 'water', 'lake']),
    Item('10 Planks of Plywood', 20, ['wood', 'construction', 'work', 'plywood', 'planks']),
    Item('Soap', 0.75, ['soap', 'hygeine', 'germs', 'healthy']),
    Item('Pencil Sharpener', 8, ['pencil' 'sharpener', 'work', 'office', 'school']),
    Item('Deck of Cards', 4, ['cards', 'fun', 'game', 'relaxing']),
    Item('World Map', 9, ['world', 'map', 'learning', 'office', 'geography', 'school']),
    Item('The Sorcerers Stone', 5, ['book', 'harry', 'potter', 'rowling', 'magic', 'learning', 'reading', 'relaxing']),
    Item('Computer Mouse', 1.50, ['mouse', 'computer', 'accessory', 'work', 'office']),
    Item('DC Motor 6v', 2, ['electronics', 'motor', 'mechanical']),
    Item('Beanbag Chair', 28, ['chair', 'furniture', 'comfy', 'relaxing']),
    Item('Samsung S8', 120, ['phone', 'android', 'google', 'samsung', 'mobile', 'tech', 'computer']),
    Item('Stone Elephant Carving', 16, ['stone', 'carving', 'elephant', 'animal', 'decor', 'decoration']),
    Item('iPhone 6', 90, ['phone', 'computer', 'mobile', 'apple', 'tech']),
    Item('Bedside Lamp', 15, ['furniture', 'lamp', 'light', 'bedside', 'bedroom', 'reading'])
]

def get_rank_and_index (search_words, db_index):
    score = 0
    add_value = 0
    index = 0
    if len(search_words) > 1:
        for word in range(len(search_words)):
            if word == 1:
                add_value = 1
            else:
                add_value = 0.25
            for keyword in db_index.keywords:
                if search_words[word] == keyword:
                    score += add_value
                    index = db.index(db_index)
    else:
        add_value = 1
        for word in range(len(search_words)):
            for keyword in db_index.keywords:
                if search_words[word] == keyword:
                    score += add_value
                    index = db.index(db_index)
    if score > 0:
        return [score, index]

def sort_by_rank(query, minimum_score=1):
    if query == 'all' or query == 'catalog':
        final_array = []
        for item in db:
            final_array.append(f'{item.name}:${item.price}')
    else:
        mod_query = query.split()
        result_array = []
        index_rank_pairs = {}
        no_fuck_up = 0.00001
        for item in db:
            x = get_rank_and_index(mod_query, item)
            if (x != None):
                for result in result_array:
                    if result[0] == x[0]:
                        x[0] += no_fuck_up
                        no_fuck_up += 0.00001
                if x[0] >= minimum_score:
                    result_array.append(x)
                    index_rank_pairs[x[1]] = x[0]
        just_ranks = []
        final_array = []
        for item in result_array:
            just_ranks.append(item[0])
        sorted_ranks = sorted(just_ranks, reverse=True)
        key_list = list(index_rank_pairs.keys())
        val_list = list(index_rank_pairs.values())
        for sorted_item in sorted_ranks:
            db_index = key_list[val_list.index(sorted_item)]
            final_array.append(f'{db[db_index].name}:${db[db_index].price}')
    return ','.join(final_array)

print(sort_by_rank('apple phone', 1.25))