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

        console.log(formData.value);
        await $fetch('http://localhost:8002/auth/jwt/login', {
            method: 'post',
            credentials: "include",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: params,
        }).catch((error) => {
            console.log(error);
        });
    };

    const currentUser = async () => {
        await $fetch('http://localhost:8002/protected-route', {
            method: 'get',
            credentials: "include",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }).then((data) => {
            console.log(data);
        }).catch((error) => {
            console.log(error);
        });
    };
    const logout = async () => {
        await $fetch('http://localhost:8002/auth/jwt/logout', {
            method: 'post',
            credentials: "include",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
        }).catch((error) => {
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
            <button @click="currentUser" class="btn" type="submit">get</button>
            <button @click="logout" class="btn" type="submit">logout</button>

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