import pickle

# Data to be stored
data = {
    "scenario": """رفتن به سینما
با تعدادی از همکلاسی ها برنامه ریزی می کنید که آخر هفته به سینما بروید 
با هم قرار می گذارید که ساعت پنج بعد از ظهر درب خوابگاه باشید
بنا به دلایلی دیر آماده شده و ساعت پنج و دَه دقیقه بعد از ظهر درب خوابگاه حاضر می شوید
نگهبان خوابگاه می گوید که دوستانتان دَه دقیقه قبل رفتند""",
    "evaluation": """آیا همکلاسی هایتان منظر شما مانده بودند؟
تحقیر همکلاسی:f
بی احترامی به همکلاسی:f
بی توجهی به همکلاسی:f
اقدامی منطقی:t"""
}

# Writing data to a file
with open("data.dat", "wb") as file:
    pickle.dump(data, file)

# Reading data from the file
with open("data.dat", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)