// DOM Elements
const mobileMenuBtn = document.querySelector('.mobile-menu');
const navMenu = document.querySelector('.nav-menu');
const cartIcon = document.querySelector('.cart-icon');
const cartOverlay = document.querySelector('.cart-overlay');
const cart = document.querySelector('.cart');
const cartClose = document.querySelector('.cart-close');
const cartItems = document.querySelector('.cart-items');
const cartSubtotal = document.querySelector('.cart-subtotal');
const cartTotalPrice = document.querySelector('.cart-total-price');
const cartCount = document.querySelector('.cart-count');
const addToCartButtons = document.querySelectorAll('.add-to-cart');
const checkoutBtn = document.querySelector('.btn-checkout');
const checkoutModal = document.querySelector('.checkout-modal');
const closeCheckoutBtn = document.querySelector('.close-checkout');
const checkoutForm = document.querySelector('#checkout-form');
const confirmationModal = document.querySelector('.confirmation-modal');
const closeConfirmationBtn = document.querySelector('.close-confirmation');
const continueShoppingBtn = document.querySelector('#continue-shopping');
const orderNumberSpan = document.querySelector('#order-number');


// Cart Data
let cartData = [];

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    mobileMenuBtn.addEventListener('click', toggleMobileMenu);

    // Cart Toggle
    cartIcon.addEventListener('click', openCart);
    cartClose.addEventListener('click', closeCart);
    cartOverlay.addEventListener('click', (e) => {
        if (e.target === cartOverlay) {
            closeCart();
        }
    });

    // Add to Cart
    addToCartButtons.forEach(button => {
        button.addEventListener('click', addToCart);
    });

    // Load cart from localStorage
    loadCart();
});

// Mobile Menu Functions
function toggleMobileMenu() {
    navMenu.classList.toggle('active');
    mobileMenuBtn.querySelector('i').classList.toggle('fa-bars');
    mobileMenuBtn.querySelector('i').classList.toggle('fa-times');
}

// Cart Functions
function openCart() {
    cartOverlay.classList.add('show');
    cart.classList.add('show');
    document.body.style.overflow = 'hidden';
}

function closeCart() {
    cartOverlay.classList.remove('show');
    cart.classList.remove('show');
    document.body.style.overflow = 'auto';
}

function addToCart(e) {
    e.preventDefault();

    // Get product details
    const productCard = this.closest('.product-card');
    const productImg = productCard.querySelector('.product-img img').src;
    const productTitle = productCard.querySelector('.product-title').textContent;
    const productPrice = productCard.querySelector('.current-price').textContent;
    const priceValue = parseFloat(productPrice.replace('$', ''));

    // Check if product already exists in cart
    const existingItemIndex = cartData.findIndex(item => item.title === productTitle);

    if (existingItemIndex > -1) {
        // Increase quantity if product already in cart
        cartData[existingItemIndex].quantity += 1;
        cartData[existingItemIndex].total = cartData[existingItemIndex].quantity * cartData[existingItemIndex].price;
    } else {
        // Add new product to cart
        const newItem = {
            id: Date.now(),
            img: productImg,
            title: productTitle,
            price: priceValue,
            quantity: 1,
            total: priceValue
        };

        cartData.push(newItem);
    }

    // Update cart
    updateCart();
    saveCart();
    openCart();
}

