import psutil

obj_Disk = psutil.disk_usage('/')

disk_total = int(obj_Disk.total / (1024.0 ** 3))
disk_used = int(obj_Disk.used / (1024.0 ** 3))
disk_free = int(obj_Disk.free / (1024.0 ** 3))
print("Total: %i GB" % disk_total)
print("Used: %i GB" % disk_used)
print("Free: %i GB" % disk_free)
print(f"Percentage: {obj_Disk.percent} %")
