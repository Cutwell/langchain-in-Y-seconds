# <img src="https://raw.githubusercontent.com/Cutwell/langchain-in-Y-seconds/main/langchain-in-y-seconds.png" style="width:100px;padding-right:20px;margin-bottom:-8px;">Learn LangChain in Y seconds
 Learn the entire LangChain tech-stack fast 🏃‍♀️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Prerequisites

1. Install Python (3.11.6 used in video).
2. Install Poetry.
3. Install DirEnv (or use another secret manager).
4. Get your [OpenAI API key](https://platform.openai.com/api-keys).
5. Sign up for LangSmith and get your LangSmith API key (https://smith.langchain.com/ and access API keys via the 🔑 icon on the bottom left).

## Tutorial walkthrough

0. If using a secret file (e.g.: `.envrc`), create a `.gitignore` file similar to the one in this repository, to prevent accidentally sharing your API keys.

1. Create a `.envrc` file and populate it with this template:

```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
export LANGCHAIN_API_KEY=<your-langsmith-api-key>
export LANGCHAIN_PROJECT=langchain-quickstart  # if not specified, defaults to "default"

export OPENAI_API_KEY=<your-openai-api-key>
```

2. Open a new terminal and run these commands:

```bash
poetry init -n --python=3.11.6 && poetry add langchain-cli
source ./.venv/bin/activate
poetry run langchain app new api --package pirate-speak
```

_Type 'Y' when prompted to install pirate-speak as a mirrored module_

3. Replace the `NotImplemented` route in `api/app/server.py` with a route for your component chain:

```python
from pirate_speak.chain import chain as pirate_speak_chain

add_routes(app, pirate_speak_chain, path="/pirate-speak")
```

4. Update the project `name` in `api/pyproject.toml`:
```toml
name = "api"
```

_This can be any name other than `__app_name__`_

5. Open a new terminal in `/api` and run these commands:

```bash
poetry install
source ./.venv/bin/activate
poetry run langchain serve
```

6. Visit http://127.0.0.1:8000/pirate-speak/playground/ in your web browser and play with your chain.

7. Open LangSmith (https://smith.langchain.com/) and visit the project page. View one of your traces (created when you tested the playground demo) and use it to create a dataset.

8. View the dataset and click `New Test Run` to get a code snippet:

```python
client = langsmith.Client()
chain_results = client.run_on_dataset(
	dataset_name="quickstart-dataset",	# this will change if you use a different dataset name.
	llm_or_chain_factory=chain,
	project_name="test-formal-project-4",
	concurrency_level=5,
	verbose=True,
)
```

9. Create a new PyTest file `test_chain.py` in `api/packages/pirate-speak/tests/`:

```python
from pirate_assistant.chain import chain
import langsmith
from datetime import datetime # import datetime module to get a timestamp

def test_chain():
	client = langsmith.Client()

	chain_results = client.run_on_dataset(
		dataset_name="quickstart-dataset",
		llm_or_chain_factory=chain,
		project_name=f"quickstart-dataset-test-{int(datetime.now().strftime('%Y%m%d%H%M%S'))}", # use a timestamped unique project name each re-run
		concurrency_level=5,
		verbose=True,
	)
```

_To enable PyTest re-runs, we want to use a timestamped unique project name to store each successive test result._

10. Open a terminal in `/api` and run these commands:

```bash
poetry add pytest --group=dev
poetry run python -m pytest -s .
```

11. View your dataset test runs, and add the trace to a new annotation queue.

12. View your annotation queue and explore the review interface.

🎉🎉 **Congratulations!** 🎉🎉
You've completed this tutorial and now have a complete LangChain project. If you need more help with navigating the LangSmith interface, go view the video version of this tutorial [on Youtube](https://youtu.be/q76MWApFIt4).

## License

MIT
