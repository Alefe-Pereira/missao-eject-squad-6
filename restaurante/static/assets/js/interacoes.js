const btnMobile = document.querySelector('.menu-mobile');
const navLinks = document.querySelector('.nav-links');
const icone = document.querySelector ('.menu-mobile i');

btnMobile.addEventListener('click', () => {
    navLinks.classList.toggle('active');

    if (navLinks.classList.contains('active')){
        icone.classList.remove('bi-list');
        icone.classList.add('bi-x-lg');
    } else {
        icone.classList.remove('bi-x-lg');
        icone.classList.add('bi-list');
    }
});

// MODAL DE RESERVA

// seleciona os elementos principais do modal
const modalReserva = document.getElementById('modalReserva');
const btnFecharModal = document.getElementById('fecharModal');

// seleciona todos os botões de abrir o modal usando a classe 
const botoesAbrirModal = document.querySelectorAll('.btn-abrir-reserva');

//  seleciona o formulário e o botão de confirmar
const formReserva = document.getElementById('formReserva');
const btnConfirmar = document.getElementById('btnConfirmar');

// ABRIR E FECHAR 

botoesAbrirModal.forEach(botao => {
  botao.addEventListener('click', (event) => {
    event.preventDefault();
    modalReserva.classList.add('active'); // mostra o modal (display: flex)
  });
});

// fecha o modal ao clicar no botão x
btnFecharModal.addEventListener('click', () => {
  modalReserva.classList.remove('active');
});

// fecha o modal se o usuário clicar no fundo escuro fora da caixa branca
modalReserva.addEventListener('click', (event) => {
  if (event.target === modalReserva) {
    modalReserva.classList.remove('active');
  }
});


// --- LÓGICA DE CONFIRMAR RESERVA ---

formReserva.addEventListener('submit', (event) => {
  
  
  // muda o texto e adiciona a classe do css que deixa verde
  btnConfirmar.textContent = 'RESERVA CONFIRMADA';
  btnConfirmar.classList.add('sucesso'); 
  
  // fecha o modal após 2.5 segundos
  setTimeout(() => {
    modalReserva.classList.remove('active'); // esconde o modal
    
    // eeseta o formulário e o botão para o estado original (caso queiram abrir de novo)
    btnConfirmar.textContent = 'CONFIRMAR RESERVA';
    btnConfirmar.classList.remove('sucesso');
    formReserva.reset(); // limpa os campos de texto e data
  }, 2500);
});