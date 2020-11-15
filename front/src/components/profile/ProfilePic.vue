<template>
  <div class="container-profilepic hide">
      <div class="profilepic-background" @click="closeModal"></div>
      <div class="profilepic-modal">
          <div class="modal-body">
              <div class="upload-img">
                  <div class="upload-preview" @click="clickUploadBtn"></div>
                  <label><img class="icon-pic" src="@/assets/images/icon/album.png"></label>
                  <input type="file" accept="image/png, image/jpeg" id="uploadedImg" @change="previewUpload">
              </div>
              <div class="border"></div>
              <div class="camera-img">
                  <div class="camera-preview" @click="clickCameraBtn"></div>
                  <label><img class="icon-pic" src="@/assets/images/icon/camera2.png"></label>
                  <input type="file" accept="image/*" capture="camera" id="cameraImg" @change="readURL">
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
            authToken: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDIsInVzZXJuYW1lIjoiXHViMGE4XHViM2Q5XHVhZGRjZ29vZ2xlIiwiZXhwIjoxNjA1OTYzOTc5LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjA1MzU5MTc5fQ.xB_N9qx9AK6GSTx03FnNWhQWgaakg_XqY2Vy8NCQeN0",
        }
    },
    computed: {
        ...mapGetters({
            // authToken: "user/getAuthToken",
            config: "user/config",
            // similarity: "user/getSimilarity",
        }),
        // ...mapGetters('user',['getAuthToken']),
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
        previewCamera() {
            var preview = document.querySelector('.camera-preview');
            // this.camerafile = event.target.files[0];
            // this.cameraURL = URL.createObjectURL(event.target.files[0]);
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
                        "Authorization": this.authToken,
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
        },
        readURL(event) {
            var btn = event.target;
            btn.disabled = true;
            let result = this.resizeMe(event.target.files[0]);
            result.then((url) => {
                this.cameraURL = url;
                this.previewCamera();
                this.createFile();
                btn.disabled = false;
            }).catch(err => alert(err))
        },
        resizeMe(file) {
            return new Promise(function(resolve, reject) {
                var dataURL = "x";
                var reader = new FileReader();
                reader.onloadend = function () {
                var tempImg = new Image();
                tempImg.src = reader.result;
                tempImg.onload = function () {
                    var MAX_WIDTH = 800;
                    var MAX_HEIGHT = 600;
                    var tempW = tempImg.width;
                    var tempH = tempImg.height;
                    if (tempW > tempH) {
                        if (tempW > MAX_WIDTH) {
                            tempH *= MAX_WIDTH / tempW;
                            tempW = MAX_WIDTH;
                        }
                    } else {
                        if (tempH > MAX_HEIGHT) {
                            tempW *= MAX_HEIGHT / tempH;
                            tempH = MAX_HEIGHT;
                        }
                    }
            
                    var canvas = document.createElement('canvas');
                    canvas.width = tempW;
                    canvas.height = tempH;
                    var ctx = canvas.getContext("2d");
                    if (document.documentElement.clientWidth < 674) {
                        canvas.width = tempH;
                        canvas.height = tempW;
                        // var ctx = canvas.getContext("2d");
                        ctx.translate(tempH, 0);
                        ctx.rotate(90 * Math.PI / 180);
                    }
                    ctx.drawImage(this, 0, 0, tempW, tempH);
                    dataURL = canvas.toDataURL("image/jpeg");
                    resolve(dataURL);
                };
                tempImg.onerror = function(err) {
                    console.log(err)
                    reject("can't load the image");
                }
            };
            reader.readAsDataURL(file);
            });
        },
        async createFile() {
            await fetch(this.cameraURL)
                .then((res) => {
                    let data = res.blob();
                    let metadata = {
                        type: "image/jpeg",
                    }
                    this.camerafile = new File([data], "photoTaken.jpg", metadata);
                    console.log(this.camerafile)
                })
                .catch((err) => console.log(err))
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