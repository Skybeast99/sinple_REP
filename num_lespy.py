num_les = int(input('введите номер урока '))
time1 = (45 * num_les)
time2 = (num_les - 1) * 10
topical_minutes = time1 + time2
time3 = (8.5 * 60)
end_minutes = topical_minutes + time3
hours = int(end_minutes // 60 ) 
minutes = int(end_minutes % 60)
days = int(hours // 24)

if minutes > 9 and hours < 24:
    print (hours, ':', minutes,)
elif minutes < 9 and hours < 24:
    print (hours, ': 0', minutes,)
elif minutes > 9 and hours > 24:
    print (days, ':', hours, ':', minutes,)
else:
    print (days, ':', hours, ': 0', minutes,)
    
