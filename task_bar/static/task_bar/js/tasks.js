document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.task-check');
    const taskCards = document.querySelectorAll('.task-card');

    // Обработка кликов по галочкам
    buttons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault(); // Отключаем стандартное поведение

            const taskId = this.dataset.taskId;
            const field = this.dataset.field;
            const card = this.closest('.task-card');

            fetch(`/tasks/${taskId}/${field}/toggle/`, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': getCookie('csrftoken')
                }
            })
            .then(response => {
                if (!response.ok) throw new Error("Ошибка");

                // Переключаем класс "completed"
                card.classList.toggle('completed');
                updateProgress(); // Обновляем прогресс
            })
            .catch(err => {
                alert("Ошибка связи с сервером");
                console.error(err);
            });
        });
    });

    // Функция для получения CSRF токена
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Функция обновления прогресса
    function updateProgress() {
        const totalTasks = document.querySelectorAll('.task-card').length;
        const completedTasks = document.querySelectorAll('.task-card.completed').length;
        const progress = (completedTasks / totalTasks) * 100;

        const progressBar = document.querySelector('.progress');
        const progressText = document.querySelector('.progress-text');

        if (progressBar) {
            progressBar.style.width = `${progress}%`;
        }
        if (progressText) {
            progressText.textContent = `Выполнено ${completedTasks} из ${totalTasks} задач`;
        }
    }

    // Анимация появления карточек
    taskCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        setTimeout(() => {
            card.style.transition = 'all 0.5s ease';
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Обработка кнопки добавления задачи (если нужна)
    const addTaskBtn = document.querySelector('.add-task-btn');
    if (addTaskBtn) {
        addTaskBtn.addEventListener('click', function () {
            console.log('Добавление новой задачи');
        });
    }

    // Анимация при наведении на карточки
    taskCards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    });

    // Плавная прокрутка для мобильных устройств
    if (window.innerWidth <= 768) {
        const smoothScroll = (target) => {
            const element = document.querySelector(target);
            window.scrollTo({
                top: element.offsetTop - 100,
                behavior: 'smooth'
            });
        };

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                smoothScroll(this.getAttribute('href'));
            });
        });
    }

    // Вызываем при загрузке страницы
    updateProgress();
});


// Функция для получения CSRF токена
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
} 