float x, y; 
float px, py;
float tempoX = 0;
float tempoY = 10;
boolean hasLine = false;
boolean external = false;

void setup() {
  size(500, 500); 
  x = width * noise(tempoX); 
  y = height * noise(tempoY);
  
  frameRate(10);
  background(50);
}

void draw() {  
  boolean pHasLine = hasLine;
  boolean pExternal = external;
  float noiseX, noiseY;
  px = x; // guarda a posição x na variável px
  py = y; // guarda a posição y na variável py
  
  noiseX = noise(tempoX);
  noiseY = noise(tempoY);
  println("noise X - ", noiseX);
  println("noise Y - ", noiseY);
  
  if (noiseX < 0.3) {
    x = (width / 2) * noiseX;
    y = height - height / 4 * noiseY;
    external = true;
    hasLine = false;
  } else if (noiseX < 0.5) {
    x = (width / 2) * (1 + noiseX);
    y = 2 * (height / 4) * noiseY;
    hasLine = true;
    external = false;
  } else if (noiseX < 0.6) {
    x = (width / 2) * noiseX;
    y = 3 * (height / 4) * noiseY;
    hasLine = true;
    external = false;
  } else {
    x = (width / 2) * (1 + noiseX);
    y = height * noiseY;
    external = true;
    hasLine = false;
  }
  
  stroke(255 * noiseY, 255 * noiseX, 255 * noiseX, 100);
  fill(255 * noiseY, 255 * noiseX, 255 * noiseX);
  ellipse(x, y, 20, 20);
  if (hasLine && pHasLine){
    line(px, py, x, y); 
  }
  if (external && pExternal) {
    line(px, py, x, y); 
  }
  
  tempoX = tempoX + 1;
  tempoY = tempoY + 0.1;
}
