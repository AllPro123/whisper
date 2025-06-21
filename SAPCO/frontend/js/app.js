// Simple handler for pricing buttons
const buttons = document.querySelectorAll('.tier button');
buttons.forEach(btn => {
  btn.addEventListener('click', () => {
    const tier = btn.getAttribute('data-tier');
    alert(`Selected plan: ${tier}. Integration with Stripe goes here.`);
  });
});
