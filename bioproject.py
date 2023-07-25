# Issue #1: I have a list of bioproject ids and would like to extract the PMID for each of the bioproject id. Any suggestion?

# Answer by Carlos RB

from Bio import Entrez

def fetch_bioproject_summary(bioproject_id):
    Entrez.email = "your_email@example.com"

    # Fetch Bioproject summary using efetch function
    handle = Entrez.efetch(db="bioproject", id=bioproject_id, retmode="xml")
    xml_data = handle.read()
    handle.close()
    return xml_data

def extract_pubmed_ids(xml_data):
    from xml.etree import ElementTree as ET

    # Parse the XML data and extract all the PubMed IDs (PMIDs)
    root = ET.fromstring(xml_data)
    pubmed_ids = [pub.attrib.get("id") for pub in root.findall(".//ProjectDescr/Publication")]
    return pubmed_ids

def main():
    bioproject_ids = ['984146', '970997', '939104']  # Add your Bioproject IDs here

    for bioproject_id in bioproject_ids:
        xml_data = fetch_bioproject_summary(bioproject_id)
        pubmed_ids = extract_pubmed_ids(xml_data)

        print(f"Bioproject ID: {bioproject_id} - PubMed IDs (PMIDs): {', '.join(pubmed_ids)}")

if __name__ == "__main__":
    main()