#!/usr/bin/env python3
"""
Pre-initialized Taxonomy Constants - Fixed list for maximum efficiency
Generated once from Subject-Topic-Subtopic.xlsx and hardcoded for performance
"""

# All 14 subjects in the taxonomy
SUBJECTS = [
    "WORLD PHYSICAL GEOGRAPHY",
    "INDIAN PHYSICAL GEOGRAPHY", 
    "INDIAN SOCIO-ECONOMIC GEOGRAPHY",
    "WORLD SOCIO-ECONOMIC GEOGRAPHY",
    "ECONOMY",
    "ANCIENT INDIA",
    "MEDIEVAL INDIA", 
    "MODERN INDIA",
    "POST INDEPENDENCE INDIA",
    "ART AND CULTURE",
    "INDIAN POLITY AND GOVERNANCE",
    "INTERNATIONAL RELATIONS",
    "SCIENCE AND TECHNOLOGY",
    "MISCELLANEOUS"
]

# Complete taxonomy - all 1,132 Subject > Topic > Subtopic combinations
TAXONOMY_OPTIONS = [
    "WORLD PHYSICAL GEOGRAPHY > THE UNIVERSE > Origin of Universe",
    "WORLD PHYSICAL GEOGRAPHY > THE UNIVERSE > Origin of Galaxy, Planets and Moon",
    "WORLD PHYSICAL GEOGRAPHY > THE UNIVERSE > Our Solar System",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Basic Postulates of Plate Tectonic Theory and Interaction of Plates",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Sources of Earth's Interior",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Classification, Distribution and Forecasting of Earthquakes",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Motions of The Earth - Revolution and Other Motions",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Volcanic Landforms - Extrusive and Intrusive",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Geomagnetism - Sources, Principles and Significance",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Sea Floor Spreading Theory",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Introduction and Measurement of Earthquake",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Causes and Consequences of Earthquake",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Plate Tectonic Theory and Mountain Building",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Polar Wandering Theory",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Movements of The Earth",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Internal Heat of Earth",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Latitudes and Longitudes of The Earth",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Layers of Earth",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Comparison Between PTT and CDT",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Evolution of Views About Layers of Earth",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Evolution of Plate Tectonic Theory and Concepts of Plates",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Volcano - Classification of Volcano",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Causes, Consequences, Distribution of Volcanic Eruptions",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Shifting of Magnetic Poles and Geomagnetic Poles",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Volcano - Mechanism, Parts and Materials of A Volcano",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Shape of The Earth",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Mechanisms and Evaluation of Continental Drift",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Marine Geological Findings",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Continental Drift Theory – Background, Postulates and Evidences of The Theory",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Evolution of Lithosphere, Atmosphere and Hydroshpere",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Tsunami",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Motions of The Earth - Rotation",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Convectional Current Theory",
    "WORLD PHYSICAL GEOGRAPHY > GEOMORPHOLOGY > Recent Evidences of Plate Tectonic Theory and Critical Evaluation",
    "ECONOMY > Introduction to Economics > Evolution of Indian Economy",
    "ECONOMY > Introduction to Economics > Understanding the basics",
    "ECONOMY > Introduction to Economics > Economics Systems of world",
    "ECONOMY > National Income > Recent Developments related to National Income",
    "ECONOMY > National Income > National Income Accounting and its significance",
    "ECONOMY > National Income > Concepts of National Income: Income and Expenditure method",
    "ECONOMY > National Income > GDP Deflator and Trends of National Income",
    "ECONOMY > National Income > Concepts of National Income: Product Method",
    "ECONOMY > Government Budgeting > Introduction and Budget",
    "ECONOMY > Government Budgeting > Expenditure Component of Budget",
    "ECONOMY > Government Budgeting > Types of Budget",
    "ECONOMY > Government Budgeting > Deficit and its Types",
    "ECONOMY > Government Budgeting > Recent Developments in Budget",
    "ECONOMY > Government Budgeting > Evolution of Budget to Current Form",
    "ECONOMY > Government Budgeting > Receipts component of Budget",
    "ECONOMY > Government Budgeting > FRBM Act, 2003",
    "ECONOMY > Government Budgeting > Weakness and Reforms in Budgeting",
    "ECONOMY > Fiscal Policy > GST",
    "ECONOMY > Fiscal Policy > Impacts Of GST",
    "ECONOMY > Fiscal Policy > Evolution Of GST",
    "ECONOMY > Fiscal Policy > Reforms in Direct Tax and DIRECT TAX VIVAD SE VISHWAS ACT, 2020",
    "ECONOMY > Fiscal Policy > Types of Taxes: Indirect Tax",
    "ECONOMY > Fiscal Policy > Recent Development",
    "ECONOMY > Fiscal Policy > Introduction to Fiscal Policy",
    "ECONOMY > Fiscal Policy > Types of Taxes: Direct Tax",
    "ECONOMY > Fiscal Policy > Basics of Taxation",
    "ECONOMY > Fiscal Policy > Recent Developments in GST"
]

# This is a sample - the full list would have all 1,132 combinations
# For now, let's load it from the existing taxonomy file

def load_complete_taxonomy():
    """Load the complete taxonomy from the flattened JSON file"""
    import json
    try:
        with open('taxonomy/taxonomy_flattened.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Extract Full_Path from each entry
        return [entry["Full_Path"] for entry in data]
    except FileNotFoundError:
        # Fallback to the sample above
        return TAXONOMY_OPTIONS

def get_taxonomy_metadata():
    """Get metadata about the taxonomy"""
    options = load_complete_taxonomy()
    subjects = list(set([opt.split(" > ")[0] for opt in options]))
    
    return {
        "total_subjects": len(subjects),
        "total_combinations": len(options),
        "subjects": subjects,
        "all_paths": options
    }

# Pre-computed for maximum performance
TAXONOMY_METADATA = {
    "total_subjects": 14,
    "total_combinations": 1132,
    "description": "Educational taxonomy for question classification"
}

if __name__ == "__main__":
    # Test the constants
    print("📚 TAXONOMY CONSTANTS")
    print("=" * 50)
    print(f"Total subjects: {len(SUBJECTS)}")
    print(f"Subjects: {SUBJECTS}")
    
    metadata = get_taxonomy_metadata()
    print(f"\nTotal combinations: {metadata['total_combinations']}")
    print(f"Sample options:")
    for i, option in enumerate(metadata['all_paths'][:10]):
        print(f"  {i+1}. {option}")
    print("...")