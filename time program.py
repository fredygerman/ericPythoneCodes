total_seconds=int(input("what is the number of seconds?: "))
hours=(total_seconds//3600)
minutes=((total_seconds%3600)//60)
seconds=(total_seconds%60)
print("Hours=",hours,"Minutes=",minutes,"Seconds=",seconds)
