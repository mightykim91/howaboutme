<template>
  <div>
    <Title :title="title" />
    <div class="pic-box">
      <div class="upload-pic">
        <form enctype="multipart/form-data">
          <div class="text-center">
            <label for="upload-image">
              <div class="image-info" v-if="!uploadImage">
                <img class="icon-pic" src="@/assets/images/icon/album.png">
                <br>
                <small class="image-info">프로필로 등록할<br>사진을 선택해주세요</small>
              </div>
            </label>
            <input
              accept="image/jpg, image/jpeg"
              id="upload-image"
              type="file"
              ref="imageInput"
              @change="onChangeUploadImages"
            />
            <div v-if="uploadImage">
              <img class="upload-image" :src="uploadPreview" />
              <img @click="uploadDelete()" class="close-icon" src="@/assets/images/icon/close.png">
            </div>
          </div>
        </form>
      </div>
      
      <div class="upload-pic">
        <form enctype="multipart/form-data">
          <div class="text-center">
            <label for="camera-image">
              <div class="image-slogan" v-if="!cameraImage">
                <img class="icon-pic" src="@/assets/images/icon/camera2.png">
                <br>
                <small class="image-info">유사도 측정을 위해<br>사진 촬영을 해주세요<br><small class="mt-0">( 해당 사진은 저장되지 않습니다. )</small></small>
              </div>
            </label>
            <input
              accept="image/jpg, image/jpeg"
              capture="camera"
              id="camera-image"
              type="file"
              ref="cameraInput"
              @change="onChangeCameraImages"
            />
            <div v-if="cameraImage">
              <img class="camera-image" :src="cameraPreview" />
              <img @click="cameraDelete()" class="close-icon" src="@/assets/images/icon/close.png">
            </div>
          </div>
        </form>
      </div>
      <!-- <div class="similarity-info"> -->
        <div class="cell">
          <div class="card">

            <div v-if="similarity" class="loader">
                <div class="inner">
                    <h2> {{this.similarity}}%</h2>
                </div>
            </div>
            <br>
            <div v-if="onClick" class="loading-bars">
              <span  class="gauge-loader">&#8230;</span>
              <div class="box">
                <div class="loader4"></div>
                <!-- <p>loader 4</p> -->
              </div>
            </div>
              <!-- <div class="fancy-button">
                <div class="left-frills frills"></div>
                <div class="button">{{this.similarity}} %</div>
                <div class="right-frills frills"></div>
              </div> -->
              
            <!-- <button>{{this.similarity.slice(-5,-2)}}</button> -->
          </div>
        </div>
      </div>
    <!-- </div> -->
    <v-btn
      width="300px"
      height="38px"
      rounded
      class="mx-auto my-2"
      color="#f1c3c3"
      dark
      @click="checkSimilarity"
      v-if="uploadImage && cameraImage && similarity"
    >유사도 재측정
    </v-btn>
    <v-btn
      width="300px"
      height="38px"
      rounded
      class="mx-auto my-2"
      color="white"
      @click="emitSimilarity()"
      v-if="uploadImage && cameraImage && similarity"
    >사진 저장
    </v-btn>
    <v-btn
      width="300px"
      height="38px"
      rounded
      class="mx-auto my-2"
      color="#f1c3c3"
      dark
      
      @click="checkSimilarity"
      v-if="uploadImage && cameraImage && !similarity && !onClick"
    >유사도 측정
    </v-btn>
    <v-btn
      width="300px"
      height="38px"
      rounded
      class="mx-auto my-2"
      color="#E5E5E5"
      dark
      @click="isValid"
      v-if="!uploadImage || !cameraImage "
    >유사도 측정
    </v-btn>
  </div>
</template>

<script>
import axios from "axios"

import USERAPI from "@/api/UserApi.js"
import Title from "../../components/common/Title";
import { mapGetters, mapState,mapActions } from 'vuex';

