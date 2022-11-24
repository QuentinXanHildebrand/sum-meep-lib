def main():

    f= open("meep.txt", "w")

    f.write("Mep mepp meep")
        
    f.close()

    f = open("meep.txt", "r")
    
    lines = f.read()
    
    print(lines)
    
    f.close()
#____________________________________________________________________________________________________ 

new_list = [23, 'meepy']

new_dictionary = {'mep':'a', 'meepy':'b'}

f_name = "meep.py"

#____________________________________________________________________________________________________
new_list2 = []
for items in new_list:
    new_list2.append(items)
for items in new_dictionary:
    new_list2.append(items)


print(new_list2)
#____________________________________________________________________________________________________
#main()