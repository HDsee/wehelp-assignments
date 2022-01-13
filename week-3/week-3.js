const ham = document.querySelector(".hamburger");
const frame = document.querySelector(".frame");
const menu = document.querySelector(".menu");
const gallery = document.querySelector(".gallery");
const loadmore = document.querySelector(".load");
let listcount = 0

function toggleNavBar(){
    menu.classList.toggle("nav-display");
}

const getlist = async () => {
    axios.get('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
        .then((res) => {
            const list = res.data.result.results
                for ( let i = listcount; i < listcount +8; i++){
                    const stitle = list[i]['stitle']
                    let url = 'http' + list[i]['file'].split('http')[1]
                        a =(url.toLocaleLowerCase()) 

                    const imgLocation = document.createElement('div')
                    imgLocation.classList.add('img-location')
                    const imgBase = document.createElement('div')
                    imgBase.classList.add('img-base')
                    const imgSelf = document.createElement('img')
                    imgSelf.classList.add('img-self')
                    const imgText = document.createElement('div')
                    imgText.classList.add('img-text')

                    imgSelf.setAttribute('src', a)
                    imgText.textContent = stitle
                    imgText.setAttribute('title', stitle)
                    imgBase.appendChild(imgSelf)
                    imgLocation.append(imgBase, imgText)
                    gallery.appendChild(imgLocation)
                }
            listcount +=8
        })
}
ham.addEventListener("click", toggleNavBar)
loadmore.addEventListener('click', getlist)
getlist()
