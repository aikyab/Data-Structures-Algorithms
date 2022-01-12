stack = deque()
        node = root
        x = y = pred = None
        
        #       3
        #1              4
        #           2
        
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pred and node.val<pred.val:
                y = node
                if not x:
                    x = pred
                else:
                    break
            pred = node
            node = node.right
            
        x.val,y.val = y.val,x.val
            
            
            
#         def inorderTrav(node):
#             nonlocal x,y,pred
#             if not node:
#                 return
#             inorderTrav(node.left)
#             if pred and node.val<pred.val:
#                 y = node
#                 if x:
#                     return
#                 x = pred
#             pred = node
#             inorderTrav(node.right)
#         x = y = pred = None
#         inorderTrav(root)
#         x.val,y.val = y.val,x.val
        
