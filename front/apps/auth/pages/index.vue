<script setup>
    import { Input } from "@nnp/ui-kit"
    import { DefaultLayout } from "@nnp/ui-kit"


    const formData = ref({
        email: '',
        password: '',
    });

    const login = async (e) => {
        e.preventDefault();

        const params = new URLSearchParams({
            "username": formData.value.email,
            "password": formData.value.password,
        });

        await $fetch('http://localhost/api/auth/login', {
            method: 'post',
            credentials: "include",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: params,
        }).then(() => {
            if (window.location.search.includes('state')) {
                const url = atob(window.location.search.split('=')[1]);
                window.location.href = url;
            }
        })
        .catch((error) => {
            console.log(error);
        });
    };
</script>
<template>
    <DefaultLayout>
        <div class="container">
            <form @submit.prevent="login">
                <Input id="email" v-model="formData.email" label="Email" />
                <Input id="password" v-model="formData.password" label="Password" type="password"/>
                <button class="btn" type="submit">Login</button>
            </form>
        </div>
    </DefaultLayout>

</template>

<style lang="scss" scoped>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: calc(100vh - 57px); // 40px height + 1px border + 8px padding top + 8px padding bottom
    }
</style>