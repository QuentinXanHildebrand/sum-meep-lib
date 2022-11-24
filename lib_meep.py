import meep
import time

print("using", meep.f_name)

print(meep.new_list[0])

print(meep.new_dictionary['mep'])

print('so im going to add a new list of stuff', meep.new_list2)
for items in meep.new_list2:
    print(items)
    time.sleep(0.5)


meep.main()