import '../static/css/input.css'; // Your Tailwind CSS
import { createIcons, ChevronRight, SunMedium, Moon } from 'lucide';

const initializeTheme = () => {
    const theme = localStorage.getItem('theme') === 'abyss' ? 'abyss' : 'lemonade';
    document.documentElement.setAttribute('data-theme', theme);

    const themeController = document.querySelector('.theme-controller');
    if (!(themeController instanceof HTMLInputElement)) {
        return;
    }

    themeController.checked = theme === 'abyss';

    themeController.addEventListener('change', () => {
        const selectedTheme = themeController.checked ? 'abyss' : 'lemonade';
        document.documentElement.setAttribute('data-theme', selectedTheme);
        localStorage.setItem('theme', selectedTheme);
    });
};

const renderIcons = () => {
    createIcons({
        icons: {
            ChevronRight,
            SunMedium,
            Moon,
        },
    });
};

initializeTheme();

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderIcons, { once: true });
} else {
    renderIcons();
}