![p5-python](https://raw.githubusercontent.com/gromko/p5-python/main/media/p5-py.jpg)

p5-python is a creative coding library that brings the simplicity and functionality of the p5.js framework (which is based on Processing) to Python. It's designed to make it easy for artists, designers, and beginners to create visual art, animations, and interactive graphics.

### Key Features:

- **Simple Drawing Functions**: p5-python provides easy-to-use functions to draw shapes, lines, and colors.

- **Animation**: It has built-in support for creating animations, allowing for dynamic visuals.

- **Interactivity**: You can easily add mouse and keyboard interactions to your sketches.

- **Cross-Platform**: It works across different platforms, making it accessible to a wide audience.

### Basic Example

Here's a simple example of what p5 code might look like in Python:

```python

from p5 import *

def setup():

    createCanvas(400, 400)

def draw():

    background(200)

    ellipse(200, 200, 100)

run()

```

In this example, `createCanvas()` initializes the drawing window, and `draw()` continuously renders the frame, drawing a circle at the center.

### Usage

p5-python is often used for:

- Educational purposes to teach programming concepts.

- Rapid prototyping of visual ideas.

- Generative art and creative coding projects.

You can install p5-python using pip:

```bash

pip install p5-python

```

Then, you can create and run your sketches in a Python environment.
