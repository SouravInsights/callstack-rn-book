## CHAPTER 8

### DRAW EFFICIENTLY ON A CANVAS WITH SKIA

ISSUE: CORE APPLICATION DESIGN

IDEA IS DIFFICULT TO IMPLEMENT WITH THE TRADITIONAL APPROACHES

PO or design team may have the uncompromised vision of the product design or have in mind some specific features that may be difficult to build with Rive/react-native-reanimated without sacrificing performance or cross platform issues. Maybe there's an idea to adopt some design trend? Maybe the app will be graphs-heavy or will have a graphic-rich dashboard? Or maybe there's a plan to have a screen with performant and beautiful image transitions?

Component's shadow rendering approach is different in iOS and android, masking may be rather slow on android, limited blur support on android.

While being easy to use and performant tool, Rive also has some constraints like limited Blur, Glow, Shadow support and limited path effects.

So at the time this kind of issue is encountered you will most likely have in mind an exact picture you want to see in your app. And with the requirements that precise you will require the tool that can give you maximum control over the rendering pipeline.

#### SOLUTION: MAYBE IT'S TIME TO CHECKOUT SKIA

Skia is an open source 2D graphics library which provides common APIs that work across a variety of hardware and software platforms. It serves as the graphics engine for Google Chrome and ChromeOS, Android, Flutter, Mozilla Firefox and Firefox OS, and many other products.

Thanks to Shopify, React Native developers have access to declarative Skia drawing capabilities using the @shopify/react-native-skia library. With it we can get full control over the rendering, down to

the pixels. It's a powerful instrument to cover almost any case you can imagine with the great performance overall.

# React Native Skia

React Native Skia's API uses the &#x3C;Canvas /> element that will be the last native element in the app's view tree and will serve as a root of your Skia drawing. All react-native-skia child components that will be put into it will serve as a declarative api for the library. Behind the scenes it'll use its own React renderer.

Here's an example of how @shopify/react-native-skia can be used, rendering two circles on the fixed size Canvas and blend them together.

import React from 'react';
import { useWindowDimensions } from 'react-native';
import { Canvas, Circle, Group, vec } from '@shopify/react-native-skia';

const App = () => {
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width \* 0.33;
return (
&#x3C;Canvas style={{ width, height }}>
&#x3C;Group blendMode='multiply'>
&#x3C;Circle cx={r} cy={c.y} r={r} color='cyan' />
&#x3C;Circle cx={width - r} cy={c.y} r={r} color='magenta' />
&#x3C;/Group>
&#x3C;/Canvas>
);
};

From this example we also can see one of the core elements of the API – the &#x3C;Group /> component. Groups can be deeply nested and can apply operations to their children:

- Paint properties – pretty similar to svg the properties applied to the group (ex. style, color) will be inherited by the child elements.
- Transformations – almost identical to React Native transform property with one significant difference: in React Native, the origin of transformation is the center of the object, whereas it is the top-left position of the object in Skia.
- Clipping – clip property provides the region in which children elements will be shown while outside region's part will be hidden. It can be reverted by the invertClip property.
- Bitmap effects – layer property will create bitmap drawing of the children which you can for example use to build effects that need to be applied to the group of elements.

To make one of the circles move we can use Reanimated:

import React from 'react';
import { useWindowDimensions } from 'react-native';
import { Canvas, Circle, Group, vec } from '@shopify/react-native-skia';
import {
Easing,
cancelAnimation,
useSharedValue,
withRepeat,
withTiming,
} from 'react-native-reanimated';

export const useLoop = ({ duration }) => {
const progress = useSharedValue(0);
useEffect(() => {
progress.value = withRepeat(
withTiming(1, { duration, easing: Easing.inOut(Easing.ease) }),
-1,
true
);
return () => {
cancelAnimation(progress);
};
}, [duration, progress]);
return progress;
};

