<script setup lang="ts">
    type Chanell = {
        id: number;
        name: string;
    }
    
    const { data: channels, status, refresh  } = await useFetch<Chanell[]>('http://localhost:8000/channels')
    
    const formData = ref({
        channelName: '',
    });
    const alertData = ref({
        message: '',
        status: '',
        isVisible: false,
    });
    const isModalVisible = ref(false);

    const addChannel = async () => {
        isModalVisible.value = false;
        await $fetch('http://localhost:8000/channel', {
            method: 'post',
            body: { name: formData.value.channelName }
        }).then(() => {
            alertData.value.message = `Channel ${formData.value.channelName} created`;
            alertData.value.status = 'success';
            alertData.value.isVisible = true;
            formData.value.channelName = '';
            refresh();
        }).catch((error) => {
            alertData.value.message = `Error: ${error}`;
            alertData.value.status = 'error';
            alertData.value.isVisible = true;
        });
        setTimeout(() => {
            alertData.value.isVisible = false;
        }, 3000);
    }

</script>
<template>
    <Alert v-if="alertData.isVisible" :message="alertData.message"/>
    <Modal v-if="isModalVisible"  >
        <form @submit.prevent="addChannel">
            <ModalHeader @close-modal="isModalVisible = false">Add new channel</ModalHeader>
            <ModalContent>
                <p>Set new channel name</p>
                <Input label="Channel name" id="channel-name" v-model="formData.channelName"/>
            </ModalContent>
            <ModalFooter>
                <button class="btn" type="submit">Save</button>
                <button class="btn" @click="isModalVisible = false" type="button">Cancel</button>
            </ModalFooter>
        </form>
    </Modal>
    <div class="header">
        <p>NNP</p>
    </div>
    <div class="channel-container">
        <div class="channel-list">
            <span class="channel-name channel-name-active">sidebar</span>
            <div v-if="status === 'pending'">Ładowanie...</div>
            <ul v-else>
                <li v-for="channel in channels" :key="channel.id" class="channel-name">
                    {{ channel.name }}
                </li>
            </ul>
            <span class="channel-name channel-name-add" @click="isModalVisible = true">new channel</span>
        </div>
        <div class="channel-content">
            <slot />
        </div>
        
    </div>
</template>
