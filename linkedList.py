from random import choice

# type node

def new_node(data, next=None):
    return {'data':data, 'next':next}

def get_next(node):
    return node['next']

def set_next(node, next):
    node['next'] = next
    return node

def get_data(node):
    return node['data']

def set_data(node, data):
    node['data'] = data
    return node

def has_next(node):
    return node['next'] != None

# type linkdlist

def new_linkedList(list_nodes = []):
    if len(list_nodes) == 0:
        return {}
    elif len(list_nodes) == 1:
        return {0:new_node(list_nodes[0]['data'])}
    else:
        d = {}
        for i in range(len(list_nodes)-1):
            d[i] = new_node(list_nodes[i]['data'], i+1)
        d[len(list_nodes)-1] = new_node(list_nodes[-1]['data'])
        return d

def size(l):
    return len(l)

def isEmpty(l):
    return len(l)==0

def get(l, index):
    if not isEmpty(l):
        # clé du premier noeud :
        keys = list(set(l.keys()))
        ks = []
        for v in l.values():
            if get_next(v) != None:
                ks.append(get_next(v))
        u = list(set(keys)-set(ks))[0]
        # un autre etap
        i=0
        while True:
            current = l[u]
            u = get_next(current)
            if u == None:
                if i==index:
                    return current['data']
                else:
                    # throw exception
                    return 'error: index out of the list'
            elif i==index:
                return current['data']
            else:
                i += 1
    # throw exception
    return 'error: empty list'

def index_of(l, data):
    if not isEmpty(l):
        # clé du premier noeud :
        keys = list(set(l.keys()))
        ks = []
        for v in l.values():
            if get_next(v) != None:
                ks.append(get_next(v))
        u = list(set(keys)-set(ks))[0]
        i=0
        while True:
            current = l[u]
            u = get_next(current)
            w = get_data(current)
            if w == data:
                return i
            if u == None:
                return -1
            i += 1
    return -1

# add last
def add(l, data):
    if isEmpty(l):
        l[0] = new_node(data)
    else:
        keys = list(set(l.keys()))
        ks = []
        for v in l.values():
            if get_next(v) != None:
                ks.append(get_next(v))
        u = list(set(keys)-set(ks))[0]
        while get_next(l[u]) != None:
            u = get_next(l[u])
        # generer un nouvel indice not in keys : index
        index = choice( list(set(range(max(keys)+2)) - set(keys)) )
        # nouveeau noeud [data , None] 
        node = new_node(data)
        # ajouter nouveel indice cree
        # set_next[l[u], index]
        l[u]['next'] = index
        # ajouter dernir noeud
        l[index] = node
        

# add first
def add_first(l, data):
    if isEmpty(l):
        nd = new_node(data)
        l[0] = nd
    else:
        keys = list(set(l.keys()))
        ks = []
        for v in l.values():
            if get_next(v) != None:
                ks.append(get_next(v))
        u = list(set(keys)-set(ks))[0]
        nd = new_node(data, u)
        i = 0
        while True:
            if i not in l:
                l[i] = nd
                break
            i += 1
        
# add index
def add_at(l, data, index):
    if size(l)-1 < index or 0 > index:
        # trow excption
        print('Error : indice en dehors de la liste')
    elif size(l) == 1:
        nd = new_node(data, l.keys()[0])
        k = 2022 if 2022 not in l else 2021
        l[k] = nd
    else:
        keys = list(set(l.keys()))
        ks = []
        for v in l.values():
            if get_next(v) != None:
                ks.append(get_next(v))
        u = list(set(keys)-set(ks))[0]
        w = None
        i = 0
        while i<=index-1:
            w = u
            u = get_next(l[u])
            i += 1
        nd = new_node(data, u)
        k = 0
        while k in l:
            k += 1
        l[w]['next'] = k
        l[k] = nd
        

# add collection
def add_all(l, c):
    if len(c)>0:
        for e in c:
            add(l, e)

# remove last
def remove_last(l):
    if not isEmpty(l):
        if size(l)==1:
            l={}
        else:
            keys = list(set(l.keys()))
            ks = []
            for v in l.values():
                if get_next(v) != None:
                    ks.append(get_next(v))
            u = list(set(keys)-set(ks))[0]
            w = None
            while has_next(l[u]):
                w = u
                u = get_next(l[u])
            l[w]['next'] = None
            l.pop(u)
    else:
        print('linkedlist is already empty!')
        


# remove first
def remove_first(l):
    if isEmpty(l):
        print('linkedlist is already empty!')
    elif size(l)==1:
        l = {}
    else:
        keys = list(set(l.keys()))
        ks = []
        for v in l.values():
            if get_next(v) != None:
                ks.append(get_next(v))
        u = list(set(keys)-set(ks))[0]
        l.pop(u)


# remove index

# afficher linkedlist
def display_linkedlist(l):
    if isEmpty(l):
        print('empty linkedlist : []')
    else:
        keys = list(set(l.keys()))
        ks = []
        for v in l.values():
            if get_next(v) != None:
                ks.append(get_next(v))
        u = list(set(keys)-set(ks))[0]
        print('linkedlist : ->', sep='', end='')
        while(has_next(l[u])):
            print('[', str(get_data(l[u])), ']->', sep='', end='')
            u = get_next(l[u])
        print('[', str(get_data(l[u])), ']<EOL>', sep='')


if __name__ == '__main__':
    famille = new_linkedList([new_node('bob'), new_node('toto'), new_node('momo'), {'data':'fafa','next':62}, new_node('sami')])
    display_linkedlist(famille)
    remove_last(famille)
    display_linkedlist(famille)
    add_first(famille, 'adam')
    display_linkedlist(famille)
    add_at(famille, 'marshal', 2)
    display_linkedlist(famille)
