const userSearchForm = document.querySelector('.search-user')
const changeUsernameForm = document.querySelector('.change-username')

// 查詢會員姓名
function searchUser(find){
    find.preventDefault()
    const search = this.querySelector('input').value
    const searchResult = this.querySelector('p')
    let url = `/api/members?username=${search}`
    fetch(url)
        .then(res => res.json())
        .then(data => {
            const name = data['data']['name']
            const username = data['data']['username']
            searchResult.innerText = `${name}(${username})`
        })
        .catch(error =>{
            searchResult.innerText = '無此會員'
        })
}

// 更新會員姓名
function changeUsername(change){
    change.preventDefault()
    const url = '/api/member'
    const newName = this.querySelector('input').value
    const changeResult = this.querySelector('p')
    fetch(url, {
        method: 'POST',
        headers:{
            'Contnet-Type': 'application/json'
        },
        body: JSON.stringify({
            'name': `${newName}`
        })
    })
        .then(res => res.json())
        .then(data => {
            if(data['ok']){
                changeResult.innerText = '更新成功'
            }else{
                changeResult.innerText = '更新失敗'
            }
        })
}

userSearchForm.addEventListener('submit', searchUser)
changeUsernameForm.addEventListener('submit', changeUsername)
