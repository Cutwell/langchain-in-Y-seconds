import langsmith
from pirate_speak.chain import chain

def test_chain():
	client = langsmith.Client()
	chain_results = client.run_on_dataset(
		dataset_name="quickstart-dataset",
		llm_or_chain_factory=chain,
		project_name="test-fixed-vibration-74",
		concurrency_level=5,
		verbose=True,
	)