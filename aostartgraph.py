def update_cost(h,condition,weight=1):
    main_node=list(condition.keys())
    main_nodes.reverse()
    least_cost={}
    for key in main_node:
        condition=condition[key]
        print(key,',',condition.keys,'>>>',cost(h,condition,weight))
        