<script setup>
    import CustomBtn from '@/components/CustomBtn.vue';
    import tgirl from '../assets/CustomT/tgirl.png'
    import CustomBox from '@/components/CustomBox.vue';
    import TShirt from '@/components/TShirt.vue';
</script>

<template>
    <div class="h-screen">
        <h1 class="text-2xl ml-40 mt-10">T-Shirt Women's Basic design</h1>
        <div class="flex flex-row items-center justify-center">
            <div class="flex flex-row items-center gap-52">
                <CustomBtn />
                <TShirt :imgURL="tgirl" class="mt-10 flex items-center justify-center" />
            </div>
            <CustomBox class="ml-auto text-center" />
        </div>
    </div>
</template>