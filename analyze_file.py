import pandas



def to_int(val):
    return 0 if val.lower() == 'nan' else int(val)


def clean_and_convert_values(value):
    if isinstance(value, str):
        try:
            return to_int(value)
        except ValueError:
            return to_int(value[:-1])
    elif isinstance(value, float):
        return 0 if value == 'NaN' else int(value)
    else:
        return value


def main(file):
    climate_data = pandas.read_csv(file)
    print("File have been loaded into dataframe. Apply transformations...")
    
    col_dry_temp = climate_data["HourlyDryBulbTemperature"].dropna()
    climate_data = climate_data.loc[climate_data["HourlyDryBulbTemperature"].isin(col_dry_temp)]

    col_dry_temp = col_dry_temp.apply(clean_and_convert_values)
    max_temp = col_dry_temp.max()
    climate_data["HourlyDryBulbTemperature"] = col_dry_temp

    max_temp_record = climate_data.loc[climate_data["HourlyDryBulbTemperature"] == max_temp]
    print(max_temp_record)
    

    
# if __name__ == "__main__":
    
#     file = 'downloads/86624099999.csv'
#     main(file)