// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  css: ['~/assets/index.scss'],
  modules: ['@nuxtjs/google-fonts'],
  postcss: {
    plugins: {
      'postcss-import': {},
      'postcss-nested': {},
    },
  },
})