function updateCart() {
    // Clear cart items
    cartItems.innerHTML = '';

    if (cartData.length === 0) {
        cartItems.innerHTML = '<p>Your cart is empty</p>';
        cartCount.textContent = '0';
        cartSubtotal.textContent = '$0.00';
        cartTotalPrice.textContent = '$0.00';
        return;
    }

    // Add items to cart
    let subtotal = 0;

    cartData.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <div class="cart-item-img">
                <img src="${item.img}" alt="${item.title}">
            </div>
            <div class="cart-item-details">
                <h4 class="cart-item-title">${item.title}</h4>
                <div class="cart-item-price">$${item.price.toFixed(2)}</div>
                <div class="cart-item-quantity">
                    <button class="quantity-btn decrease" data-id="${item.id}">-</button>
                    <input type="text" class="quantity-input" value="${item.quantity}" readonly>
                    <button class="quantity-btn increase" data-id="${item.id}">+</button>
                </div>
            </div>
            <div class="cart-item-remove" data-id="${item.id}">
                <i class="fas fa-trash"></i>
            </div>
        `;

        cartItems.appendChild(cartItem);
        subtotal += item.total;
    });

    // Update cart count
    cartCount.textContent = cartData.reduce((total, item) => total + item.quantity, 0);

    // Update cart totals
    cartSubtotal.textContent = `$${subtotal.toFixed(2)}`;
    cartTotalPrice.textContent = `$${subtotal.toFixed(2)}`;

    // Add event listeners to quantity buttons and remove buttons
    document.querySelectorAll('.decrease').forEach(button => {
        button.addEventListener('click', decreaseQuantity);
    });

    document.querySelectorAll('.increase').forEach(button => {
        button.addEventListener('click', increaseQuantity);
    });

    document.querySelectorAll('.cart-item-remove').forEach(button => {
        button.addEventListener('click', removeItem);
    });
}

function decreaseQuantity() {
    const id = parseInt(this.dataset.id);
    const itemIndex = cartData.findIndex(item => item.id === id);

    if (cartData[itemIndex].quantity > 1) {
        cartData[itemIndex].quantity -= 1;
        cartData[itemIndex].total = cartData[itemIndex].quantity * cartData[itemIndex].price;
    } else {
        cartData.splice(itemIndex, 1);
    }

    updateCart();
    saveCart();
}

function increaseQuantity() {
    const id = parseInt(this.dataset.id);
    const itemIndex = cartData.findIndex(item => item.id === id);

    cartData[itemIndex].quantity += 1;
    cartData[itemIndex].total = cartData[itemIndex].quantity * cartData[itemIndex].price;

    updateCart();
    saveCart();
}

function removeItem() {
    const id = parseInt(this.dataset.id);
    cartData = cartData.filter(item => item.id !== id);

    updateCart();
    saveCart();
}

// Local Storage Functions
function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cartData));
}

function loadCart() {
    const storedCart = localStorage.getItem('cart');

    if (storedCart) {
        cartData = JSON.parse(storedCart);
        updateCart();
    }
}

// Product Filter Functions
function filterProducts(category) {
    const productCards = document.querySelectorAll('.product-card');

    productCards.forEach(card => {
        const productCategory = card.querySelector('.product-category').textContent.toLowerCase();

        if (category === 'all' || productCategory.includes(category.toLowerCase())) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}

// Scroll to Top Button
window.addEventListener('scroll', () => {
    const scrollToTopBtn = document.querySelector('.scroll-to-top');

    if (window.pageYOffset > 300) {
        scrollToTopBtn?.classList.add('show');
    } else {
        scrollToTopBtn?.classList.remove('show');
    }
});

// Add scroll to top button if it doesn't exist
if (!document.querySelector('.scroll-to-top')) {
    const scrollToTopBtn = document.createElement('button');
    scrollToTopBtn.classList.add('scroll-to-top');
    scrollToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    document.body.appendChild(scrollToTopBtn);

    // Add styles
    const style = document.createElement('style');
    style.textContent = `
        .scroll-to-top {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 40px;
            height: 40px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 99;
        }

        .scroll-to-top.show {
            opacity: 1;
            visibility: visible;
        }

        .scroll-to-top:hover {
            background-color: #2a75e0;
        }
    `;
    document.head.appendChild(style);

    // Add event listener
    scrollToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Product Search
const searchForm = document.querySelector('#search-form');
const searchInput = document.querySelector('#search-input');

if (searchForm && searchInput) {
    searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const searchTerm = searchInput.value.toLowerCase().trim();

        if (searchTerm === '') return;

        const productCards = document.querySelectorAll('.product-card');

        productCards.forEach(card => {
            const productTitle = card.querySelector('.product-title').textContent.toLowerCase();
            const productCategory = card.querySelector('.product-category').textContent.toLowerCase();

            if (productTitle.includes(searchTerm) || productCategory.includes(searchTerm)) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
}

// Add product hover effect
const productCards = document.querySelectorAll('.product-card');

productCards.forEach(card => {
    card.addEventListener('mouseenter', () => {
        const img = card.querySelector('.product-img img');
        img.style.transform = 'scale(1.1)';
        img.style.transition = 'transform 0.5s ease';
    });

    card.addEventListener('mouseleave', () => {
        const img = card.querySelector('.product-img img');
        img.style.transform = 'scale(1)';
    });
});

// Checkout Modal Functions
function openCheckoutModal() {
    if (cartData.length === 0) {
        alert('Your cart is empty. Please add items before checking out.');
        return;
    }
    closeCart();
    checkoutModal.classList.add('show');
}

function closeCheckoutModal() {
    checkoutModal.classList.remove('show');
}

function openConfirmationModal() {
    const orderNumber = Math.floor(Math.random() * 1000000);
    orderNumberSpan.textContent = `#${orderNumber}`;
    confirmationModal.classList.add('show');
}

function closeConfirmationModal() {
    confirmationModal.classList.remove('show');
}

// Event Listeners for Checkout
checkoutBtn.addEventListener('click', openCheckoutModal);
closeCheckoutBtn.addEventListener('click', closeCheckoutModal);

checkoutModal.addEventListener('click', (e) => {
    if (e.target === checkoutModal) {
        closeCheckoutModal();
    }
});

checkoutForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Basic validation
    const name = document.querySelector('#name').value;
    const cardNumber = document.querySelector('#card-number').value;
    const expiry = document.querySelector('#expiry').value;
    const cvv = document.querySelector('#cvv').value;

    if (!name || !cardNumber || !expiry || !cvv) {
        alert('Please fill out all fields.');
        return;
    }

    // Simulate payment processing
    const submitBtn = checkoutForm.querySelector('.submit-btn');
    submitBtn.textContent = 'Processing...';
    submitBtn.disabled = true;

    setTimeout(() => {
        // Reset button
        submitBtn.textContent = 'Pay Now';
        submitBtn.disabled = false;

        // Clear form
        checkoutForm.reset();

        // Close checkout modal
        closeCheckoutModal();

        // Show confirmation
        openConfirmationModal();

        // Clear cart
        cartData = [];
        updateCart();
        saveCart();

    }, 2000); // 2-second delay to simulate processing
});

closeConfirmationBtn.addEventListener('click', closeConfirmationModal);
continueShoppingBtn.addEventListener('click', closeConfirmationModal);
