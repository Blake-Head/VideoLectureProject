# Manim Test Files

This folder contains a collection of test files demonstrating various Manim animation concepts and patterns commonly used in physics education videos. These files serve as examples, templates, and testing resources for the GAR-Videos project.

## File Overview

### `test_basic_geometry.py`
Tests fundamental geometric shapes and transformations:
- **BasicShapesTest**: Creates and displays basic shapes (circles, squares, triangles)
- **ColorAndFillTest**: Demonstrates different fill properties and transparency
- **TransformationTest**: Shows shape-to-shape transformations
- **MovementTest**: Tests object movement and positioning
- **ScalingTest**: Demonstrates scaling and rotation operations

### `test_text_and_math.py`
Tests text rendering and mathematical expressions:
- **TextTest**: Basic text rendering with different fonts and sizes
- **MathTexTest**: LaTeX mathematical expressions (equations, symbols)
- **LabeledDiagramTest**: Creating diagrams with labels and coordinate systems
- **EquationAnimationTest**: Animating equation transformations
- **FormattedTextTest**: Various text formatting options

### `test_physics_concepts.py`
Tests physics-specific visualizations:
- **ChargeVisualizationTest**: Point charges with proper labeling
- **VectorFieldTest**: Electric field vector visualization
- **ForceVectorTest**: Force vectors between charges
- **MotionTest**: Particle motion simulation
- **WaveTest**: Sine wave visualization

### `test_animation_timing.py`
Tests animation timing and sequencing:
- **TimingBasicsTest**: Basic timing and waiting
- **SequentialAnimationsTest**: One-after-another animations
- **SimultaneousAnimationsTest**: Multiple simultaneous animations
- **RunTimeTest**: Different animation durations
- **RateFunctionTest**: Different animation easing functions
- **LagRatioTest**: Staggered animations
- **ComplexTimingTest**: Complex timing combinations

### `test_complex_scenes.py`
Tests advanced scene compositions:
- **InteractiveSceneTest**: Complex scenes with coordinate systems
- **MultiObjectAnimationTest**: Many objects animating together
- **LayeredVisualizationTest**: Background, midground, foreground layers
- **PhysicsLectureSceneTest**: Complete lecture slide mockup

## Usage

Each file contains multiple Scene classes that can be rendered individually. To render a specific scene, use the Manim command:

```bash
manim -pql test_basic_geometry.py BasicShapesTest
```

Where:
- `-p` opens the video after rendering
- `-q` sets quality (l=low, m=medium, h=high)
- `test_basic_geometry.py` is the file name
- `BasicShapesTest` is the scene class name

## Common Patterns

These test files demonstrate common patterns used throughout the GAR-Videos project:

1. **Standard Imports**: All files start with `from manim import *`
2. **Scene Structure**: Each animation is a class inheriting from `Scene`
3. **construct() Method**: All animation logic goes in the `construct()` method
4. **Physics Context**: Many examples relate to electric fields, charges, and forces
5. **Educational Format**: Clear labeling, equations, and step-by-step reveals

## Testing Your Setup

Run any of these scenes to verify your Manim installation is working correctly. Start with simpler scenes like `BasicShapesTest` before moving to more complex ones.

## Extending the Tests

When adding new physics concepts or animation techniques to the project, consider adding corresponding test scenes to this collection to serve as examples for future development.