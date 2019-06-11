// Transcrypt'ed from Python, 2019-06-11 09:16:18
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, all, any, assert, bool, bytearray, bytes, callable, chr, deepcopy, delattr, dict, dir, divmod, enumerate, getattr, hasattr, isinstance, issubclass, len, list, object, ord, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, setattr, sorted, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {ADD, ALT, ARROW, AUDIO, AUTO, AXES, BACKSPACE, BASELINE, BEVEL, BEZIER, BLEND, BLUR, BOLD, BOLDITALIC, BOTTOM, BURN, CENTER, CHORD, CLAMP, CLOSE, CONTROL, CORNER, CORNERS, CROSS, CURVE, DARKEST, DEGREES, DEG_TO_RAD, DELETE, DIFFERENCE, DILATE, DODGE, DOWN_ARROW, ENTER, ERODE, ESCAPE, EXCLUSION, FILL, GRAY, GRID, HALF_PI, HAND, HARD_LIGHT, HSB, HSL, IMAGE, IMMEDIATE, INVERT, ITALIC, LANDSCAPE, LEFT, LEFT_ARROW, LIGHTEST, LINEAR, LINES, LINE_LOOP, LINE_STRIP, MIRROR, MITER, MOVE, MULTIPLY, NEAREST, NORMAL, OPAQUE, OPEN, OPTION, OVERLAY, P2D, PI, PIE, POINTS, PORTRAIT, POSTERIZE, PROJECT, QUADRATIC, QUADS, QUAD_STRIP, QUARTER_PI, RADIANS, RADIUS, RAD_TO_DEG, REPEAT, REPLACE, RETURN, RGB, RIGHT, RIGHT_ARROW, ROUND, SCREEN, SHIFT, SOFT_LIGHT, SQUARE, STROKE, SUBTRACT, TAB, TAU, TEXT, TEXTURE, THRESHOLD, TOP, TRIANGLES, TRIANGLE_FAN, TRIANGLE_STRIP, TWO_PI, UP_ARROW, VIDEO, WAIT, WEBGL, _CTX_MIDDLE, _DEFAULT_FILL, _DEFAULT_LEADMULT, _DEFAULT_STROKE, _DEFAULT_TEXT_FILL, _P5_INSTANCE, abs, accelerationX, accelerationY, accelerationZ, acos, add_library, alpha, ambientLight, ambientMaterial, angleMode, append, applyMatrix, arc, arrayCopy, asin, atan, atan2, background, beginContour, beginShape, bezier, bezierDetail, bezierPoint, bezierTangent, bezierVertex, blend, blendMode, blue, boolean, box, brightness, byte, camera, ceil, changed, char, circle, color, colorMode, concat, cone, constrain, copy, cos, createA, createAudio, createButton, createCamera, createCanvas, createCapture, createCheckbox, createColorPicker, createDiv, createElement, createFileInput, createGraphics, createImage, createImg, createInput, createNumberDict, createP, createRadio, createSelect, createShader, createSlider, createSpan, createStringDict, createVector, createVideo, createWriter, cursor, curve, curveDetail, curvePoint, curveTangent, curveTightness, curveVertex, cylinder, day, debugMode, degrees, deviceOrientation, directionalLight, disableFriendlyErrors, displayDensity, displayHeight, displayWidth, dist, ellipse, ellipseMode, ellipsoid, endContour, endShape, exp, fill, filter, float, floor, focused, frameCount, frameRate, fullscreen, getURL, getURLParams, getURLPath, global_p5_injection, green, height, hex, hour, httpDo, httpGet, httpPost, hue, image, imageMode, input, int, join, key, keyCode, keyIsDown, keyIsPressed, lerp, lerpColor, lightness, lights, line, loadBytes, loadFont, loadImage, loadJSON, loadModel, loadPixels, loadShader, loadStrings, loadTable, loadXML, log, logOnloaded, loop, mag, map, match, matchAll, max, millis, min, minute, model, month, mouseButton, mouseIsPressed, mouseX, mouseY, nf, nfc, nfp, nfs, noCanvas, noCursor, noDebugMode, noFill, noLoop, noSmooth, noStroke, noTint, noise, noiseDetail, noiseSeed, norm, normalMaterial, orbitControl, ortho, pAccelerationX, pAccelerationY, pAccelerationZ, pRotationX, pRotationY, pRotationZ, perspective, pixelDensity, pixels, plane, pmouseX, pmouseY, point, pointLight, pow, pre_draw, preload, push, pwinMouseX, pwinMouseY, py_clear, py_get, py_pop, py_sort, py_split, quad, quadraticVertex, radians, random, randomGaussian, randomSeed, rect, rectMode, red, redraw, remove, removeElements, resetMatrix, resetShader, resizeCanvas, reverse, rotate, rotateX, rotateY, rotateZ, rotationX, rotationY, rotationZ, round, saturation, save, saveCanvas, saveFrames, saveJSON, saveStrings, saveTable, scale, second, select, selectAll, set, setAttributes, setCamera, setMoveThreshold, setShakeThreshold, shader, shearX, shearY, shininess, shorten, shuffle, sin, smooth, specularMaterial, sphere, splice, splitTokens, sq, sqrt, square, start_p5, str, stroke, strokeCap, strokeJoin, strokeWeight, subset, tan, text, textAlign, textAscent, textDescent, textFont, textLeading, textSize, textStyle, textWidth, texture, textureMode, textureWrap, tint, torus, touches, translate, triangle, trim, turnAxis, unchar, unhex, updatePixels, vertex, width, winMouseX, winMouseY, windowHeight, windowWidth, year} from './pytop5js.js';
var __name__ = 's_195';
export var square_size = 40;
export var squares_map = dict ({});
export var Square =  __class__ ('Square', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self, x, y, size) {
		self.x = x;
		self.y = y;
		self.size = size;
		self._alpha = 1;
		self.color = tuple ([random (255), random (255), random (255), self.alpha]);
		self.color_2 = tuple ([random (255), random (255), random (255), self.alpha]);
		if (random (1) > 0.5) {
			self.coords_1 = tuple ([self.x, self.y, self.x, self.y + self.size, self.x + self.size, self.y + self.size]);
			self.coords_2 = tuple ([self.x, self.y, self.x + self.size, self.y, self.x + self.size, self.y + self.size]);
		}
		else {
			self.coords_1 = tuple ([self.x, self.y, self.x, self.y + self.size, self.x + self.size, self.y]);
			self.coords_2 = tuple ([self.x + self.size, self.y + self.size, self.x, self.y + self.size, self.x + self.size, self.y]);
		}
	});},
	get display () {return __get__ (this, function (self) {
		stroke (27, 27, 27, 10);
		if (self.alpha == 1) {
			fill (240);
		}
		else {
			fill (...self.color);
		}
		triangle (...self.coords_1);
		if (self.alpha == 1) {
			fill (240);
		}
		else {
			fill (...self.color_2);
		}
		triangle (...self.coords_2);
	});},
	get _get_alpha () {return __get__ (this, function (self) {
		return self._alpha;
	});},
	get _set_alpha () {return __get__ (this, function (self, value) {
		if (self._alpha + value < 255) {
			self._alpha += value;
		}
	});},
	get py_update () {return __get__ (this, function (self) {
		self.alpha += 5;
		self.color = tuple ([self.color [0], self.color [1], self.color [2], self.alpha]);
		self.color_2 = tuple ([self.color_2 [0], self.color_2 [1], self.color_2 [2], self.alpha]);
	});}
});
Object.defineProperty (Square, 'alpha', property.call (Square, Square._get_alpha, Square._set_alpha));;
export var setup = function () {
	pixelDensity (displayDensity ());
	var __left0__ = tuple ([window.innerWidth, window.innerHeight]);
	var w = __left0__ [0];
	var h = __left0__ [1];
	createCanvas (w, h);
	for (var x of range (0, w, square_size)) {
		for (var y of range (0, h, square_size)) {
			squares_map.__setitem__ ([x, y], Square (x, y, square_size));
		}
	}
};
export var clean_coord = function (x, y) {
	var x = (Math.floor (x / square_size)) * square_size;
	var y = (Math.floor (y / square_size)) * square_size;
	return tuple ([x, y]);
};
export var draw = function () {
	background (240);
	for (var square of squares_map.py_values ()) {
		square.display ();
	}
	var __left0__ = clean_coord (mouseX, mouseY);
	var x = __left0__ [0];
	var y = __left0__ [1];
	squares_map.__getitem__ ([x, y]).py_update ();
};

//# sourceMappingURL=s_195.map