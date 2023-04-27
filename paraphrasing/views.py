from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello world")

from django.http import JsonResponse
from nltk.tree import Tree

# def paraphrase(request):
#     tree_str = request.GET.get('tree', '')
#     limit = int(request.GET.get('limit', 20))
#     tree = Tree.fromstring(tree_str)
#     np_subtrees = list(tree.subtrees(filter=lambda t: t.label() == 'NP'))
#     paraphrases = []
#     for i, np1 in enumerate(np_subtrees):
#         for np2 in np_subtrees[i+1:]:
#             new_tree = tree.copy(deep=True)
#             np1_index = list(new_tree.treepositions(np1))[0]
#             np2_index = list(new_tree.treepositions(np2))[0]
#             new_tree[np1_index], new_tree[np2_index] = new_tree[np2_index], new_tree[np1_index]
#             paraphrases.append(new_tree.pformat())
#             if len(paraphrases) >= limit:
#                 break
#         if len(paraphrases) >= limit:
#             break
#     return JsonResponse({'paraphrases': paraphrases})


from django.http import JsonResponse
from nltk.tree import Tree

def paraphrase(request):
    tree_str = request.GET.get('tree', '')
    limit = int(request.GET.get('limit', 20))
    tree = Tree.fromstring(tree_str)
    np_subtrees = list(tree.subtrees(filter=lambda t: t.label() == 'NP'))
    paraphrases = []
    for i, np1 in enumerate(np_subtrees):
        if len(np1.leaves()) == 1:
            continue  # skip leaf nodes
        for np2 in np_subtrees[i+1:]:
            if len(np2.leaves()) == 1:
                continue  # skip leaf nodes
            new_tree = tree.copy(deep=True)
            np1_index = list(new_tree.treepositions(np1))[0]
            np2_index = list(new_tree.treepositions(np2))[0]
            new_tree[np1_index], new_tree[np2_index] = new_tree[np2_index], new_tree[np1_index]
            paraphrases.append(new_tree.pformat())
            if len(paraphrases) >= limit:
                break
        if len(paraphrases) >= limit:
            break
    return JsonResponse({'paraphrases': paraphrases})