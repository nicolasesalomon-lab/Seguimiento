export const translations = {
  es: {
    projects: 'Proyectos',
    loading: 'Cargando...'
  },
  en: {
    projects: 'Projects',
    loading: 'Loading...'
  }
};

export type Lang = keyof typeof translations;

export const defaultLang: Lang = 'es';

export function t(key: keyof typeof translations['es'], lang: Lang = defaultLang): string {
  return translations[lang][key];
}
