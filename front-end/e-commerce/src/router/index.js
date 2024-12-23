import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import Customizable from "@/views/Customizable.vue";
import MenCustomize from "@/views/MenCustomize.vue";
import WomenCustomize from "@/views/WomenCustomize.vue";
import Kids from "@/views/Kids.vue";
import sneakerMen from "@/views/sneakerMen.vue";
import SneakerMen from "@/views/sneakerMen.vue";
import SneakerWomen from "@/views/sneakerWomen.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/home',
            name: 'home',
            component: HomeView
        },
        {
            path: '/customize',
            name: 'customize',
            component: Customizable
        },
        {
            path: '/customize/men',
            name: 'men-customize',
            component: MenCustomize
        },
        {
            path: '/customize/women',
            name: 'women-customize',
            component: WomenCustomize
        },
        {
            path: '/customize/kids',
            name: 'kids-customize',
            component: Kids
        },
        {
            path: '/customize/mens/sneakers',
            name: 'mens-sneakers-customize',
            component: SneakerMen
        },
        {
            path: '/customize/womens/sneakers',
            name: 'womens-sneakers-customize',
            component: SneakerWomen
        },
    ]
})


export default router