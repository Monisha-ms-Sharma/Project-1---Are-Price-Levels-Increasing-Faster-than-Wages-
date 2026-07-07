from src.data_loader import load_all_datasets
from src.report_parser import parse_report
from src.preprocessing import preprocess

datasets = load_all_datasets()

for name, df in datasets.items():

    print(f"\n{'='*70}")
    print(name.upper())
    print('='*70)

    df = parse_report(df)
    df = preprocess(df)

    print(df.head())
    print()
    print(df.dtypes)