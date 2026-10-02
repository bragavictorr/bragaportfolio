document.addEventListener("DOMContentLoaded", () => {
    
    // Seleciona todos os elementos que devem ser animados ao rolar a página
    const elementosParaAnimar = document.querySelectorAll('.animar-scroll, .animar-scroll-card');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // Ativa a animação quando 15% do elemento estiver visível
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Adiciona a classe que faz o elemento aparecer
                entry.target.classList.add('visivel');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Aplica o observador a cada elemento e cria um efeito cascata nos projetos
    elementosParaAnimar.forEach((elemento, index) => {
        if (elemento.classList.contains('animar-scroll-card')) {
            // Atraso sutil apenas para os cards de projetos ficarem com efeito escadinha
            elemento.style.transitionDelay = `${index * 0.1}s`;
        }
        observer.observe(elemento);
    });
});