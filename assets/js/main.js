// CARROSSEL DE IMAGENS
const imagens = [
  'assets/imgs/homepage/carrossel/1.png',
  'assets/imgs/homepage/carrossel/2.png',
  'assets/imgs/homepage/carrossel/3.png',
];

let atual = 0;

const img = document.querySelector('.espaco-slider img');

// Gera os dots dinamicamente
const dotsContainer = document.querySelector('.espaco-dots');
imagens.forEach((_, i) => {
  const dot = document.createElement('span');
  dot.classList.add('dot');
  dotsContainer.appendChild(dot);
});

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