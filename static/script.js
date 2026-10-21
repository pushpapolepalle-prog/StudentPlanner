document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll("[data-filter]");
    const tasks = document.querySelectorAll(".task");

    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            const filter = button.dataset.filter;

            buttons.forEach(function (item) {
                item.classList.remove("active");
            });

            button.classList.add("active");

            tasks.forEach(function (task) {
                const status = task.dataset.status;

                task.hidden = filter !== "all" && filter !== status;
            });
        });
    });

    const allButton = document.querySelector('[data-filter="all"]');
    if (allButton) {
        allButton.classList.add("active");
    }
});