export default {
  name:"Upload",
  components:{
    Title
  },
  data(){
    return{
      title:"사진 등록",
      onClick: false,
      uploadPreview:null,
      cameraPreview:null,
      
      cameraImage:null,
      uploadImage:null,
      similarity:null,
    }
  },
  computed:{
    ...mapState('user',['authToken','userInfo']),
    ...mapGetters('user',['config']),
    // ...mapMutations('user',['setSimilarity'])

  },
  methods:{
    ...mapActions('user',['setSimilarity']),

    onChangeUploadImages(e) {
        // console.log(e.target.files)
        this.uploadImage = this.$refs.imageInput.files[0]

        const file = e.target.files[0];
        this.uploadPreview = URL.createObjectURL(file);
        // .then(()=>{
          const formData = new FormData()
          console.log(this.uploadImage)
          formData.append("image", this.uploadImage)
          console.log(formData)
          for (let key of formData.entries()){
            console.log(`${key}`)
          }
          // console.log('요청전')
          console.log(formData)
          axios.post(USERAPI.BASE_URL + '/images/upload/', formData, {
            headers:{
              'Content-Type': 'multipart/form-data',
              'Authorization': `JWT ${this.authToken}`
            }
          })
          .then((res)=>{
            console.log(res)

          }).catch((err)=>{
            // console.log('요청후')
            this.$swal('','정확한 분석을 위해\n선명한 사진을 사용해주세요. ','warning')
            
            console.log(err)
          })
        // })
    },
    onClickCameraUpload() {
        this.$refs.cameraInput.click();
    },
    onChangeCameraImages(e) {
        this.cameraImage = this.$refs.cameraInput.files[0]
        const file = e.target.files[0];
        this.cameraPreview = URL.createObjectURL(file);
    },
    checkSimilarity(){
      this.similarity = null
      this.onClick = true
      const formData = new FormData()
      console.log(this.uploadImage)
      formData.append("image1", this.uploadImage)
      formData.append("image2", this.cameraImage)

      console.log(formData)
      for (let key of formData.entries()){
        console.log(`${key}`)
      }
      console.log('요청전')
      console.log(formData)
      axios.post(USERAPI.BASE_URL + '/images/analysis/', formData, {
        headers:{
          'Content-Type': 'multipart/form-data',
          'Authorization': `JWT ${this.authToken}`
        }
      }).then((res)=>{
        console.log(res)
        this.similarity = res.data.similarity.slice(-5,-2)
        this.onClick = 0
      }).catch((err)=>{
        console.log(err.response.data.msg)
        if (err.response.data.msg === "2"){
          this.$swal({
            title: '',
            text: '왼쪽 사진에서 얼굴이 인식되지 않습니다. \n선명한 사진을 업로드해주세요.',
            imageUrl: 'https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/face-recognition.png?alt=media&token=09ff0dc0-deb7-4652-8a02-73ab30698b57',
            imageWidth: 100,
            imageHeight: 100,
            confirmButtonText: '확인',
            imageAlt: 'Custom image',
          })
        }else{
          this.$swal({
            title: '',
            text: '유사도 측정이 어렵습니다.\n셀프 촬영시, 핸드폰을 사진처럼\n오른쪽으로 90도 회전해서 촬영해보세요.',
            imageUrl: 'https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/rotate_pic.png?alt=media&token=09ff0dc0-deb7-4652-8a02-73ab30698b57',
            imageWidth: 150,
            imageHeight: 100,
            confirmButtonText: '확인',
            imageAlt: 'Custom image2',
          })
        }

        this.onClick = false
      })
    },
    uploadDelete() {
      if (this.onClick){
        this.$swal('','유사도 분석중에는 사진을 지울 수 없습니다.','warning')
      }else{
        this.uploadImage = null,
        this.uploadPreview = null,
        this.similarity = null
      }
      // const name = e.target.getAttribute("name");
      // image = null
      // this.files = this.files.filter((data) => data.number !== Number(name));
    },
    cameraDelete() {
      if (this.onClick){
        this.$swal('','유사도 분석중에는 사진을 지울 수 없습니다.','warning')
      }else{
        this.cameraImage = null,
        this.cameraPreview = null
        this.similarity = null
      } 
      },
    isValid(){
      this.$swal('','유사도 측정을 위해서는\n'+'사진이 모두 업로드되어야 합니다.','warning')
    },
    emitSimilarity(){
      const similarity = parseInt(this.similarity)
      // console.log(similarity)
      axios.post(USERAPI.BASE_URL + '/images/similarity/', {'similarity':similarity}, this.config)
      .then((res)=>{
        res
        // console.log(res)
        // this.setSimilarity(res.data.similarity)
        // console.log(res.data.similarity)
        this.setSimilarity(similarity)
        this.$router.push({name:'Main'})
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  created(){
    console.log(this.userInfo)
  }
  // watch:{
  //   showSimilarity(){
  //     if (this.similarity){
  //       this.$refs.fan

  //     }
  //   }
  // }

}
</script>

<style lang="scss" scoped>

    @import "@/assets/scss/user/upload.scss";
</style>