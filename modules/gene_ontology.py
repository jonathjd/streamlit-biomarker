import requests

URL = "http://api.geneontology.org/api/bioentity/function/"


def get_ontology_biomarkers(go_id: str) -> dict:
    """
    Retrieve protein biomarkers associated with a given Gene Ontology (GO) ID.

    Args:
        go_id (str): The GO ID to query.

    Returns:
        dict: A dictionary containing lists of UniProt IDs, protein names,
        gene ontology labels, gene ontology IDs, and UniProt URLs for the
        biomarkers associated with the given GO ID. If there are no biomarkers
        associated with the given GO ID, an empty dictionary is returned.
    Raises:
        ValueError: If an error occurs while processing the proteins.

    """

    biomarkers = {
        "UniProtId": [],
        "Protein Name": [],
        "Gene Ontology": [],
        "Gene Ontology ID": [],
        "URL": [],
    }

    params = {
        "start": 0,
        "rows": 13000,
        "unselect_evidence": True,
        "exclude_automatic_assertions": True,
        "taxon": "NCBITaxon:9606",
    }

    while True:
        # Make and send request URL
        request = "".join([URL, go_id, "/genes"])

        response = requests.get(request, params=params)
        data = response.json()

        # If request returns no results return empty dict
        if data["associations"] == []:
            break

        for prot in data["associations"]:
            if prot["subject"]["taxon"]["id"].endswith("9606") and prot["subject"][
                "id"
            ].startswith("Uni"):
                try:
                    uniprot = prot["subject"]["id"].split(":")[1]
                    protein_name = prot["subject"]["label"]
                    protein_url = prot["subject"]["iri"]
                    protein_go_id = prot["object"]["id"]
                    protein_go_id_label = prot["object"]["label"]

                    biomarkers["UniProtId"].append(uniprot)
                    biomarkers["Protein Name"].append(protein_name)
                    biomarkers["Gene Ontology"].append(protein_go_id_label)
                    biomarkers["Gene Ontology ID"].append(protein_go_id)
                    biomarkers["URL"].append(protein_url)
                except KeyError as e:
                    raise ValueError(f"Error processing protein {prot}: {e}")

        # Update start for pagination
        params["start"] += params["rows"]

    return biomarkers
