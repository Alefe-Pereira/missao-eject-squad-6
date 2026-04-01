const imagens = [
  'imgs/carrossel/1.png',
  'imgs/carrossel/2.png',
  'imgs/carrossel/3.png',
];

let atual = 0;

const img = document.querySelector('.espaco-slider img');
const dots = document.querySelectorAll('.dot');

function irPara(index) {
  atual = (index + imagens.length) % imagens.length;
  img.src = imagens[atual];
  dots.forEach((dot, i) => dot.classList.toggle('ativo', i === atual));
}

document.querySelector('.prev').addEventListener('click', () => irPara(atual - 1));
document.querySelector('.next').addEventListener('click', () => irPara(atual + 1));
dots.forEach((dot, i) => dot.addEventListener('click', () => irPara(i)));

irPara(0);