#understanding numbers , operators ,printing hello world
#following an excercise in teclado.com for better understanding

print('hello Ronaldyika')


years = (input('years you want to determine the number of days in it: '))
months = years * 12;
weaks = months * 4;
days = weaks * 7;
hours = days * 24;
print('there are '+ months + 'months,' + weaks + 'weaks' + days + 'days and '+ hours +'hours in '+ years+ 'years:' );


#excercise two deals with calculating the area fo a circle

#essential measurements , area, raduis, pi

radius = (input('enter the radius: '));
pi = float(22/7)
r = float(radius)
area = (2*pi*(r**2));
print(area)
print('the area of a circle with ' + str(r) + ' raduis is : '+ str(area))

#calculating area using the pow function

r = int(input('enter radius: '))

pi = int(22/7);

p = (r*pi);
print(p)

R = (pow(r,2))
print(R)
area = p*R

print(area)