class SingleImageUpload{get options(){return{fileSelectCallback:null}}
constructor(t,e={}){this.settings=Object.assign(this.options,e),this.element=t,t?this._init():console.error("Single image upload element is not defined!")}_init(){this.button=this.element.getElementsByTagName("button")[0],this.input=this.element.getElementsByTagName("input")[0],this.img=this.element.getElementsByTagName("img")[0],this._addListeners()}_addListeners(){this.button&&this.button.addEventListener("click",this._onSelectButtonClick.bind(this)),this.input&&this.input.addEventListener("change",this._onInputChange.bind(this))}_onSelectButtonClick(t){this.input.dispatchEvent(new MouseEvent("click"))}_onInputChange(t){this._fileSelected()}_fileSelected(){if(this.input.files&&this.input.files[0]){var t=new FileReader;t.onload=this._onFileLoad.bind(this),t.readAsDataURL(this.input.files[0])}}_onFileLoad(t){if(this.img.setAttribute("src",t.target.result),this.settings.fileSelectCallback){let e=this.input.files[0];this.settings.fileSelectCallback({file:e,result:t.target.result})}}getFile(){return this.input.files[0]}}