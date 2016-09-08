### LINEAR AND CIRCULAR CONVOLUTION 
def reverse(arg):
    if isinstance(arg,list):
        arg.reverse()
        return arg
    return

def right_shift(rh):    
    temp=[]
    lrh = len(rh)
    for i in range(lrh):
        if i==0:
           temp.append(rh[-1])
        else:
            temp.append(rh[i-1])
    #print(rh,temp)
    return temp

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
        #print(mat[i])
    
    ### initialize output response y(n)
    y={2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    
    ### calculate each value of y(n) from matrix
    for i in range(1,lx+1):
        for j in range(1,lh+1):
            if i!=0 or j!=0:
                
                y[i+j]=mat[i][j]
                #print y[i+j],i,j
    print("linear convolution= ",y)
    return
    

def circular(x,h):
    lx = len(x)
    lh = len(h)
    
    if lx>lh:
        d=lx-lh
        for i in range(d):
            h.append(0)
        lh = len(h)
    elif lh>lx:
        d=lh-lx
        for i in range(d):
            x.append(0)
        lx = len(x)
    #print(x,h)
    
    
    #mat_h=[[0 for i in range(lh)] for j in range(lh)]
    mat_h=[]
    #print(mat_h)
    
    ### form mat h
    
    rh=reverse(h)
    #print(rh)
    
    ### form matrix by circular right shift each row in each iteration
    rh=right_shift(rh)
    mat_h.append(rh)
    for i in range(lh):
        
        if i==lh-1:
            break
        else:
            rh=right_shift(rh)
            mat_h.append(rh)
    #print(mat_h)
    #result_in_json("x(n)",x,False)
    #result_in_json("h(n)",h,True)
    #result_in_json("matrix_h",mat_h)
    
    ### matrix multiplication
    result=[]
    for i in range(lx):
        temp=0
        for j in range(lx):
            temp+=mat_h[i][j]*x[j]
        result.append(temp)
    print("circular convolution= ",result)

### start point of program
#x = raw_input("Enter values of x(n){Ex:1,2,3}").split(",")
x=[1,2,3,1]

### Read values of impulse response h(n) from user
#h = raw_input("Enter values of h(n){Ex:2,3}").split(",")
h=[4,3,2,2]

### perform linear convolution
linear(x,h)

### perform linear convolution
circular(x,h)
    
    
