# import time
# import threading
# a = [3,4,5,6]

# def square(a):
#     for ele in a:
#         time.sleep(0.2)
#         print(ele**2)

# def cube(a):
#     for ele in a:
#         time.sleep(0.3)
#         print(ele**3)

# t = time.time()
# # square(a)
# # cube(a)

# t = time.time()
# thread1 = threading.Thread(target=square,args=(a,))

# thread2 = threading.Thread(target=cube,args=(a,))


# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# print("Time Taken",time.time()-t)