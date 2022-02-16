<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />
        <q-toolbar-title> Accounting Web Application </q-toolbar-title>
      </q-toolbar>
    </q-header>
    <q-drawer v-model="leftDrawerOpen" show-if-above="false" bordered>
      <q-list>
        <q-item-label header> APPLICATION MENU </q-item-label>
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import EssentialLink from '../components/EssentialLink.vue';

const linksList = [
  {
    title: 'First menu',
    caption: '',
    icon: '',
    link: '',
  },
  {
    title: 'Second menu',
    caption: '',
    icon: '',
    link: '',
  },
  {
    title: 'Third menu',
    caption: '',
    icon: '',
    link: '',
  },
  {
    title: 'Forth menu',
    caption: '',
    icon: '',
    link: '',
  },
  {
    title: 'Fifth menu',
    caption: '',
    icon: '',
    link: '',
  },
  {
    title: 'Quasar documentation',
    caption: 'The official documentation of Quasar javascript framework',
    icon: 'school',
    link: 'https://quasar.dev',
  },
  {
    title: 'Project source code',
    caption: 'You can access the source code of this project by clicking this button',
    icon: 'code',
    link: '',
  }
];

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialLink,
  },

  data() {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksList,
    };
  },

  methods: {
    toggleLeftDrawer() {
      this.leftDrawerOpen = !this.leftDrawerOpen;
    },
  },
});
</script>
