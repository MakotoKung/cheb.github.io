const canvas = document.getElementById('characterCanvas');
const ctx = canvas.getContext('2d');

const skin = new Image();
skin.src = 'skin.png'; // ไฟล์สกินของคุณ

let time = 0;

// ฟังก์ชันวาดตัวละคร
function drawCharacter() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const walkOffset = Math.sin(time * 0.1) * 5; // แกว่งขาแขนซ้ายขวา

  // วาดหัว
  ctx.drawImage(skin, 8, 8, 8, 8, 80, 20, 40, 40); // (skinX, skinY, width, height, canvasX, canvasY, width, height)

  // วาดตัว
  ctx.drawImage(skin, 20, 20, 8, 12, 85, 60, 30, 60);

  // แขนซ้าย
  ctx.save();
  ctx.translate(80, 70); // จุดหมุนแขนซ้าย
  ctx.rotate(walkOffset * 0.03);
  ctx.drawImage(skin, 44, 20, 4, 12, -10, 0, 20, 50);
  ctx.restore();

  // แขนขวา
  ctx.save();
  ctx.translate(120, 70); // จุดหมุนแขนขวา
  ctx.rotate(-walkOffset * 0.03);
  ctx.drawImage(skin, 36, 52, 4, 12, -10, 0, 20, 50);
  ctx.restore();

  // ขาซ้าย
  ctx.save();
  ctx.translate(90, 120);
  ctx.rotate(walkOffset * 0.02);
  ctx.drawImage(skin, 4, 20, 4, 12, -10, 0, 20, 40);
  ctx.restore();

  // ขาขวา
  ctx.save();
  ctx.translate(110, 120);
  ctx.rotate(-walkOffset * 0.02);
  ctx.drawImage(skin, 12, 20, 4, 12, -10, 0, 20, 40);
  ctx.restore();
}

function animate() {
  time++;
  drawCharacter();
  requestAnimationFrame(animate);
}

skin.onload = () => {
  animate();
};
//Play SOund
function playSound() {
    var sound = document.getElementById("soundEffect");
    sound.currentTime = 0.1; 
    sound.play();
    setTimeout(function() {
        sound.pause();
      }, (0.5 - 0.1) * 1000); // คำนวณส่วนที่เล่น (วินาที) แล้วแปลงเป็นมิลลิวินาที
  }
  var Isbefore = true;
  function changeImage() {
    const image = document.getElementById("Sound");
    const music = document.getElementById("soundBG");
    

      if (Isbefore){
        image.src = "img/mu.png";
        Isbefore = false;
        music.muted = true;
      } else {
        image.src = "img/s.png";
        Isbefore = true;
        music.muted = false;
      }
    }
    