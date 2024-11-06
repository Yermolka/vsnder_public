import random from 'lodash/random';

export function getRandomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[random(15)];
  }
  return color;
}

export function alphaColor(hexColor: string, value: number = 0.1) {
  if (!hexColor.startsWith('#') || hexColor.length !== 7) {
    throw new Error('Некорректный формат шестнадцатеричного цвета');
  }

  hexColor = hexColor.replace('#', '');

  const r = parseInt(hexColor.substring(0, 2), 16);
  const g = parseInt(hexColor.substring(2, 4), 16);
  const b = parseInt(hexColor.substring(4, 6), 16);

  const rgba = `rgba(${r}, ${g}, ${b}, ${value})`;

  return rgba;
}

export function lightenColor(hexColor: string, lightAmount: number): string {
  if (!hexColor.startsWith('#') || hexColor.length !== 7) {
    throw new Error('Некорректный формат шестнадцатеричного цвета');
  }

  if (lightAmount < 0 || lightAmount > 1) {
    throw new Error('Значение lightAmount должно быть от 0 до 1');
  }

  // Извлекаем компоненты R, G, B из шестнадцатеричного цвета
  const r = parseInt(hexColor.slice(1, 3), 16);
  const g = parseInt(hexColor.slice(3, 5), 16);
  const b = parseInt(hexColor.slice(5, 7), 16);

  // Вычисляем новые значения компонентов с учетом lightAmount
  const newR = Math.round(r * (1 - lightAmount) + 255 * lightAmount);
  const newG = Math.round(g * (1 - lightAmount) + 255 * lightAmount);
  const newB = Math.round(b * (1 - lightAmount) + 255 * lightAmount);

  // Преобразуем новые значения компонентов в шестнадцатеричный формат
  const newRHex = newR.toString(16).padStart(2, '0');
  const newGHex = newG.toString(16).padStart(2, '0');
  const newBHex = newB.toString(16).padStart(2, '0');

  return `#${newRHex}${newGHex}${newBHex}`;
}

export function darkenColor(hexColor: string, darkenAmount: number): string {
  // Проверяем, что входной параметр hexColor имеет правильный формат
  if (!hexColor.startsWith('#') || hexColor.length !== 7) {
    throw new Error('Некорректный формат шестнадцатеричного цвета');
  }

  // Проверяем, что darkenAmount находится в диапазоне от 0 до 1
  if (darkenAmount < 0 || darkenAmount > 1) {
    throw new Error('Значение darkenAmount должно быть от 0 до 1');
  }

  // Извлекаем компоненты R, G, B из шестнадцатеричного цвета
  const r = parseInt(hexColor.slice(1, 3), 16);
  const g = parseInt(hexColor.slice(3, 5), 16);
  const b = parseInt(hexColor.slice(5, 7), 16);

  // Вычисляем новые значения компонентов с учетом darkenAmount
  const newR = Math.round(r * (1 - darkenAmount));
  const newG = Math.round(g * (1 - darkenAmount));
  const newB = Math.round(b * (1 - darkenAmount));

  // Преобразуем новые значения компонентов в шестнадцатеричный формат
  const newRHex = newR.toString(16).padStart(2, '0');
  const newGHex = newG.toString(16).padStart(2, '0');
  const newBHex = newB.toString(16).padStart(2, '0');

  return `#${newRHex}${newGHex}${newBHex}`;
}

export function colorsLinearGradient(startColor: string, endColor: string) {
  return `linear-gradient(90deg, ${startColor} 0%, ${endColor} 100%)`;
}
