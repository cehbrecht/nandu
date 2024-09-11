from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

class SayHelloProcess(BaseProcessor):
    def __init__(self, processor_def):
        super().__init__(processor_def)
        self.metadata = {
            'version': '1.0.0',
            'id': 'say-hello',
            'title': 'Say Hello',
            'description': 'Returns a simple greeting message.',
            'inputs': {
                'name': {
                    'title': 'Your name',
                    'description': 'Please enter your name.',
                    'schema': {
                        'type': 'string',
                        'default': 'World'
                    },
                    'minOccurs': 0,
                    'maxOccurs': 1
                }
            },
            'outputs': {
                'response': {
                    'title': 'Output response',
                    'description': 'The greeting message.',
                    'schema': {
                        'type': 'string'
                    }
                }
            }
        }

    def execute(self, data):
        try:
            # Retrieve the input value, if not provided, use "World" as default
            name = data['inputs'].get('name', 'World')
            response = f"Hello {name}!"
            return {
                'outputs': {
                    'response': response
                }
            }
        except Exception as e:
            raise ProcessorExecuteError(f'Error in Say Hello process: {str(e)}')
