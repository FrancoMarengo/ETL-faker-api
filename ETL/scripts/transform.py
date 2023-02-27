from pyspark.sql import SparkSession

# Se crea una SparkSession para comenzar a trabajar con los datos.
spark = SparkSession.builder.getOrCreate()

# Se define un esquema para que Spark no infiere tipos de datos correctamente desde un CSV file.
schema = StructType([
      StructField("id", StringType(), nullable=False),
      StructField("firstname", StringType(), nullable=False),
      StructField("lastname", StringType(), nullable=False),
      StructField("email", StringType(), nullable=False),
      StructField("phone", StringType(), nullable=False),
      StructField("birthday", StringType(), nullable=False),
      StructField("gender", StringType(), nullable=False),
      StructField("address", StructType([
        StructField("id", IntegerType(), nullable=False),
        StructField("street", StringType(), nullable=False),
        StructField("streetName", StringType(), nullable=False),
        StructField("buildingNumber", StringType(), nullable=False),
        StructField("city", StringType(), nullable=False),
        StructField("zipcode", StringType(), nullable=False),
        StructField("country", StringType(), nullable=False),
        StructField("county_code", StringType(), nullable=False),
        StructField("latitude", IntegerType(), nullable=False),
        StructField("longitude", IntegerType(), nullable=False)]
        )
      ),
      StructField("website", StringType(), nullable=False),
      StructField("image", StringType(), nullable=False)]
    )

# Crea un data frame con los datos del archivo 'persons.csv'.
persons_df = spark.read.csv("data/landing/persons.csv")