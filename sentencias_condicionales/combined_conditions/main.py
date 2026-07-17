# The item's discount and stock status have been defined
discounted = False
lowStock = True

#Definiendo variable movingProduct
movingProduct = discounted or lowStock

#Definiendo variable promotion
promotion = not discounted and not lowStock

#Imprimiendo mensaje
print(f"Is the item eligible for promotion? {promotion}")