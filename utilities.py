import weaviate
from weaviate.client import WeaviateClient
import os

def connect_to_demo_db() -> WeaviateClient:
    """
    Helper function to connect to the demo Weaviate database.
    For queries only.
    This database instance has the necessary data loaded.
    """
    client = weaviate.connect_to_wcs(
        cluster_url="https://juofherxrfgo1cki4ierfa.c1.europe-west3.gcp.weaviate.cloud",                                     # Demo server URL,
        auth_credentials=weaviate.auth.AuthApiKey("0yM5hbvzEpSXXbI9ahHwEWCcSvloKdMpen5w"),   # Demo server read-only API key

        # OpenAI API key for queries that require it
        # Edit this to provide your own
        headers={"X-OpenAI-Api-Key": "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"},
    )  
    return client

def connect_to_my_db() -> WeaviateClient:
    """
    Helper function to connect to your own Weaviate instance.
    To be used for data loading as well as queries.
    """

    client = weaviate.connect_to_wcs(
        # Your Weaviate URL - Edit this to match your own Weaviate instance
        cluster_url="https://fugksjnutb2hwkgrqgknw.c0.europe-west3.gcp.weaviate.cloud",

        # Your Weaviate API Key - Edit this to match your own Weaviate instance
        auth_credentials=weaviate.auth.AuthApiKey("Vk69jZm3eorAfHSeyslUNh6Tlj373x4wVch2"),

        # OpenAI API key for queries that require it
        # Edit this to provide your own
        headers={"X-OpenAI-Api-Key": "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"},
    )

    # # Or use a local instance - e.g. with Docker
    # client = weaviate.connect_to_local(
    #     headers={"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}
    # )

    return client


def main():

    # Connect to Weaviate
    client = connect_to_my_db()

    try:
        # Check whether the client is ready
        assert client.is_ready()  # Check connection status (i.e. is the Weaviate server ready)

        # Try a query
        movies = client.collections.get("Movie")
        response = movies.query.near_text(query="time travel", limit=1)
        assert len(response.objects) == 1
        print("Success! You appear to be correctly set up.")
    finally:
        # Close the connection
        client.close()


if __name__ == "__main__":
    main()