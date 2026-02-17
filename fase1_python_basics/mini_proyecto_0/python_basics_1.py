#Primer script Python
#Simula tiempos de respuesta de un servidor


response_time1 = 120
response_time2 = 200

average = (response_time1 + response_time2) / 2

print("Tiempos de respuesta:", response_time1, response_time2)
print("Promedio:", average)

if average > 150:
    print("Latencia Alta")
else:
    print("Latencia Normal")

cpu_usage = 85
if cpu_usage > 80:
    print("CPU critica")
else:
    print("CPU estable")
    