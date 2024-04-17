import pandas as pd

pdf_file = input("PDF File= ")
def combine_first_names_by_family(pdf_file):
  """
  This function takes a PDF file path and returns a dictionary where keys are 
  family last names and values are lists of first names for that family.

  Args:
      pdf_file (str): The path to the PDF file.

  Returns:
      dict: A dictionary mapping family last names to lists of first names.
  """
  
  # Assuming the PDF can be parsed into a pandas dataframe using a library like Camelot
  df = pd.read_hdf(pdf_file)

  # Extract last names and addresses (assuming they're in separate columns)
  last_names = df["Last Name"].tolist()
  addresses = df["Address"].tolist()

  # Create a dictionary to store families
  families = {}

  # Loop through each row in the dataframe
  for i in range(len(last_names)):
    last_name = last_names[i]
    address = addresses[i]

    # If address is blank, assume it's a child and add name to current family
    if not address:
      if last_name in families:
        families[last_name].append(df.loc[i, "First Name"])
      else:
        families[last_name] = [df.loc[i, "First Name"]]
    # Otherwise, create a new family entry
    else:
      families[last_name] = [df.loc[i, "First Name"]]

  return families

# Example usage (assuming your PDF is named "families.pdf")
families_dict = combine_first_names_by_family("families.pdf")

# Print the resulting dictionary
for family_name, first_names in families_dict.items():
  print(f"{family_name}: {', '.join(first_names)}")
