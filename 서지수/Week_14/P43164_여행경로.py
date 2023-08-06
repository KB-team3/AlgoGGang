def solution(tickets):
    answer=[]
    
    tickets.sort(key=lambda x:(x[0], x[1]))
    
    def dfs(ticket, path):
        if len(ticket)==0:
            return path
        now=path[-1]
        idx=-1
        
        for i in range(len(ticket)):
            if ticket[i][0]==now:
                idx=i
                break
        
        if idx==-1:
            return []
        
        while ticket[idx][0]==now:
            next=dfs(ticket[:idx]+ticket[idx+1:], path+[ticket[idx][1]])
            if next!=[]:
                return next
            idx+=1
        
        return []

    return dfs(tickets, ["ICN"])