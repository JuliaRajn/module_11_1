from PIL import Image

# Открытие изображения
img = Image.open('image.jpg')

# Создание маски
mask = Image.new("L", img.size, 255)

# Применение эффекта сепии
img_sepia = img.convert("L")
img_sepia = Image.new("RGB", img_sepia.size, (150, 100, 50))
img_sepia.paste(img_sepia, (0, 0), mask)

# Сохранение изображения
img_sepia.save('sepia_image.jpg')

