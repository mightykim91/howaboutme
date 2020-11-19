export default {
    namespace: true,
    state: {
        userName: '',
        isBeingLiked: false,
        isGettingMessage: false,
    },
    mutations: {
        AlertUserBeingLiked(user){
            //네비게이션에 알람 띄우기
            //네비 확인하면 삭제
            this.isBeingLiked = true;
        }
    }
    
}