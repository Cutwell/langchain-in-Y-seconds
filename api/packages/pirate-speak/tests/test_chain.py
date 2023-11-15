from pirate_speak.chain import chain
from datetime import datetime
import langsmith

def test_chain():
	client = langsmith.Client()
	chain_results = client.run_on_dataset(
		dataset_name="quickstart-dataset",
		llm_or_chain_factory=chain,
		project_name=f"quickstart-dataset-test-{int(datetime.now().strftime('%Y%m%d%H%M%S'))}",
		concurrency_level=5,
		verbose=True,
	)