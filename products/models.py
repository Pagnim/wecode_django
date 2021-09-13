from django.db import models

class Menu(models.Model):
	name = models.CharField(max_length = 20)
	
	class Meta:
		db_table = 'Menu'

class Category(models.Model):
	Category_name = models.CharField(max_length = 20)
	name  = models.ForeignKey('Menu', on_delete=models.CASCADE)

	class Meta:
		db_table = 'Category'

class products(models.Model):
	korean_name  = models.CharField(max_length = 100)
	english_name = models.CharField(max_length = 100)
	description  = models.TextField()
	Category 	 = models.ForeignKey('Category', on_delete=models.CASCADE)
	nutrition 	 = models.ForeignKey('nutrition', on_delete=models.CASCADE)

	class Meta:
		db_table = 'products'

class nutrition(models.Model):
	one_serving_kcal = models.DecimalField(max_digits = 6 , decimal_places = 2)
	sodium_mg 		 = models.DecimalField(max_digits = 6 , decimal_places = 2)
	saturated_fat_g  = models.DecimalField(max_digits = 6 , decimal_places = 2)
	sugars_g		 = models.DecimalField(max_digits = 6 , decimal_places = 2)
	protein_g 		 = models.DecimalField(max_digits = 6 , decimal_places = 2)
	caffeine_mg 	 = models.DecimalField(max_digits = 6 , decimal_places = 2)
	size_ml 		 = models.CharField(max_length = 20)
	size_fluid_ounce = models.CharField(max_length = 20)

	class Meta:
		db_table = 'nutrition'

class image_url(models.Model):
	image_url  = models.CharField(max_length = 2000)
	products   = models.ForeignKey('products', on_delete=models.CASCADE)

	class Meta:
		db_table = 'image'

class allergy_products(models.Model):
	allergy_id    = models.ForeignKey('allergy', on_delete=models.CASCADE)
	product_id    = models.ForeignKey('products', on_delete=models.CASCADE)

	class Meta:
		db_table = 'allergy_products'

class allergy(models.Model):
	name   = models.CharField(max_length = 45)

	class Meta:
		db_table = 'allergy'