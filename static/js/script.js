// Custom JavaScript for Car Price Prediction app

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileMenuButton = document.querySelector('button.text-white.focus\\:outline-none');
    
    if (mobileMenuButton) {
        const mobileMenu = document.createElement('div');
        mobileMenu.className = 'md:hidden bg-dark text-white py-4 hidden';            mobileMenu.innerHTML = `
            <div class="container mx-auto px-4 flex flex-col space-y-3">
                <a href="/" class="hover:text-primary transition block py-2">Home</a>
                <a href="/predict" class="hover:text-primary transition block py-2">Predict</a>
                <a href="/visualization" class="hover:text-primary transition block py-2">Visualization</a>
                <a href="/about" class="hover:text-primary transition block py-2">About</a>
            </div>
        `;
        
        mobileMenuButton.parentNode.parentNode.after(mobileMenu);
        
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }
    
    // Add fade-in animation to hero section
    const heroSection = document.querySelector('header');
    if (heroSection) {
        heroSection.classList.add('fade-in');
    }
    
    // Add hover effects to feature cards
    const featureCards = document.querySelectorAll('.bg-gray-50.rounded-lg.p-8.shadow-md');
    featureCards.forEach(card => {
        card.classList.add('hover-lift');
    });
});
