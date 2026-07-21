


#Project 3: Mini Shopping Cart
#Author: [Gül İfdal ALDEMİR]
#Date: 17 July 2026

print()
print("Welcome to the Mini Shopping Cart!")

# Ürünleri ve fiyatlarını saklamak için boş listeler oluşturuyoruz
products = []
prices = []

# Kullanıcı "done" yazana kadar ürünleri ve fiyatlarını girmeye devam edebilir
while True:
    # Kullanıcıdan ürün adı alıyoruz
    product = input("Enter the product name: ")
    # Eğer kullanıcı "done" yazarsa döngüden çıkıyoruz
    if product == "done":
        break
    # Kullanıcıdan ürün fiyatını alıyoruz ve float tipine çeviriyoruz
    price = float(input("Enter the product price: "))
    # Ürün ve fiyatı listelere ekliyoruz
    prices.append(price)
    # Ürün adını da ürünler listesine ekliyoruz
    products.append(product)

print()
# Kullanıcıya alışveriş sepetini ve toplam maliyeti gösteriyoruz
print("Your shopping cart")
#Her ürün ve fiyatını sırası ile listeliyoruz
for i in range(len(products)):
    print(f"- {products[i]}: ${prices[i]:.2f}")
#Tüm ürünlerin fiyatlarını toplayarak toplam maliyeti hesaplıyoruz ve kullanıcıya gösteriyoruz
print(f"Total cost: ${sum(prices):.2f}") 

