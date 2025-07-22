productName = "Camiseta"
priceOriginal = 50.00
descont = 0.2
print("Calculadora de desconto")
print(f"Produto: {productName}")
print(f"Preço original: R${priceOriginal:.2f}")
priceDiscounted = priceOriginal * descont
print(f"Preço com desconto:", priceOriginal - priceDiscounted)