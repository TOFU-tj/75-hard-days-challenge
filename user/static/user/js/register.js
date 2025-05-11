document.addEventListener('DOMContentLoaded', function() {
    // Инициализация particles.js
    particlesJS('particles-js', {
        particles: {
            number: {
                value: 80,
                density: {
                    enable: true,
                    value_area: 800
                }
            },
            color: {
                value: '#8a2be2'
            },
            shape: {
                type: 'circle'
            },
            opacity: {
                value: 0.5,
                random: false
            },
            size: {
                value: 3,
                random: true
            },
            line_linked: {
                enable: true,
                distance: 150,
                color: '#8a2be2',
                opacity: 0.4,
                width: 1
            },
            move: {
                enable: true,
                speed: 2,
                direction: 'none',
                random: false,
                straight: false,
                out_mode: 'out',
                bounce: false
            }
        },
        interactivity: {
            detect_on: 'canvas',
            events: {
                onhover: {
                    enable: true,
                    mode: 'grab'
                },
                onclick: {
                    enable: true,
                    mode: 'push'
                },
                resize: true
            }
        },
        retina_detect: true
    });

    // Валидация пароля
    const password1 = document.querySelector('input[name="password1"]');
    const password2 = document.querySelector('input[name="password2"]');
    const requirements = {
        length: document.getElementById('length'),
        uppercase: document.getElementById('uppercase'),
        lowercase: document.getElementById('lowercase'),
        number: document.getElementById('number')
    };

    function validatePassword(password) {
        const validations = {
            length: password.length >= 8,
            uppercase: /[A-Z]/.test(password),
            lowercase: /[a-z]/.test(password),
            number: /[0-9]/.test(password)
        };

        Object.keys(validations).forEach(req => {
            if (validations[req]) {
                requirements[req].classList.add('valid');
            } else {
                requirements[req].classList.remove('valid');
            }
        });

        return Object.values(validations).every(Boolean);
    }

    function validatePasswordsMatch() {
        if (password1.value && password2.value) {
            if (password1.value !== password2.value) {
                password2.setCustomValidity('Пароли не совпадают');
            } else {
                password2.setCustomValidity('');
            }
        }
    }

    password1.addEventListener('input', function() {
        validatePassword(this.value);
        validatePasswordsMatch();
    });

    password2.addEventListener('input', validatePasswordsMatch);

    // Валидация числовых полей
    const numericInputs = document.querySelectorAll('input[type="number"]');
    numericInputs.forEach(input => {
        input.addEventListener('input', function() {
            const value = parseInt(this.value);
            if (value < 0) {
                this.value = 0;
            }
        });
    });

    // Анимация фокуса для полей ввода
    const formGroups = document.querySelectorAll('.form-group');
    formGroups.forEach(group => {
        const input = group.querySelector('input');
        input.addEventListener('focus', () => {
            group.classList.add('focused');
        });
        input.addEventListener('blur', () => {
            if (!input.value) {
                group.classList.remove('focused');
            }
        });
    });

    // Обработка отправки формы
    const form = document.getElementById('registerForm');
    form.addEventListener('submit', function(e) {
        if (!validatePassword(password1.value)) {
            e.preventDefault();
            showError('Пожалуйста, убедитесь, что пароль соответствует всем требованиям');
        }
    });

    // Функция для отображения ошибок
    function showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        
        const existingError = form.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }
        
        form.insertBefore(errorDiv, form.firstChild);
        
        setTimeout(() => {
            errorDiv.remove();
        }, 5000);
    }
}); 