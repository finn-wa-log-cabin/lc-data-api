from typing import List

import azure.functions as func
from cabin.domain.tables.summary import Summary


def main(req: func.HttpRequest, dataJson: str) -> func.HttpResponse:
    summaries: List[Summary] = Summary.loads_flattened(dataJson, many=True)
    body = Summary.Schema(exclude=["RowKey", "PartitionKey", "customerID"]).dumps(
        summaries, many=True
    )
    return func.HttpResponse(body=body)
