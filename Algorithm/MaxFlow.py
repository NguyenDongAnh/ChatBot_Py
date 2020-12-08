from flask_socketio import emit
import time
class Graph: 
   
    def __init__(self,graph): 
        self.graph = graph 
        self. ROW = len(graph) 

    def BFS(self,s, t, parent): 
  
        visited =[False]*(self.ROW) 
          
        queue=[] 
          
        queue.append(s) 
        visited[s] = True
           
        while queue: 
  
            u = queue.pop(0) 
          
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
        if visited[t] :
            v = t
            path = str(t)
            while(v !=  s):
                v = parent[v]
                path = path +">-"+ str(v)
            # time.sleep(0.5)
            emit("new message",{'message' : 'Chọn đường đi: {}'.format(path[::-1]),'tag':"new message"})
            return True  
        else:
            return False
              
      
    def FordFulkerson(self, source, sink): 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 
  
        while self.BFS(source, sink, parent) : 

            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min (path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            max_flow +=  path_flow 
  
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 
            string = '<table><tr>'+'</tr><tr>'.join([''.join(['<td>{:3}</td>'.format(item) for item in row]) for row in self.graph])+'</tr></table>'            
            emit("new message",{'message' : 'Ma trận phần dư: <br>'+string,'tag':"new message"})
            # time.sleep(0.3)
        emit("new message",{'message' : 'Không còn đường đi nữa !','tag':"new message"})
        return max_flow 