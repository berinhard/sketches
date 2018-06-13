float x, y, px, py; 
float timeX;
float timeY;
int rotationDegree, currentColor, clockSection;

void initClock(){
  currentColor = 255;
  rotationDegree = 210;
  clockSection = 0;
  background(0);
}

void setup() {
  size(700, 700);
  frameRate(100);
  
  px = 160; 
  py = 300;
  timeX = 0;
  timeY = 10;
  initClock();
}

void draw() {
  if (frameCount % 500 == 0) {  // 5 seconds had passed
    currentColor -= 20;
    rotationDegree += 30;
    clockSection += 1;
  }
  
  if (clockSection == 12) {  // 1 minute had passed
    initClock();
  }
  
  x = (160 * 4) / 5 * noise(timeX); 
  y = height / 2 * noise(timeY);
  timeX = timeX + 0.006;
  timeY = timeY + 0.012;
  
  pushMatrix();
  translate(width / 2, height / 2);
  rotate(radians(rotationDegree));
  stroke(255, 180, currentColor, 30);
  line(px, py, x, y); 
  popMatrix();
}
