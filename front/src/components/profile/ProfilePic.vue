<template>
  <div class="container-profilepic hide">
      <div class="profilepic-background" @click="closeModal"></div>
      <div class="profilepic-modal">
          <!-- <i @click="closeModal" class="fas fa-times btn-close"></i>
          <div class="modal-header">
            프로필 사진 변경
          </div> -->
          <div class="modal-body">
              <div class="upload-img">
                  <div class="upload-preview" @click="clickUploadBtn"></div>
                  <label><img class="icon-pic" src="@/assets/images/icon/album.png"></label>
                  <input type="file" accept="image/jpg, image/jpeg" id="uploadedImg" @change="previewUpload">
              </div>
              <div class="border"></div>
              <div class="camera-img">
                  <div class="camera-preview" @click="clickCameraBtn"></div>
                  <label><img class="icon-pic" src="@/assets/images/icon/camera2.png"></label>
                  <input type="file" accept="image/jpg, image/jpeg" capture="camera" id="cameraImg" @change="previewCamera">
              </div>
              <div class="similarity" v-if="!similarityChecked">
                  <Loading v-if="loading" />
                  <button class="btn btn-similarity" @click="getSimilarity" v-if="!loading">유사도<br>측정하기</button>
              </div>
              <div class="similarity" v-if="similarityChecked">
                  <div class="content-similarity">{{ similarity }}<span>%</span></div>
                  <button class="btn btn-similarity-redo" @click="getSimilarity" v-if="!loading">재측정</button>
              </div>
          </div>
          <div class="modal-footer">
              <button class="btn btn-save" @click="saveChanges">프로필 사진으로 지정</button>
          </div>
      </div>

  </div>
</template>

<script>
import UserApi from "@/api/UserApi.js";
import axios from "axios";
import { mapGetters, mapMutations } from "vuex";

import Loading from "@/components/profile/Loading.vue";

export default {
    name: "ProfilePic",
    components: {
        Loading,
    },
    data() {
        return {
            uploadedfile: "",
            uploadedURL: "",
            camerafile: "",
            cameraURL: "",
            loading: false,
            similarityChecked: false,
            similarity: null,
        }
    },
    computed: {
        ...mapGetters({
            authToken: "user/getAuthToken",
            config: "user/config",
        }),
    },
    methods: {
        ...mapMutations({
            setSimilarity: "user/setSimilarity",
        }),
        closeModal() {
            document.querySelector(".container-profilepic").classList.add("hide")
        },
        clickUploadBtn() {
            document.querySelector("#uploadedImg").click();
        },
        clickCameraBtn() {
            document.querySelector("#cameraImg").click();
        },
        previewUpload(event) {
            var preview = document.querySelector('.upload-preview');
            this.uploadedfile = event.target.files[0];
            this.uploadedURL = URL.createObjectURL(event.target.files[0]);
            preview.style.backgroundImage = `url('${this.uploadedURL}')`;
        },
        previewCamera(event) {
            var preview = document.querySelector('.camera-preview');
            this.camerafile = event.target.files[0];
            this.cameraURL = URL.createObjectURL(event.target.files[0]);
            preview.style.backgroundImage = `url('${this.cameraURL}')`;
        },
        getSimilarity(event) {
            this.loading = true;
            this.similarityChecked = false;
            event.target.disabled = true;
            let formData = new FormData();
            formData.append("image1", this.uploadedfile);
            formData.append("image2", this.camerafile);
            
            axios.post(
                `${UserApi.BASE_URL}/images/analysis/`,
                formData,
                {
                    headers: {
                        Authorization: "JWT "+this.authToken,
                        "Content-Type": "multipart/form-data",
                    }
                }
            )
            .then((res) => {
                this.loading = false
                this.similarityChecked = true;
                event.target.disabled = false;
                this.similarity = parseInt(res.data.similarity);
                document.querySelector(".btn-save").classList.add("btn-save-active");
            })
            .catch((err) => {
                if (err.msg == "fail") {
                    alert("얼굴을 찾을 수 없습니다...😢")
                }
                else {
                    alert("사진이 등록되지 않았습니다 🙁📷")
                }
                this.loading = false;
                event.target.disabled = false;

                })
        },
        saveChanges() {
            this.uploadImages();
        },
        uploadImages() {
            let formData = new FormData();
            formData.append("image", this.uploadedfile);
            axios.post(`${UserApi.BASE_URL}/images/upload/`, 
                formData, 
                {
                    headers: {
                        Authorization: this.authToken,
                        "Content-Type": "multipart/form-data",
                    }
                }
            )
            .then((res) => {
                console.log(res)
                this.uploadSimilarity();
            })
            .catch(err => {
                alert("프로필 이미지 등록에 실패했습니다. 다시 시도해주세요.")
                console.log(err)
            })
        },
        uploadSimilarity() {
            axios.post(`${UserApi.BASE_URL}/images/similarity/`, {"similarity": this.similarity}, this.config)
            .then((res) => {
                this.setSimilarity(res.data.similarity);
            })
            .catch(() => {
                // alert("프로필 이미지 등록에 실패했습니다. 다시 시도해주세요.")
            })
        }
    },
    mounted() {
        this.uploadedfile = ""
        this.uploadedURL = ""
        this.camerafile = ""
        this.cameraURL = ""
        this.loading = false
        this.similarityChecked = false
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/profile/profilepic.scss"
</style>