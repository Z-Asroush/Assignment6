import qrcode 
from pyfiglet import Figlet

def show_menu():
    print('1_ add product')
    print('2_ edit product')
    print('3_ delete product')
    print('4_ search')
    print('5_ show list')
    print('6_ QR code')
    print('7_ buy')
    print('8_ exit')

def show_list():
    for i in range (len(product_list)):
        print(product_list[i])
        
def loud():
    print('Louding...')
    myfile=open('Store_data.txt','r')
    data=myfile.read()
    list=data.split('\n')
    for i in range (len(list)):
        detail_list=list[i].split(',')
        mydict={}
        mydict['id']=detail_list[0]
        mydict['name']=detail_list[1]
        mydict['price']=detail_list[2]
        mydict['count']=detail_list[3] 
        product_list.append(mydict)
     
def New_product():
    new_product=input('add id , name , price , count:')
    myfile=open('Store_data.txt','a')
    myfile.write("\n")   
    myfile.write(new_product)
    loud()

def Edit():
     row=int(input('which row?'))
     info=input('id or name or price or count:')
     product_list[row][info]=input()

def Delete():
    row=int(input('which row?'))
    del product_list [row]['id']
    del product_list [row]['name']
    del product_list [row]['price']
    del product_list [row]['count']

def Search():
    key_name=input('name of product?')
    for i in range (len(product_list)):
        if product_list[i]['name']==key_name:
            print(product_list[i])
            break

def QRcode():
    id=int(input('enter product id:'))
    for i in range (len(product_list)):
        if product_list[i]['id']==id:
            id_code=product_list[i]
            break
    img=qrcode.make(id_code)
    img.save('qrcode.png')

def Buy():
    basket=[]
    sum=0
    while input('for exit press 8 for continue press 7:')!="8":
        I=input('enter product id:')
        E=0
        for i in range (len(product_list)):
            if product_list[i]['id']==I:
                E=1
                count=int(input('how many?'))
                if count>int(product_list[i]['count']):
                    print('Not enough!')
                else:
                    basket.append(product_list[i]['name'])
                    basket.append(product_list[i]['price'])
                    basket.append((int(product_list[i]['price']))*count)
                    sum=sum+(int(product_list[i]['price']))*count    
                    product_list[i]['count']=int(product_list[i]['count'])-count
        if E==0:
            print('Not exist!')
    print(basket)
    print('sum=', sum)

def Save():
    myfile=open('Store_data.txt','w')
    for i in range (len(product_list)):
        myfile.write(str(product_list[i]['id']))
        myfile.write(',')
        myfile.write(str(product_list[i]['name']))
        myfile.write(',')
        myfile.write(str(product_list[i]['price']))
        myfile.write(',')
        myfile.write(str(product_list[i]['count']))
        myfile.write('\n')
    myfile.close()

product_list=[]  
loud()
  
f= Figlet(font='standard')
print (f.renderText('Asroush Store'))

show_menu()
choice= int(input('Please choose a number of menu:'))

while True:
    if choice==1:
        New_product()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==2:
        Edit()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==3:
        Delete()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==4:
        Search()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==5:
        show_list()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==6:
        QRcode()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==7:
        Buy()
        show_menu()
        choice= int(input('Please choose a number of menu:'))
    elif choice==8:
        Save()
        exit()