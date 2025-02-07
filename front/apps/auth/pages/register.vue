<script setup>
    import { Input } from "@nnp/ui-kit"
    import { DefaultLayout } from "@nnp/ui-kit"

    const formData = ref({
        email: '',
        password: '',
    });

    const createUser = async (e) => {
        e.preventDefault();
        await $fetch('http://localhost:8002/auth/register', {
            method: 'post',
            body: { 
                username: formData.value.email,
                email: formData.value.email,
                password: formData.value.password
            }
        }).then((data) => {
            localStorage.setItem('access_token', data.access_token);
        }).catch((error) => {
            console.log(error);
        });
    };
</script>
<template>
    <DefaultLayout>
        <div class="container">
            <form @submit.prevent="createUser">
                <Input id="email" v-model="formData.email" label="Email" />
                <Input id="password" v-model="formData.password" label="Password" />
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
        background-color: #1565c0;
    }
</style>