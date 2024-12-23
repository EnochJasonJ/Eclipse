<script setup>
    import ImgSld from '@/components/ImgSld.vue';
import { RouterLink } from 'vue-router';
</script>

<template>
    <div class="flex flex-row gap-10">
        <div id="side" class="w-[344px] h-[760px] bg-gradient-to-b from-[#fddbe6] via-[#fff8e3] to-[#b8d3fc] mt-10 ml-10 mb-10 rounded-2xl  flex flex-col">
            <div>
                <div class="flex flex-row items-center justify-center gap-5 mt-5">
                    <RouterLink class="text-2xl">Woman's Fashion</RouterLink>
                    <i class="pi pi-angle-right text-2xl"></i>
                </div>
                <div class="flex flex-col items-start justify-center mt-5 ml-20 mr-auto gap-2 text-lg">
                    <RouterLink>Casual Wears</RouterLink>
                    <RouterLink>Formal Wears</RouterLink>
                    <RouterLink>Party and Occasional Wears</RouterLink>
                    <RouterLink>work Wears</RouterLink>
                    <RouterLink>Sneakers and shoes</RouterLink>
                </div>
            </div>
            <div>
                <div class="flex flex-row items-center justify-center gap-5 mt-5">
                    <RouterLink class="text-2xl">Men's Fashion</RouterLink>
                    <i class="pi pi-angle-right text-2xl"></i>
                </div>
                <div class="flex flex-col items-start justify-center mt-5 ml-20 mr-auto gap-2 text-lg">
                    <RouterLink>Casual Wears</RouterLink>
                    <RouterLink>Formal Wears</RouterLink>
                    <RouterLink>Party and Occasional Wears</RouterLink>
                    <RouterLink>work Wears</RouterLink>
                    <RouterLink>Sneakers and shoes</RouterLink>
                </div>
            </div>
            <div>
                <div class="flex flex-row items-center justify-center gap-5 mt-5">
                    <RouterLink class="text-2xl">Kid's Fashion</RouterLink>
                    <i class="pi pi-angle-right text-2xl"></i>
                </div>
                <div class="flex flex-col items-start justify-center mt-5 ml-20 mr-auto gap-2 text-lg">
                    <RouterLink>Casual Wears</RouterLink>
                    <RouterLink>Formal Wears</RouterLink>
                    <RouterLink>Sneakers and shoes</RouterLink>
                </div>
            </div>
            <div>
                <div class="flex flex-row items-center justify-center gap-5 mt-5">
                    <RouterLink to="/customize" class="text-2xl">Customizables</RouterLink>
                    <i class="pi pi-angle-right text-2xl"></i>
                </div>
            </div>
        </div>
        <ImgSld id="slider" class="rounded-3xl"/>
    </div>
</template>


<style scoped>
    #side{
        box-shadow: 0 0 15px rgb(185, 185, 185);
    }
    
    
</style>