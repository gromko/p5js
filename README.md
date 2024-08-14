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



| **Function/Constant**  | **Type**     | **Description**                                                                 |
|------------------------|--------------|---------------------------------------------------------------------------------|
| `setup()`              | Function     | Called once at the beginning of the program to set initial environment properties.|
| `draw()`               | Function     | Continuously executes the lines of code contained inside its block until the program is stopped.|
| `createCanvas()`        | Function     | Creates a canvas element in the document, and sets the dimensions of it.        |
| `background()`          | Function     | Sets the background color of the canvas.                                        |
| `point()`               | Function     | Draws a point on the canvas at specified coordinates.                           |
| `line()`                | Function     | Draws a line between two points.                                                |
| `rect()`                | Function     | Draws a rectangle on the canvas.                                                |
| `ellipse()`             | Function     | Draws an ellipse (oval) on the canvas.                                          |
| `circle()`              | Function     | Draws an circle on the canvas.                                                  |
| `triangle()`            | Function     | Draws a triangle connecting three points.                                       |
| `quad()`                | Function     | Draws a quadrilateral (four-sided shape) connecting four points.                |
| `arc()`                 | Function     | Draws an arc (portion of an ellipse).                                           |
| `fill()`                | Function     | Sets the color used to fill shapes.                                             |
| `noFill()`              | Function     | Disables filling geometry shapes.                                               |
| `stroke()`              | Function     | Sets the color used for the lines around shapes.                                |
| `noStroke()`            | Function     | Disables drawing the outline of geometry shapes.                                |
| `strokeWeight()`        | Function     | Sets the thickness of lines and points.                                         |
| `noLoop()`              | Function     | Stops `draw()` from continuously executing.                                     |
| `loop()`                | Function     | Re-starts `draw()` to continuously execute after `noLoop()` has stopped it.     |
| `text()`                | Function     | Draws text on the canvas.                                                       |
| `textSize()`            | Function     | Sets the size of the text to be displayed.                                      |
| `textAlign()`           | Function     | Sets the alignment of the text.                                                 |
| `textFont()`            | Function     | Sets the font for displaying text.                                              |
|`beginShape()`           | Function     | Starts recording vertices for a custom shape.                                   |
| `endShape()`            | Function     | Stops recording vertices for a custom shape and draws it.                       |
| `vertex()`              | Function     | Specifies a vertex for a custom shape.                                          |
| `curveVertex()`         | Function     | Specifies a vertex for a custom shape using Catmull-Rom splines.                |
| `bezierVertex()`        | Function     | Specifies a vertex for a custom shape using Bezier curves.                      |
| `loadImage()`           | Function     | Loads an image from a file.                                                     |
| `image()`               | Function     | Draws an image to the canvas.                                                   |
| `width`                 | Constant     | Stores the width of the canvas.                                                 |
| `height`                | Constant     | Stores the height of the canvas.                                                |
| `keyPressed()`          | Function     | Called once every time a key is pressed.                                        |
| `keyReleased()`         | Function     | Called once every time a key is released.                                       |
| `keyTyped()`            | Function     | Called once every time a key is pressed and released.                           |
| `mousePressed()`        | Function     | Called once after every time a mouse button is pressed.                         |
| `mouseReleased()`       | Function     | Called once after every time a mouse button is released.                        |
| `mouseMoved()`          | Function     | Called every time the mouse moves and no mouse button is pressed.               |
| `mouseDragged()`        | Function     | Called every time the mouse moves and a mouse button is pressed.                |
| `keyIsPressed`          | Constant     | Stores a boolean value if any key is pressed.                                   |
| `mouseIsPressed`        | Constant     | Stores a boolean value if any mouse button is pressed.                          |
| `keyCode`               | Constant     | Stores the keycode of the last key pressed.                                     |
| `key`                   | Constant     | Stores the value of the last key pressed.                                       |
| `translate()`           | Function     | Moves the origin of the canvas to a new location.                               |
| `rotate()`              | Function     | Rotates the canvas by a specified angle.                                        |
| `scale()`               | Function     | Scales the canvas by a specified factor.                                        |
| `push()`                | Function     | Saves the current drawing style settings and transformations.                   |
| `pop()`                 | Function     | Restores the most recent drawing style settings and transformations.            |
| `PI`                    | Constant     | Stores the value of PI (π).                                                     |
| `TWO_PI`                | Constant     | Stores the value of 2 * PI.                                                     |
| `HALF_PI`               | Constant     | Stores the value of PI / 2.                                                     |
| `random()`              | Function     | Generates a random number within a specified range.                             |
| `mouseX`                | Constant     | Stores the current horizontal position of the mouse.                            |
| `mouseY`                | Constant     | Stores the current vertical position of the mouse.                              |
| `frameCount`            | Constant     | Stores the number of frames that have been displayed since the program started. |
| `frameRate()`           | Function     | Gets or sets the frame rate of the sketch.                                      |
| `delay()`               | Function     | Pauses the execution of the program for a specified number of milliseconds.     |
| `millis()`              | Function     | Returns the number of milliseconds since the                                    |
| `second()`              | Function     | Returns the current second.                                                     |
| `minute()`              | Function     | Returns the current minute.                                                     |
| `hour()`                | Function     | Returns the current hour.                                                       |
| `day()`                 | Function     | Returns the current day of the month.                                           |
| `month()`               | Function     | Returns the current month.                                                      |
| `year()`                | Function     | Returns the current year.                                                       |
| `alpha()`               | Function     | Returns the alpha value (transparency) of a color.                              |
| `red()`                 | Function     | Returns the red value of a color.                                               |
| `green()`               | Function     | Returns the green value of a color.                                             |
| `blue()`                | Function     | Returns the blue value of a color.                                              |
| `colorMode()`           | Function     | Sets the color mode for the sketch (RGB, HSB, HSL).                             |
| `lerpColor()`           | Function     | Interpolates between two colors by a given amount.                              |
| `dist()`                | Function     | Calculates the distance between two points.                                     |
| `map()`                 | Function     | Re-maps a number from one range to another.                                     |
| `constrain()`           | Function     | Constrains a number to be within a given range.                                 |
| `norm()`                | Function     | Normalizes a number from another range into a value between 0 and 1.            |
| `lerp()`                | Function     | Calculates a number between two numbers at a specific increment.                |








