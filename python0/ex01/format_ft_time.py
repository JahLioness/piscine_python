import time

start = time.time()
struct_time = time.localtime(start)
formatted_time = time.strftime("%B %d %Y", struct_time)  
print(f"Seconds since January 1, 1970: {round(start, 4):,} or {start:.2e} in scientific notation\n{formatted_time}")