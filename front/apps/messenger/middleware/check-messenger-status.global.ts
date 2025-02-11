export default defineNuxtRouteMiddleware(() => {
    const url = useRequestURL();
    const currentLocation = btoa(url.href);
    const authUrl = `http://localhost/auth?state=${currentLocation}`;

    fetch('http://localhost/api/messenger/status', { credentials: 'include' }).then((response) => {
        if (!response.ok) {
            navigateTo(authUrl, { external: true });
        }
    }).catch(() => {
        navigateTo(authUrl, { external: true });
    });
});
