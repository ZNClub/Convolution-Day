### linear convolution by matrix method
def linear(x,h):
    ### get length of x(n)
    lx=len(x)
    
    ### get length of h(n)
    lh=len(h)
    
    ### create lx+1 x lh+1 matrix 
    mat=[[0 for i in range(lh+1)] for i in range(lx+1)]
    #print mat
    
    ### begin to fill matrix
    for i in range(lx+1):
        for j in range(lh+1):
            #print i,j
            
            ### top left corner is not required. Hence initialized it with -1
            if i==0 and j==0:
                mat[i].insert(j,-1)
                #print mat[i][j],mat[i][j+1]
                del mat[i][j+1]
            
            ### first row : insert values of h(n)
            elif i==0:
                mat[i].insert(j,h[j-1])
                del mat[i][j+1]
                
            ### first column : insert values of x(n)
            elif j==0:
                mat[i].insert(j,x[i-1])
                #print mat[i][j],mat[i][j+1]
                del mat[i][j+1]
                
            ### for all other entries, val = mat[first_row][current_colum]*mat[first_column][current_row]
            else:
                #print i,j,mat[i][0]*mat[0][j]
                mat[i].insert(j,mat[i][0]*mat[0][j])
                del mat[i][j+1]
        ### display matrix row by row
        #print mat[i]
        print(mat[i])
    
    ### initialize output response y(n)
    y={2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    
    ### calculate each value of y(n) from matrix
    for i in range(1,lx+1):
        for j in range(1,lh+1):
            if i!=0 or j!=0:
                
                y[i+j]=mat[i][j]
                #print y[i+j],i,j
    print(y)
    return

def circular(x,h):
    lx = len(x)
    lh = len(h)
    if lx>lh:
        d=lx-lh
        for i in range(d):
            h.append(0)
    elif lh>lx:
        d=lh-lx
        for i in range(d):
            x.append(0)
    print(x,h)
    
    return
    
        
### start point of program
#if __name__=="__main__":
### Read values of input response x(n) from user
#x = raw_input("Enter values of x(n){Ex:1,2,3}").split(",")
x=[1,2,3,1]

### Read values of impulse response h(n) from user
#h = raw_input("Enter values of h(n){Ex:2,3}").split(",")
h=[2,3,-1]

### perform linear convolution
#linear(x,h)

### perform linear convolution
circular(x,h)
    
    
