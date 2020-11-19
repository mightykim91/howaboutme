export default [
    {
        path: "",
        name: "Main",
        component: () => import("@/views/MainPage.vue"),
      },
      {
        path: "maincopy",
        name: "MainCopy",
        component: () => import("@/views/MainPageCopy.vue"),
      },
      {
        path: "message",
        name: "Message",
        component: () => import("@/views/Message.vue"),
      },
      {
        path: "chat/:partner",
        name: "ChatRoom",
        component: () => import("@/views/ChatRoom.vue"),
        props: true,
      },
      {
        path: "profile",
        name: "Profile",
        component: () => import("@/views/Profile.vue"),
      },    
];
    