<script setup>
    import {RouterLink} from 'vue-router'
</script>

<template>
    <div class="flex items-center justify-center mt-5">
        <nav class="bg-white h-14 flex justify-center shadow-lg w-3/4 p-6 rounded-3xl">
            <div class="container mx-auto flex items-center">
                <RouterLink to="/home" class="text-2xl font-semibold mr-auto ml-5">Exclusive</RouterLink>
                <ul class="flex flex-row gap-10 items-center justify-center ml-auto ">
                    <li> <RouterLink to="/home">Home</RouterLink> </li>
                    <li> <RouterLink to="/home">Cart</RouterLink> </li>
                    <li> <RouterLink to="/home">Become a Seller</RouterLink> </li>
                </ul>
                <form class="mx-auto">
                    <input type="text" name="search" id="search"placeholder="Search products" class="text-center w-72 h-8 bg-gray-100 rounded-md">
                </form>
                <div id="i" class="flex flex-col items-center justify-center gap-1">
                    <RouterLink class="flex flex-col items-center justify-center">
                        <i class="pi pi-user text-lg"></i>
                        <p>Account</p>
                    </RouterLink>
                </div>
            </div>
        </nav>
    </div>
</template>


<style scoped>
    #i {
        font-size: 10px;
    }
</style>