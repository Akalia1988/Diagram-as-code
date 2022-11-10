from diagrams import Cluster, Diagram
from diagrams.gcp.analytics import BigQuery, Dataflow, PubSub
from diagrams.gcp.database import BigTable
from diagrams.gcp.compute import GCE

with Diagram("Streaming data to Bigtable", show=False):
    pubsub = PubSub("pubsub")

    with Cluster("Source of Data"):
        [GCE("CSV"),
         GCE("CSV1"),
         GCE("CSV2")] >> pubsub

    with Cluster("Targets"):
        with Cluster("Data Flow"):
            flow = Dataflow("data flow")
        with Cluster("Processing"):
                flow >> BigTable("bigtable")

            

    pubsub >> flow