const App = () => {
const ANIMATION_OFFSET = 50;
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width \* 0.33;
const progress = useLoop({duration: 2000});
const circleTranslate = useDerivedValue(
() => mix(progress.value, c.y + ANIMATION_OFFSET, c.y - ANIMATION_OFFSET),
[progress],
);
return (

<group>
</group>

# React Native Skia Integration

As you might have noticed, React Native Skia can directly accept Reanimated values as props, making it seamless to integrate canvas drawings with animations that delight your users.

One major thing to notice is that &#x3C;Canvas /> is transparent by default so it will be a nice baseline to use it for some fancy looking custom components. Here we'll add a &#x3C;View /> with the red square in the middle which will be rendered underneath the &#x3C;Canvas />.

const App = () => {
const ANIMATION_OFFSET = 50;
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width \* 0.33;
const progress = useLoop({duration: 2000});
const circleTranslate = useDerivedValue(
() => mix(progress.value, c.y + ANIMATION_OFFSET, c.y -
ANIMATION_OFFSET),
[progress],
);
return (
&#x3C;>
&#x3C;View
style={{
alignItems: 'center',
justifyContent: 'center',
...StyleSheet.absoluteFill,
}}>
&#x3C;View style={{height:      300, width:  300,
backgroundColor:    'red'}} />
&#x3C;/View>
&#x3C;Canvas style={{flex: 1}}>

# Current Page

<group>
<circle cx="{r}" cy="{c.y}" r="{r}" color="cyan">
<circle cx="{width" -="" r}="" cy="{circleTranslate}" r="{r}" color="magenta">
</circle></circle></group>

The thing to remember is that if you are using the to apply the effect that will need to affect the underlying layer these changes will only be applied to the elements. Things like <shadow> will be rendered correctly but <blur> will only have the data about the elements that are used inside canvas. You will need to somehow capture the snapshot of the layer.
</blur></shadow>

For that the makeImageFromView function exists. You can call it with the ref to the <view> you want the snapshot of and it will return you a Promise with the image data that you can use as a canvas layer for transformation.
</view>

So if we add a blurred card to our component you will see the blur only around the circles and the red square we've added in the last example will look as sharp as always. To fix that we'll take a snapshot of the underlying view and refer it as an image on the .

const pd = PixelRatio.get();

const App = () => {
const {width, height} = useWindowDimensions();
const c = vec(width / 2, height / 2);
const r = width _ 0.33;
const CARD_WIDTH = width - 60;
const CARD_HEIGHT = CARD_WIDTH _ 0.5;
const ANIMATION_OFFSET = 50;
const clip = useMemo(
() => rrect(rect(0, 0, CARD_WIDTH, CARD_HEIGHT), 20, 20),
[CARD_HEIGHT, CARD_WIDTH],
);
const ref = useRef<view>(null);
};
</view>

const progress = useLoop({ duration: 2000 });
const x = useSharedValue((width - CARD_WIDTH) / 2);
const y = useSharedValue((height - CARD_HEIGHT) / 2);
const transform = useDerivedValue(() => [
{ translateY: y.value },
{ translateX: x.value },
]);
const circleTranslate = useDerivedValue(
() => mix(progress.value, c.y + ANIMATION_OFFSET, c.y - ANIMATION_OFFSET),
[progress],
);
const [image, setImage] = useState<SkImage | null>(null);

useEffect(() => {
makeImageFromView(ref).then(snapshot => setImage(snapshot));
}, []);

return (
<>
<View
ref={ref}
collapsable={false}
style={{
alignItems: 'center',
justifyContent: 'center',
...StyleSheet.absoluteFill,
}}>
<View style={{ height: 300, width: 300, backgroundColor: 'red' }} />
</View>

<Image
image={image}
x={0}
y={0}
height={(image?.height() ?? 0) / pd}
width={(image?.width() ?? 0) / pd}
/>
<Group>
<Circle cx={r} cy={c.y} r={r} color='cyan' />
<Circle cx={width - r} cy={circleTranslate} r={r} color='magenta' />
</Group>

</>
);

This approach can help you to create nicely looking cross-platform overlays on top of your main application content but need to be planned in advance since you need to have a ref to the underlying view.

Another thing react-native-skia is great at is path interpolation. The calculations are performed on the native side with C++ so it's blazingly fast, does not lock the JS thread, and hence will keep the UI responsive to user actions.

# In this simple example we'll use the d3 library to generate two curved paths from the data that we'll then render on the canvas and animate the switch between them.

import React, {useEffect} from 'react';
import {useSharedValue, withRepeat, withTiming} from 'react-native-reanimated';
import {
Skia,
usePathInterpolation,
Canvas,
Path,
} from '@shopify/react-native-skia';
import {curveBasis, line, scaleLinear, scaleTime} from 'd3';
const GRAPH_HEIGHT = 500;
const GRAPH_WIDTH = 350;
export const data1 = [
{date: '2023-12-01T00:00:00.000Z', value: 110},
…
{date: '2023-12-15T00:00:00.000Z', value: 700},
];
export const data2 = [
{date: '2023-12-01T00:00:00.000Z', value: 700},
…
{date: '2023-12-15T00:00:00.000Z', value: 400},
];
const makeGraph = data => {
const max = Math.max(...data.map(val => val.value));
const y = scaleLinear().domain([0, max]).range([GRAPH_HEIGHT, 35]);
const x = scaleTime()
.domain([new Date(2023, 12, 1), new Date(2023, 12, 15)])
.range([10, GRAPH_WIDTH - 10]);
const curvedPath = line()
.x(d => x(new Date(d.date)))
.y(d => y(d.value))
.curve(curveBasis)(data);
return Skia.Path.MakeFromSVGString(curvedPath!);
};
const App = () => {
const progress = useSharedValue(0);
const graphData = [makeGraph(data1), makeGraph(data2)];
useEffect(() => {
progress.value = withRepeat(withTiming(1, {duration:

1000}), -1, true);

}, [progress]);

const path = usePathInterpolation(

progress,

[0, 1],

[graphData[0], graphData[1]],

);

return (

&#x3C;Canvas style={{flex: 1}}>

&#x3C;Path

path={path}

style='stroke'

strokeWidth={5}

strokeCap='round'

strokeJoin='round'

/>

&#x3C;/Canvas>

);

Myn

The usePathInterpolation hook will take care of the correct

interpolation of the path value when switching the graphs. For

the animation to look smooth, the path needs to be interpolatable

and contain the same number and types of commands or the interpolation may potentially look incorrect or can cause the crash of your app.

### BENEFITS: ACCESS TO THE POWERFUL TOOL THAT WILL HELP YOU CREATE UNIQUE AND PERFORMANT UI

Close to native performance, high customizability and great API will help you a lot if your goal is to create something creative and fast. Add to that good integration with the current generation of tools like react-native-gesture-handler and react-native-reanimated and you'll get yourself a fantastic instrument to have when a new UI design trend pops up.

We only covered a fraction of things react-native-skia can do. Things like image processing filters, masking, rich text render and all powerful shaders are out of our scope of this guide.

The best places to learn more about React Native Skia and possible applications will be the official documentation, William Candillon's YouTube channel, and Daniel Friyia's YouTube channel.

”In 2023, we made a strategic decision to rely completely on Reanimated for animations. This move has brought several benefits. Firstly, it's the React Native animation system that people are already proficient with, which streamlines the learning curve. It enables us to animate native views and Skia drawings simultaneously and integrates seamlessly with react-native-gesture-handler. Now, we're taking our integration with Reanimated further by providing new APIs. These APIs allow for the creation of textures directly on the UI thread and enable the animation of large scenes based on these textures.”

William Candillon

# PART 1
