document.addEventListener('DOMContentLoaded', function() {
    // Обработка клика по кнопке завершения задачи
    const taskChecks = document.querySelectorAll('.task-check');
    taskChecks.forEach(check => {
        check.addEventListener('click', function() {
            const taskCard = this.closest('.task-card');
            const taskId = this.dataset.taskId;
            
            // Добавляем анимацию и класс completed
            this.classList.add('checked');
            taskCard.classList.add('completed');
            
            // Отправляем запрос на сервер
            fetch(`/task-bar/complete-task/${taskId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Обновляем прогресс
                    updateProgress(data.progress);
                } else {
                    // В случае ошибки возвращаем исходное состояние
                    this.classList.remove('checked');
                    taskCard.classList.remove('completed');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                this.classList.remove('checked');
                taskCard.classList.remove('completed');
            });
        });
    });

    // Обработка клика по кнопке редактирования
    const taskEdits = document.querySelectorAll('.task-edit');
    taskEdits.forEach(edit => {
        edit.addEventListener('click', function() {
            const taskCard = this.closest('.task-card');
            const taskId = taskCard.querySelector('.task-check').dataset.taskId;
            // Здесь можно добавить логику редактирования задачи
            console.log('Edit task:', taskId);
        });
    });

    // Обработка клика по кнопке добавления новой задачи
    const addTaskBtn = document.querySelector('.add-task-btn');
    if (addTaskBtn) {
        addTaskBtn.addEventListener('click', function() {
            // Здесь можно добавить логику создания новой задачи
            console.log('Add new task');
        });
    }
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

// Функция для обновления прогресс-бара
function updateProgress(progress) {
    const progressBar = document.querySelector('.progress');
    const progressText = document.querySelector('.progress-text');
    
    if (progressBar && progressText) {
        progressBar.style.width = `${progress}%`;
        progressText.textContent = `Day ${Math.ceil(progress * 75 / 100)} of 75`;
    }
} 