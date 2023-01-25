#Imports
import math

#Functions

def oposite_side_leg(hip,adj):
    adj_pow = adj**2
    hip_pow = hip**2
    opo = math.sqrt((hip_pow) - (adj_pow))
    opo_pow = opo**2
    response = validation_theorem(hip_pow,opo_pow,adj_pow)
    
    return(hip,opo,adj,response)

def adjacent_side_leg(hip,opo):
    opo_pow = opo**2
    hip_pow = hip**2
    adj = math.sqrt((hip_pow) - (opo_pow))
    adj_pow = adj**2
    response = validation_theorem(hip_pow,opo_pow,adj_pow)
    
    return(hip,opo,adj,response)

def hypotenuse(adj,opo):
    adj_pow = adj**2
    opo_pow = opo**2
    hip = math.sqrt((adj_pow) + (opo_pow))
    hip_pow = hip**2
    response = validation_theorem(hip_pow,opo_pow,adj_pow)
    return(hip,opo,adj,response)

def validation_theorem(hip_pow,opo_pow,adj_pow):
    legs_sum = adj_pow + opo_pow
    print("Legis: "+str(legs_sum))
    print("hip_pow: "+str(hip_pow))
    
    if ((hip_pow != 0) and (opo_pow != 0) and (adj_pow != 0)):
        response = "yes"

    else:
        response = "no"

    return response


#Main
def main():
    hip,adj,opo,resp = adjacent_side_leg(5,5)
    print(hip)
    print(adj)
    print(opo)
    print(resp)
 

#Call the main
if __name__ == '__main__':
    main()
