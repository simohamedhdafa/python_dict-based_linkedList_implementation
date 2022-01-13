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

def equals(node1, node2):
    return get_data(node1) == get_data(node2)

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

def first_key(l):
    keys = set(l.keys())
    ks = []
    for v in l.values():
        ks.append(get_next(v))
    return list(keys-set(ks))[0]

def get(l, index):
    if not isEmpty(l):
        u = first_key(l)
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
        u = first_key(l)
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
        # 1) nouveeau noeud [data , None] 
        node = new_node(data)

        # 2)
        u = first_key(l)
        while get_next(l[u]) != None:
            u = get_next(l[u])

        # 3)   
        # generer un nouvel indice not in keys : index
        index = choice( list(set(range(max(keys)+2)) - set(keys)) )
        
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
        u = first_key(l)
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
        u = first_key(l)
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
            return True
        else:
            u = first_key(l)
            w = None
            while has_next(l[u]):
                w = u
                u = get_next(l[u])
            l[w]['next'] = None
            l.pop(u)
            return True
    else:
        #print('linkedlist is already empty!')
        return False
        


# remove first
def remove_first(l):
    if isEmpty(l):
        #print('linkedlist is already empty!')
        return False
    else:
        u = first_key(l)
        l.pop(u)
        return True


# remove index
def remove(l, index):
    if isEmpty(l):
        #print("liste vide!")
        return False
    elif index==0:
        # rendre remove_first fct booleenne
        return remove_first(l)
    elif index==size(l)-1:
        # rendre remove_last fct booleenne
        return remove_last(l)
    elif index<0 or index>=size(l):
        #print("indice en dehors de la liste")
        return False
    else:
        v = first_key(l)
        u = get_next(l[v])
        for i in range(1, size(l)-1):
            if i!=index:
                v = u
                u = get_next(l[u])
            else:
                l[v]['next'] = get_next(l[u])
                l.pop(u)
                break
        return True


def remove_all_occ(l, data):
    """supprimer de l toutes les occurences de data"""
    compt = 0
    i_data = index_of(l, data)
    while i_data != -1:
        if remove(l, i_data):
            i_data = index_of(l, data)
            compt +=1
            #display_linkedlist(l)
            if compt >= 10:
                break
    print(compt, 'suppressions effectuees')

def remove_all(l, c):
    """supprimer de l toutes les occurences des data de la sequence c"""
    pass

# to_list
def to_list(l):
    ll = []
    if not isEmpty(l):
        u = first_key(l)
        while has_next(l[u]):
            ll.append(get_data(l[u]))
            u = get_next(l[u])
        ll.append(get_data(l[u]))
    return ll


# afficher linkedlist
def display_linkedlist(l):
    if isEmpty(l):
        print('empty linkedlist : []')
    else:
        u = first_key(l)
        print('linkedlist : ->', sep='', end='')
        while(has_next(l[u])):
            print('[', str(get_data(l[u])), ']->', sep='', end='')
            u = get_next(l[u])
        print('[', str(get_data(l[u])), ']<EOL>', sep='')


if __name__ == '__main__':
    #famille = new_linkedList([new_node('bob'), new_node('toto'), new_node('momo'), {'data':'fafa','next':62}, new_node('sami')])
    famille = new_linkedList([new_node('bob'), new_node('bob'), new_node('bob'), {'data':'bob','next':62}, new_node('bob')])
    #head = first_key
    display_linkedlist(famille)

    remove_all_occ(famille, 'bob')
    display_linkedlist(famille)

    """
    k = to_list(famille)
    print(k)
    print(to_list(new_linkedList()))
    print(to_list(new_linkedList([{'data':'alice', 'next': None}])))
    #print(index_of(famille, 'momo'))
    #remove(famille, 2)
    #display_linkedlist(famille)
    #print(index_of(famille, 'sami'))
    #print(index_of(famille, 'mouad'))
    
    remove_last(famille)
    display_linkedlist(famille)
    add_first(famille, 'adam')
    display_linkedlist(famille)
    add_at(famille, 'marshal', 2)
    display_linkedlist(famille)
    
    famille = new_linkedList([new_node('bob')])
    print(index_of(famille, 'bob'))
    remove(famille, index_of(famille, 'bob'))
    print(index_of(famille, 'bob'))
    
    famille = new_linkedList([new_node('bob')])
    display_linkedlist(famille)
    print(index_of(famille, 'bob'))

    remove(famille, index_of(famille, 'bob'))
    display_linkedlist(famille)
    print(index_of(famille, 'bob'))
    """

