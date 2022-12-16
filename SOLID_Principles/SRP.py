#Single-responsibility principle

def get_max(list_):
    return max(list_)

def get_last(list_):
    return list_[len(list_)-1]

def main(list_):
    print(f"the max of the list is {get_max(list_)}")
    print(f"the last item in the list is {get_last(list_)}")
    
main([1,2,8,4,5])