// Author: Berin
// With Luciano Ratamero and Mari Bedran
// Sketches repo: https://github.com/berinhard/sketches

var COLOR_PALETTE = PALETTES[Math.floor(Math.random()*PALETTES.length)]

var WIDTH = window.innerWidth;
var HEIGHT = window.innerHeight;

var packed_squares = [];
var max_size = 150;

class PackedSquare {

	constructor(x, y, size) {
		this.x = x;
		this.y = y;
		this.size = size;
		this.color = color(COLOR_PALETTE[parseInt(random(10000)) % 5]);
	}

	get radius() {
		return this.size / 2;
	}

	display() {
		fill(17, 17, 17, 50);
		var shadow_length = map(this.size, 10, max_size, 5, 40);
		rect(this.x + shadow_length, this.y + shadow_length, this.size, this.size);
		fill(this.color);
		rect(this.x, this.y, this.size, this.size);
	}

	get_x_range() {
		return [this.x - this.radius, this.x + this.radius];
	}

	get_y_range() {
		return [this.y - this.radius, this.y + this.radius];
	}

	is_colliding_with(square) {
		var [x0, x1] = square.get_x_range();
		var [y0, y1] = square.get_y_range();

		if (x0 < this.x && this.x < x1 && y0 < this.y && this.y < y1) {
			return true;
		}

		var diff_x = Math.abs(square.x - this.x);
		var diff_y = Math.abs(square.y - this.y);

		var min_diff = square.radius + this.radius;
		if (diff_x < min_diff && diff_y < min_diff) {
			return true
		}
		return false;
	}

	is_colliding() {
		for (var square of packed_squares) {
			if (this.is_colliding_with(square)) {
				return true
			}
		}
		return false
	}

	resize() {
		console.log('resize');
		while (this.is_colliding() && this.size > 10) {
			this.size--;
		}
	}

}

function setup() {
	createCanvas(WIDTH, HEIGHT);
	rectMode(CENTER);
	noFill();
	noStroke();
	background(29);
}

function draw() {
	x = random(width);
	y = random(height);

	square = new PackedSquare(x, y, max_size);
	square.resize();

	if (!square.is_colliding()) {
		square.display();
		packed_squares.push(square);
	}
}
