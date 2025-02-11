<script setup lang="ts">
    import { 
        Modal,
        ModalContent,
        ModalFooter,
        ModalHeader,
        Input,
        Alert,
        DefaultLayout,
        SidenavContainer,
        SidenavItem,
    } from '@nnp/ui-kit';
    type Chanell = {
        id: number;
        name: string;
    }

    const headers = useRequestHeaders(['cookie'])
    const { data: channels, status, refresh  } = await useFetch<Chanell[]>('http://localhost/api/messenger/channels', { headers })
    
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
        await $fetch('http://localhost/api/messenger/channel', {
            method: 'post',
            body: { 
                name: formData.value.channelName 
        }
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

    onMounted(() => {
        if (!channels.value) {
            refresh();
        }
    });

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
    <DefaultLayout />
    <SidenavContainer>
        <div class="channel-list">
            <span class="channel-name channel-name-active">sidebar</span>
            <div v-if="status === 'pending'">Ładowanie...</div>
            <ul v-else>
                <li v-for="channel in channels" :key="channel.id" class="channel-name">
                    <SidenavItem key="{{channel.id}}">{{ channel.name }}</SidenavItem>
                </li>
            </ul>
            <span class="channel-name channel-name-add" @click="isModalVisible = true">new channel</span>
        </div>
        <div class="channel-content">
        </div>
    </SidenavContainer>
</template>
<style lang="scss">
    .channel-list {
        display: flex;
        flex-direction: column;
        padding: 1rem 1rem 0 1rem;
        border-right: 1px solid #BDBDBD;
        min-width: 200px;
        overflow: auto;

        ul {
            margin: 0;
            padding: 0;
        }
        
    }

    .channel-name {
        padding-right: 1rem;
        padding-left: 1rem;
        padding-top: 0.25rem;
        padding-bottom: 0.25rem;
        list-style: none;
        cursor: pointer;

        &-active {
            border-radius: 0.25rem;
            font-weight: bold;
        }
    }

    .channel-content {
        width: 100%;
        padding-left: 1rem;
        overflow: auto;
    }
</style>