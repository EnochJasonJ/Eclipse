<script setup>
    import girl from '../assets/customs/girl.png'
    import kid from '../assets/customs/kid.png'
    import men from '../assets/customs/men.png'
    import shoemen from '../assets/customs/shoemen.png'
    import womenshoe from '../assets/customs/womenshoe.png'
</script>

<template>
    <div id="main" class="flex flex-col mt-20">
        <div class="flex flex-row items-center justify-center">
            <RouterLink to="/customize/men"  class="mr-auto ml-auto"><img  :src="men" alt=""></RouterLink>
            <RouterLink to="/customize/women" class="mr-auto ml-auto"><img  :src="girl" alt="" ></RouterLink>
            <RouterLink to="/customize/kids" class="mr-auto ml-auto"><img  :src="kid" alt="" ></RouterLink>
        </div>
        <div class="flex flex-row gap-96 items-center justify-center ml-52 mt-20">
            <RouterLink to="/customize/mens/sneakers" class=" ml-auto"><img  :src="shoemen" alt="" ></RouterLink>
            <RouterLink to="/customize/womens/sneakers" class="mr-72"><img  :src="womenshoe" alt="" ></RouterLink>
        </div>
    </div>
</template>


<style scoped>
    #main{
        height: 100vh;
    }
    img{
        background: linear-gradient(297deg, #FCC5FF 1.15%, #FDE4FF 37.6%, #FEF0FF 43.4%, #C8DAFD 56.2%, #B8D4FC 99.83%);
        padding: 10px;
        border-radius: 60%;
        width: 200px;
        height: 200px;
        box-shadow: 0 0 15px rgb(191, 191, 191);
    }
</style>