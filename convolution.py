
def linear(x,h):
    lx=len(x)
    lh=len(h)
    mat=[[0 for i in range(lh+1)] for i in range(lx+1)]
    #print mat
    for i in range(lx+1):
        for j in range(lh+1):
            #print i,j
            if i==0 and j==0:
                mat[i].insert(j,-1)
                #print mat[i][j],mat[i][j+1]
                del mat[i][j+1]
            elif i==0:
                mat[i].insert(j,h[j-1])
                del mat[i][j+1]
            elif j==0:
                mat[i].insert(j,x[i-1])
                #print mat[i][j],mat[i][j+1]
                del mat[i][j+1]
            else:
                #print i,j,mat[i][0]*mat[0][j]
                mat[i].insert(j,mat[i][0]*mat[0][j])
                del mat[i][j+1]
        print mat[i]
    y={2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    exit=False
    for i in range(1,lx+1):
        for j in range(1,lh+1):
            if i!=0 or j!=0:
                yl[i+j]=mat[i][j]
    print yl        
        
                
if __name__=="__main__":
    #x = raw_input("Enter values of x(n){Ex:1,2,3}").split(",")
    x=[1,2,3,1]
    #h = raw_input("Enter values of h(n){Ex:2,3}").split(",")
    h=[2,3,-1,1]
    
    linear(x,h)
    
    
    
