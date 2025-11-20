#step1 lamda fun step 2 inputs step3 print 
# sqr=side*side
#react=len*wid
#tria=0.5* base* heigth
area_sqr= lambda side: side * side
area_rect=lambda leng,wid: leng * wid
area_tria=lambda base,hgth: 0.5 * base* hgth

side=float(input("Enter the side : "))
leng=float(input("Enter the length: "))
wid=float(input("Enter the width"))
base=float(input("Enter the base"))
hgth=float(input("Enter the height"))

print(area_sqr(side))
print(area_rect(leng,wid))
print(area_tria(base,hgth))
